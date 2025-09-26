#PROBLEM 97 - CHECKSUM VERIFICATION ENGINE (COMPREHENSIVE WEEK 0 TEST)
def main():
    result1 = checksum_verifier("SecureData", "simple", "standard")
    result2 = checksum_verifier("Verify123", "weighted", "enhanced")
    result3 = checksum_verifier("TestXYZ", "complex", "secure")
    
    print(result1)
    print(result2)
    print(result3)

def checksum_verifier(data_string, algorithm_type, verification_mode):

    #Step 1: Data Preparation

    #Count total characters in data_string
    data_length = len(data_string)
#Count uppercase letters (A-Z) in data_string
    uppercase_count = (
                        data_string.count("A") + data_string.count("B") + data_string.count("C") +
                        data_string.count("D") + data_string.count("E") + data_string.count("F") +
                        data_string.count("G") + data_string.count("H") + data_string.count("I") +
                        data_string.count("J") + data_string.count("K") + data_string.count("L") +
                        data_string.count("M") + data_string.count("N") + data_string.count("O") +
                        data_string.count("P") + data_string.count("Q") + data_string.count("R") +
                        data_string.count("S") + data_string.count("T") + data_string.count("U") +
                        data_string.count("V") + data_string.count("W") + data_string.count("X") +
                        data_string.count("Y") + data_string.count("Z")
                    )

#Count lowercase letters (a-z) in data_string
    lowercase_count = (
                        data_string.count("a") + data_string.count("b") + data_string.count("c") +
                        data_string.count("d") + data_string.count("e") + data_string.count("f") +
                        data_string.count("g") + data_string.count("h") + data_string.count("i") +
                        data_string.count("j") + data_string.count("k") + data_string.count("l") +
                        data_string.count("m") + data_string.count("n") + data_string.count("o") +
                        data_string.count("p") + data_string.count("q") + data_string.count("r") +
                        data_string.count("s") + data_string.count("t") + data_string.count("u") +
                        data_string.count("v") + data_string.count("w") + data_string.count("x") +
                        data_string.count("y") + data_string.count("z")
                      )
#Count digits (0-9) in data_string

    digit_count = (data_string.count("0") + data_string.count("1") + data_string.count("2") +
                    data_string.count("3") + data_string.count("4") + data_string.count("5") +
                    data_string.count("6") + data_string.count("7")+ data_string.count("8") +
                    data_string.count("9") 
                    )

    position_sum = (data_length * (data_length + 1)) / 2

    base_checksum = ((uppercase_count * 7) + (lowercase_count * 5) + (digit_count * 3))*(algorithm_type == "simple") + ((uppercase_count * position_sum) + (lowercase_count * 11) + (digit_count * 13))*(algorithm_type == "weighted")+((uppercase_count * 17) + (lowercase_count * position_sum) + (digit_count * 19))*(algorithm_type == "complex")


    final_checksum = (base_checksum * (verification_mode == "standard")) + base_checksum * 2 * (verification_mode == "enhanced") +  (base_checksum + position_sum)*(verification_mode == "secure")

    verification_digit = final_checksum % 97
    Verification_Status = "VERIFIED"*(verification_digit >= 50) + "UNVERIFIED"*(verification_digit < 50) 

    integrity_score = (final_checksum * data_length) / (uppercase_count + lowercase_count + digit_count + 1)

    Confidence_Level = "HIGH"*(integrity_score >= 1000) + "MEDIUM"*(500 <= integrity_score < 1000) + "LOW"*(integrity_score < 500)


    return f"{Verification_Status}:{ Confidence_Level}:{verification_digit}:{integrity_score:.1f}:{final_checksum}:{position_sum}:{data_length}"

main()
