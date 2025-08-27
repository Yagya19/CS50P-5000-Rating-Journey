def main():
    result1 = pattern_detector("sequence", "abc123abc456", 2, 1, 1)
    result2 = pattern_detector("numeric", "112233445566", 3, 2, 2)
    result3 = pattern_detector("text", "hello world test", 1, 3, 1)
    
    print(result1)
    print(result2)
    print(result3)

def pattern_detector(pattern_type, data_sequence, detection_sensitivity, pattern_threshold, precision_level):
    #Step 1: Count Sequence Elements

    #sequence_length: Count total characters in data_sequence
    only_chars = data_sequence.replace(" ","")
    sequence_length = len(only_chars)
    #digit_patterns: Count digit characters (0-9) in data_sequence\
    digit_patterns = only_chars.count("0") +   only_chars.count("1") +   only_chars.count("2") +  only_chars.count("3") +   only_chars.count("4") +   only_chars.count("5") + only_chars.count("6") +   only_chars.count("7") +  only_chars.count("8") +   only_chars.count("9")
    
    #repeat_elements: Count characters that appear more than once in data_sequence
    #repeat_elements: Count characters that appear more than once in data_sequence 
    
    Repeating_Count =  (only_chars.count("a")>1) + (only_chars.count("b")>1) + (only_chars.count("c")>1) + (only_chars.count("d")>1) + (only_chars.count("e")>1) + (only_chars.count("f")>1) + (only_chars.count("g")>1) + (only_chars.count("h")>1) + (only_chars.count("i")>1) + (only_chars.count("j")>1) + (only_chars.count("k")>1) + (only_chars.count("l")>1) + (only_chars.count("m")>1) + (only_chars.count("n")>1) + (only_chars.count("o")>1) + (only_chars.count("p")>1) + (only_chars.count("q")>1) + (only_chars.count("r")>1) + (only_chars.count("s")>1) + (only_chars.count("t")>1) + (only_chars.count("u")>1) + (only_chars.count("v")>1) + (only_chars.count("w")>1) + (only_chars.count("x")>1) + (only_chars.count("y")>1) + (only_chars.count("z")>1) + (only_chars.count("A")>1) + (only_chars.count("B")>1) + (only_chars.count("C")>1) + (only_chars.count("D")>1) + (only_chars.count("E")>1) + (only_chars.count("F")>1) + (only_chars.count("G")>1) + (only_chars.count("H")>1) + (only_chars.count("I")>1) + (only_chars.count("J")>1) + (only_chars.count("K")>1) + (only_chars.count("L")>1) + (only_chars.count("M")>1) + (only_chars.count("N")>1) + (only_chars.count("O")>1) + (only_chars.count("P")>1) + (only_chars.count("Q")>1) + (only_chars.count("R")>1) + (only_chars.count("S")>1) + (only_chars.count("T")>1) + (only_chars.count("U")>1) + (only_chars.count("V")>1) + (only_chars.count("W")>1) + (only_chars.count("X")>1) + (only_chars.count("Y")>1) + (only_chars.count("Z")>1) + (only_chars.count("0")>1) + (only_chars.count("1")>1) + (only_chars.count("2")>1) + (only_chars.count("3")>1) + (only_chars.count("4")>1) + (only_chars.count("5")>1) + (only_chars.count("6")>1) + (only_chars.count("7")>1) + (only_chars.count("8")>1) + (only_chars.count("9")>1)
    
    # Apply detection multiplier 
    Detection_Multiplier = 1.4*(pattern_type=="sequence")+1.6*(pattern_type=="numeric")+1.2*(pattern_type=="text")
    Pattern_Complexity_Score = (sequence_length*2) + (digit_patterns*5) + (Repeating_Count*3)
    Pattern_Strength_Index = Pattern_Complexity_Score * Detection_Multiplier * detection_sensitivity
    unchecked_Detection_Confidence = Pattern_Strength_Index - (pattern_threshold * 25)
    Detection_Confidence = unchecked_Detection_Confidence*(unchecked_Detection_Confidence>=60) + 60*(unchecked_Detection_Confidence<60)
    Pattern_Density_Ratio =  (Repeating_Count / sequence_length)*(sequence_length!=0) + 0.3*(sequence_length==0)
    Recognition_Accuracy = (Pattern_Density_Ratio * 100) + (detection_sensitivity * 12)
    Pattern_Type_Complexity = 7*(pattern_type=="sequence")+5*(pattern_type=="numeric")+6*(pattern_type=="text")
    Detection_Categories = "Strong"*(Detection_Confidence >= 150) + "Moderate"*(90<=Detection_Confidence<150) + "Weak"*(Detection_Confidence<90)
    Sensitivity_Categories ="High_Sensitivity"*(detection_sensitivity == 3)+"Medium_Sensitivity"*(detection_sensitivity == 2)+"Low_Sensitivity"*(detection_sensitivity == 1)
    Pattern_Efficiency = (digit_patterns / Repeating_Count )*20 *(Repeating_Count !=0) + 40*(Repeating_Count ==0)
    Pattern_Signature = pattern_type + str(detection_sensitivity) + str(pattern_threshold) + Detection_Categories 
    
    return f"DETECTED: {Sensitivity_Categories} | TYPE: {pattern_type} | LENGTH: {sequence_length} | DIGITS: {digit_patterns} | REPEATS: {Repeating_Count} | CONFIDENCE: {Detection_Confidence:.1f} | ACCURACY: {Recognition_Accuracy:.1f}% | DENSITY: {Pattern_Density_Ratio :.3f} | EFFICIENCY: {Pattern_Efficiency:.1f}% | CATEGORY: {Detection_Categories} | COMPLEXITY: {Pattern_Type_Complexity} | SIG: {Pattern_Signature}"

main()





