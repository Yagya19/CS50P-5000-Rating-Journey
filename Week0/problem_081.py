#PROBLEM 81 - SEQUENCE PATTERN DETECTOR (COMPLETE CHALLENGE FORMAT)
def main():
    result1 = sequence_detector("arithmetic", "seq123*456~789◆pattern", 2, 3, 1)
    result2 = sequence_detector("geometric", "data248*816~sequence", 1, 2, 2)
    result3 = sequence_detector("fibonacci", "series135*813~◆detect", 3, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def sequence_detector(pattern_mode, sequence_data, detection_threshold, analysis_depth, precision_level):
    #Step 1: Count Sequence Elements

    #sequence_size: Count total characters in sequence_data
    sequence_size = len(sequence_data)
    #pattern_elements: Count digit characters (0-9) in sequence_data
    pattern_elements = sequence_data.count("0") + sequence_data.count("1") + sequence_data.count("2") + sequence_data.count("3") + sequence_data.count("4") + sequence_data.count("5") + sequence_data.count("6") + sequence_data.count("7") + + sequence_data.count("8") + sequence_data.count("9")
    #pattern_markers: Count pattern indicator characters ("*", "~", "◆") in sequence_data
    pattern_markers = sequence_data.count("*") + sequence_data.count("~") + sequence_data.count("◆") 

    #MATHEMATICAL FORMULAS (COMPLETE):
    Pattern_Recognition_Complexity_Score = (sequence_size * 14) + (pattern_elements * 28) + (pattern_markers * 55)
    Pattern_Multiplier = 5.1*(pattern_mode=="arithmetic") +  4.6*(pattern_mode=="geometric") + 4.2*(pattern_mode=="fibonacci")
    Detection_Projection = Pattern_Recognition_Complexity_Score * Pattern_Multiplier * analysis_depth
    Raw_Pattern_Confidence_Index = Detection_Projection - (detection_threshold * 160)
    Pattern_Confidence_Index = Raw_Pattern_Confidence_Index * (Raw_Pattern_Confidence_Index >=320) + 320*(Raw_Pattern_Confidence_Index <320)
    Sequence_Regularity_Ratio = pattern_elements / (sequence_size + (sequence_size==0)) *(sequence_size !=0) + 1.5*(sequence_size ==0)
    Recognition_Accuracy = (Sequence_Regularity_Ratio * 100) + (analysis_depth * 80)
    Pattern_Mode_Complexity = 8*(pattern_mode=="arithmetic") +  10*(pattern_mode=="geometric") + 12*(pattern_mode=="fibonacci")
    Confidence_Categories = "Low_Confidence"*(Pattern_Confidence_Index <580)+"Medium_Confidence"*( 580<=Pattern_Confidence_Index <800)+"High_Confidence"*( Pattern_Confidence_Index >=800)
    Analysis_Categories = "Deep_Pattern_Analysis"*(analysis_depth == 3) + "Standard_Pattern_Analysis"*(analysis_depth == 2)+"Surface_Pattern_Analysis"*(analysis_depth == 1)
    Pattern_Consistency = (pattern_markers*150) / (pattern_elements+(pattern_elements==0)) *(pattern_elements!=0) + 170*(pattern_elements==0)
    Pattern_Signature = pattern_mode + str(analysis_depth) + str(detection_threshold) + Confidence_Categories 

    return f"DETECTED: {Analysis_Categories} | MODE: {pattern_mode} | SIZE: {sequence_size} | ELEMENTS: {pattern_elements} | MARKERS: {pattern_markers} | INDEX: {Pattern_Confidence_Index :.1f} | ACCURACY: {Recognition_Accuracy :.1f}% | REGULARITY: {Sequence_Regularity_Ratio:.3f} | CONSISTENCY: {Pattern_Consistency:.1f}% | CATEGORY: {Confidence_Categories } | COMPLEXITY: {Pattern_Mode_Complexity} | SIG: {Pattern_Signature}"

main()
