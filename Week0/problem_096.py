#PROBLEM 96 - TEXT ENCODING ENGINE (COMPREHENSIVE WEEK 0 TEST)
def main():
    result1 = text_encoder("Programming", "forward", 5)
    result2 = text_encoder("DataScience123", "reverse", 8)
    result3 = text_encoder("Hello World!", "double", 3)
    
    print(result1)
    print(result2)
    print(result3)


def text_encoder(text_input, encoding_mode, shift_value):

    #ENCODING LOGIC (EXACTLY WHAT YOU MUST IMPLEMENT):
    #Step 1: Character Analysis

    #Count total characters in text_input
    text_length = len(text_input)

    #Count vowels (a, e, i, o, u, A, E, I, O, U) in text_input
    vowel_count = text_input.count("a")+text_input.count("e")+text_input.count("i")+text_input.count("o")+text_input.count("u")+text_input.count("A")+text_input.count("E")+text_input.count("I")+text_input.count("U")+text_input.count("a")

    #Count consonants (all other alphabetic characters) in text_input
    consonauts_count = (
                        text_input.count("b") + text_input.count("c") + text_input.count("d") +
                        text_input.count("f") + text_input.count("g") + text_input.count("h") +
                        text_input.count("j") + text_input.count("k") + text_input.count("l") +
                        text_input.count("m") + text_input.count("n") + text_input.count("p") +
                        text_input.count("q") + text_input.count("r") + text_input.count("s") +
                        text_input.count("t") + text_input.count("v") + text_input.count("w") +
                        text_input.count("x") + text_input.count("y") + text_input.count("z") +
                        text_input.count("B") + text_input.count("C") + text_input.count("D") +
                        text_input.count("F") + text_input.count("G") + text_input.count("H") +
                        text_input.count("J") + text_input.count("K") + text_input.count("L") +
                        text_input.count("M") + text_input.count("N") + text_input.count("P") +
                        text_input.count("Q") + text_input.count("R") + text_input.count("S") +
                        text_input.count("T") + text_input.count("V") + text_input.count("W") +
                        text_input.count("X") + text_input.count("Y") + text_input.count("Z")
                    )
    #Count non-alphabetic characters in text_input
    digit_count = text_input.count("0")+text_input.count("1")+text_input.count("2")+text_input.count("3")+text_input.count("4")+text_input.count("5")+text_input.count("6")+text_input.count("7")+text_input.count("8")+text_input.count("9")

    vowel_score = vowel_count * shift_value * (encoding_mode == "forward") + (vowel_count * (26 - shift_value))*(encoding_mode == "reverse") + (vowel_count * shift_value * 2)**(encoding_mode == "double")

    consonant_score = (consonauts_count * (shift_value + 3))*(encoding_mode == "forward")+(consonauts_count * (30 - shift_value))*(encoding_mode == "reverse")+(consonauts_count * shift_value * 3)*(encoding_mode == "double")

    position_weight = 1.25*(text_length%2 == 0)+1.75*(text_length %2 !=0)

    total_score = (vowel_score + consonant_score) * position_weight

    Encoding_Complexity = "HIGH"*(total_score >= 200) +  "MEDIUM"*(100 <= total_score < 200) + "LOW"*(total_score < 100)


    efficiency_ratio = total_score / ( text_length + digit_count + 1)

    security = "SECURE"*(efficiency_ratio >= 15) + "STANDARD"*(8 <= efficiency_ratio < 15) +  "BASIC"*(efficiency_ratio < 8)


    return f"{Encoding_Complexity}:{security}:{total_score:.1f}:{efficiency_ratio:.2f}:{vowel_count}:{consonauts_count}:{encoding_mode}"

main()
