def main():
    result1 = data_validator("phone", "1234567890", 2, 3, 1)
    result2 = data_validator("email", "user@domain.com", 1, 2, 2)
    result3 = data_validator("password", "mypass123", 3, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def data_validator(data_type, input_data, validation_rules, strictness_level, precision_level): 

    data_length = len(input_data)
    numeric_elements = input_data.count("0")+ input_data.count("1")+input_data.count("2")+input_data.count("3")+input_data.count("4")+input_data.count("5")+input_data.count("6")+input_data.count("7")+input_data.count("8")+input_data.count("9")
    alpha_elements = (input_data.count("a") + input_data.count("b") + input_data.count("c") + 
                        input_data.count("d") + input_data.count("e") + input_data.count("f") +
                        input_data.count("g") + input_data.count("h") + input_data.count("i") +
                        input_data.count("j") + input_data.count("k") + input_data.count("l") +
                        input_data.count("m") + input_data.count("n") + input_data.count("o") +
                        input_data.count("p") + input_data.count("q") + input_data.count("r") +
                        input_data.count("s") + input_data.count("t") + input_data.count("u") +
                        input_data.count("v") + input_data.count("w") + input_data.count("x") +
                        input_data.count("y") + input_data.count("z") +
                        input_data.count("A") + input_data.count("B") + input_data.count("C") +
                        input_data.count("D") + input_data.count("E") + input_data.count("F") +
                        input_data.count("G") + input_data.count("H") + input_data.count("I") +
                        input_data.count("J") + input_data.count("K") + input_data.count("L") +
                        input_data.count("M") + input_data.count("N") + input_data.count("O") +
                        input_data.count("P") + input_data.count("Q") + input_data.count("R") +
                        input_data.count("S") + input_data.count("T") + input_data.count("U") +
                        input_data.count("V") + input_data.count("W") + input_data.count("X") +
                        input_data.count("Y") + input_data.count("Z"))

   # Step 2: Apply Validation Rules Based on Data Type

    """If data_type = "phone": Count digits and check for exactly 10 digits
    If data_type = "email": Count "@" symbols and check for exactly 1 "@" symbol
    If data_type = "password": Count total characters and check for minimum 8 characters"""

    Phone_Check = (data_type=="phone")*(numeric_elements==10) 
    Email_Check = (data_type=="email")*(input_data.count("@")==1)
    Password_Check = (data_type=="password")*(len(input_data)>=8) 

    Format_Compliance = Phone_Check+Email_Check+Password_Check

    #Formula: 20 Data Integrity Score: / Formula: (numeric_elements + alpha_elements) × validation_rules + format_bonus / Format Bonus:Formula: 20 if format requirements met, 0 if not metif format requirements met, 0 if not met
    
    Format_Bonus = 20*(Format_Compliance>0)
    Data_Integrity_Score = (numeric_elements + alpha_elements) * validation_rules  + Format_Bonus

    # Validation Confidence:

    Unchecked_Validation_Confidence = (Data_Integrity_Score * strictness_level) - (strictness_level*25) 
    Validation_Confidence = Unchecked_Validation_Confidence*(Unchecked_Validation_Confidence>=50) + 50*(Unchecked_Validation_Confidence<50)
    Valid_elements_ratio = ((numeric_elements + alpha_elements) / data_length)* (data_length != 0)
    Processing_Accuracy = (Valid_elements_ratio*100) + (strictness_level * 15)

    # Complexity Checks 
    Data_Type_Complexity = 6*(data_type=="phone")+8*(data_type=="email")+7*(data_type=="password")

    Validation_Categories = "Secure"*(Validation_Confidence >= 150) + "Valid"*(100<Validation_Confidence<150) + "Weak"*(Validation_Confidence<100)  

    Processing_Categories = "Strict_Validation"* (strictness_level==3)+"Standard_Validation"* (strictness_level==2)+"Basic_Validation"* (strictness_level==1)

    # Signature 
    Data_Efficiency = (alpha_elements / data_length) * 100 *(data_length!=0) + 25*(data_length==0)


    Validation_Signature = data_type + str(strictness_level) + str(validation_rules) + Validation_Categories

    return f"VALIDATED: {Processing_Categories} | TYPE: {data_type} | LENGTH: {data_length} | NUMERIC: {numeric_elements} | ALPHA: {alpha_elements} | CONFIDENCE: {Validation_Confidence:.1f} | ACCURACY: {Processing_Accuracy:.1f}% | EFFICIENCY: {Data_Efficiency:.1f}% | CATEGORY: {Validation_Categories} | COMPLEXITY: {Data_Type_Complexity} | SIG: {Validation_Signature}"

main()
 


    

