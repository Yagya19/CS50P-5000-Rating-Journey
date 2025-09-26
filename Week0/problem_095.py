#PROBLEM 95 - DATA VALIDATION SYSTEM (COMPREHENSIVE WEEK 0 TEST)
def main():
    result1 = data_validator("Hello123!", "strict", 10)
    result2 = data_validator("DataTest2024", "moderate", 5)
    result3 = data_validator("simple", "lenient", 15)
    
    print(result1)
    print(result2)
    print(result3)

def data_validator(data_input, validation_level, error_tolerance):

    #Step 1: Data Analysis

    #Count total characters in data_input
    data_length = len(data_input)
    #Count alphabetic characters (a-z, A-Z) in data_input
    alphabetic_count =  (
                        data_input.count("a") + data_input.count("b") + data_input.count("c") +
                        data_input.count("d") + data_input.count("e") + data_input.count("f") +
                        data_input.count("g") + data_input.count("h") + data_input.count("i") +
                        data_input.count("j") + data_input.count("k") + data_input.count("l") +
                        data_input.count("m") + data_input.count("n") + data_input.count("o") +
                        data_input.count("p") + data_input.count("q") + data_input.count("r") +
                        data_input.count("s") + data_input.count("t") + data_input.count("u") +
                        data_input.count("v") + data_input.count("w") + data_input.count("x") +
                        data_input.count("y") + data_input.count("z") +
                        data_input.count("A") + data_input.count("B") + data_input.count("C") +
                        data_input.count("D") + data_input.count("E") + data_input.count("F") +
                        data_input.count("G") + data_input.count("H") + data_input.count("I") +
                        data_input.count("J") + data_input.count("K") + data_input.count("L") +
                        data_input.count("M") + data_input.count("N") + data_input.count("O") +
                        data_input.count("P") + data_input.count("Q") + data_input.count("R") +
                        data_input.count("S") + data_input.count("T") + data_input.count("U") +
                        data_input.count("V") + data_input.count("W") + data_input.count("X") +
                        data_input.count("Y") + data_input.count("Z")
                        )
    #Count numeric digits (0-9) in data_input
    digit_count = (data_input.count("0") + data_input.count("1") + data_input.count("2") +
                        data_input.count("3") + data_input.count("4") + data_input.count("5") +
                        data_input.count("6") + data_input.count("7") + data_input.count("8") +
                        data_input.count("9"))
    #Count special characters (anything that's not alphabetic or numeric)
    special_count =  (data_input.count("~") + data_input.count("!") + data_input.count("@") +
                        data_input.count("#") + data_input.count("%") + data_input.count("^") +
                        data_input.count("&") + data_input.count("*") + data_input.count("(") +
                        data_input.count(")") )

    #Step 2: Core Validation Calculations

 
    length_score = (data_length * 2)*(data_length <= 10) + (20 + (data_length - 10))*(data_length > 10)
    balance_score = (alphabetic_count * 3) + (digit_count * 2) - (special_count * 1)
    Complexity_Rating = 1.5*(validation_level == "strict")+ 1.2*(validation_level == "moderate")+ 1.0*(validation_level == "lenient")


    #Step 3: Final Validation Metrics
    Total_Score = total_score = (length_score + balance_score) * Complexity_Rating 
    Validation_Status = "VALID"*(total_score>=(50- error_tolerance )) + "INVALID"*(total_score < (50- error_tolerance ))
    Quality_Grade = "A"*(total_score >= 80) + "B"*(60<=total_score >= 80) + "C"*(40<= total_score < 60) + "D"*( 60<= total_score < 80) + "F"*(total_score < 40)


    return f"{Validation_Status}:{Quality_Grade}:{total_score:.1f}:{data_length}:{alphabetic_count}:{digit_count}:{special_count}" 

main()
