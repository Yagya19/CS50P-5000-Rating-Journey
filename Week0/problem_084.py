#PROBLEM 84 - BEHAVIORAL PATTERN DETECTOR (COMPLETE CHALLENGE FORMAT)
def main():
    result1 = behavior_detector("routine", "daily123♦work456◊sleep△pattern", 2, 3, 1)
    result2 = behavior_detector("adaptive", "change248♦learn567△adapt", 1, 2, 2)
    result3 = behavior_detector("random", "chaos135◊varied△unpredictable", 3, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def behavior_detector(behavior_type, activity_data, pattern_threshold, detection_cycles, precision_level):
    #Step 1: Count Behavioral Elements

    #activity_span: Count total characters in activity_data
    activity_span = len(activity_data)
    #behavior_indicators: Count digit characters (0-9) in activity_data
    behavior_indicators = activity_data.count("0")+activity_data.count("1")+activity_data.count("2")+activity_data.count("3")+activity_data.count("4")+activity_data.count("5")+activity_data.count("6")+activity_data.count("7")+activity_data.count("8")+activity_data.count("9")
    #pattern_signals: Count behavioral marker characters ("♦", "◊", "△") in activity_data
    pattern_signals = activity_data.count("♦")+activity_data.count("◊")+activity_data.count("△")
    
    #MATHEMATICAL FORMULAS (COMPLETE):
    Behavioral_Analysis_Complexity_Score = (activity_span * 17) + (behavior_indicators * 34) + (pattern_signals * 70)
    Behavior_Multiplier = 6.0*(behavior_type=="routine")+ 5.5*(behavior_type=="adaptive")+ 5.1*(behavior_type=="random")
    Pattern_Recognition_Projection = Behavioral_Analysis_Complexity_Score  *  Behavior_Multiplier * detection_cycles
    Raw_Behavioral_Confidence_Index =  Pattern_Recognition_Projection - (pattern_threshold * 190)
    Behavioral_Confidence_Index = Raw_Behavioral_Confidence_Index *(Raw_Behavioral_Confidence_Index >=380) + 380*(Raw_Behavioral_Confidence_Index <380)
    Activity_Concentration_Ratio = behavior_indicators / (activity_span + (activity_span ==0))*(activity_span !=0) + 1.8*(activity_span ==0)
    Detection_Confidence = (Activity_Concentration_Ratio  * 100) + (detection_cycles * 95)
    Behavior_Type_Complexity = 7*(behavior_type=="routine")+ 9*(behavior_type=="adaptive")+ 11*(behavior_type=="random")
    Confidence_Categories = "High_Behavioral_Confidence"*(Behavioral_Confidence_Index >=950) + "Medium_Behavioral_Confidence"*(700<=Behavioral_Confidence_Index<950) + "Low_Behavioral_Confidence"*(Behavioral_Confidence_Index <700)
    Detection_Categories = "Intensive_Behavior_Detection"*(detection_cycles == 3) + "Standard_Behavior_Detection"*(detection_cycles == 2) + "Basic_Behavior_Detection"*(detection_cycles == 1) 
    Pattern_Consistency = (pattern_signals * 180) / (behavior_indicators+(behavior_indicators==0)) * (behavior_indicators!=0) + 200*(behavior_indicators==0)
    Behavioral_Signature = behavior_type + str(detection_cycles) + str(pattern_threshold) +  Confidence_Categories

    return f"DETECTED: {Detection_Categories} | TYPE: {behavior_type} | SPAN: {activity_span} | INDICATORS: {behavior_indicators} | SIGNALS: {pattern_signals} | INDEX: {Behavioral_Confidence_Index:.1f} | CONFIDENCE: {Detection_Confidence:.1f}% | CONCENTRATION: {Activity_Concentration_Ratio:.3f} | CONSISTENCY: {Pattern_Consistency:.1f}% | CATEGORY: {Confidence_Categories} | COMPLEXITY: {Behavior_Type_Complexity} | SIG: {Behavioral_Signature}"

main()
