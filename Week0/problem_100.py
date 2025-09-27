#PROBLEM 100 - INTEGRATED COMPUTATIONAL ANALYZER (FINAL WEEK 0 MASTERY TEST) 
def main():
    result1 = computational_analyzer("Advanced123!Code", 3, "maximum")
    result2 = computational_analyzer("Simple_Test", 2, "enhanced") 
    result3 = computational_analyzer("HELLO world 456", 1, "standard")
    
    print(result1)
    print(result2)
    print(result3)


def computational_analyzer(input_data, analysis_depth, precision_mode):



# Extract all uppercase letters and count them: upper_count

    upper_count = (
                input_data.count("A") + input_data.count("B") + input_data.count("C") +
                input_data.count("D") + input_data.count("E") + input_data.count("F") +
                input_data.count("G") + input_data.count("H") + input_data.count("I") +
                input_data.count("J") + input_data.count("K") + input_data.count("L") +
                input_data.count("M") + input_data.count("N") + input_data.count("O") +
                input_data.count("P") + input_data.count("Q") + input_data.count("R") +
                input_data.count("S") + input_data.count("T") + input_data.count("U") +
                input_data.count("V") + input_data.count("W") + input_data.count("X") +
                input_data.count("Y") + input_data.count("Z")
                )


#Extract all lowercase letters and count them: lower_count
    lower_count = (
                input_data.count("a") + input_data.count("b") + input_data.count("c") +
                input_data.count("d") + input_data.count("e") + input_data.count("f") +
                input_data.count("g") + input_data.count("h") + input_data.count("i") +
                input_data.count("j") + input_data.count("k") + input_data.count("l") +
                input_data.count("m") + input_data.count("n") + input_data.count("o") +
                input_data.count("p") + input_data.count("q") + input_data.count("r") +
                input_data.count("s") + input_data.count("t") + input_data.count("u") +
                input_data.count("v") + input_data.count("w") + input_data.count("x") +
                input_data.count("y") + input_data.count("z")
                )
#Extract all digits and count them: digit_count
    digit_count = (
                input_data.count("0") + input_data.count("1") + input_data.count("2") +
                input_data.count("3") + input_data.count("4") + input_data.count("5") +
                input_data.count("6") + input_data.count("7") + input_data.count("8") +
                input_data.count("9") )
#Extract all special characters (everything else) and count them: 
    special_count = (
                input_data.count("~") + input_data.count("!") + input_data.count("@") +
                input_data.count("#") + input_data.count("$") + input_data.count("%") +
                input_data.count("^") + input_data.count("&") + input_data.count("*") +
                input_data.count("(") + input_data.count(")") )



    total_length = upper_count + lower_count + digit_count + special_count


#Primary Scores:

    character_score = (upper_count * 4) + (lower_count * 3) + (digit_count * 5) + (special_count * 2)
    balance_score = upper_count + lower_count - digit_count - special_count
    complexity_score = (upper_count * lower_count) + (digit_count * special_count) + total_length 

    Depth_Based_Multipliers = 1*(analysis_depth == 1)+1.5*(analysis_depth == 2)+2*(analysis_depth == 3)+2.5*(analysis_depth >= 4)


    base_value = (character_score * Depth_Based_Multipliers)*(precision_mode == "standard") + (character_score + balance_score) * (precision_mode == "enhanced") +  (character_score + balance_score + complexity_score) * Depth_Based_Multipliers* (precision_mode == "maximum")

    performance_index = base_value + (total_length * 2)

    tier = "EXPERT"*( performance_index >= 500) + "ADVANCED"*(300 <= performance_index < 500) + "INTERMEDIATE"*(150 <= performance_index < 300) + "BEGINNER"*(75 <= performance_index < 150) + "NOVICE"*(performance_index < 75)


    efficiency_rating = performance_index / (total_length + analysis_depth + 1)

    efficiency = "OPTIMAL"*(efficiency_rating >= 50) + "GOOD"*(25 <= efficiency_rating < 50) + "AVERAGE"*(10 <= efficiency_rating < 25) + "POOR"*(efficiency_rating < 10)


    Mastery_Indicator = "COMPLETE"*(tier == "EXPERT")*(efficiency == "OPTIMAL") +  "HIGH"*(tier == "EXPERT")*(tier == "ADVANCED")*(efficiency == "OPTIMAL")* (efficiency == "GOOD") + "DEVELOPING"*(tier == "ADVANCED")*(tier == "INTERMEDIATE") + "BASIC"


    return f"{tier}:{efficiency}:{Mastery_Indicator}:{performance_index:.1f}:{efficiency_rating:.2f}:{base_value:.1f}:{character_score}:{balance_score}:{complexity_score}"

main()
