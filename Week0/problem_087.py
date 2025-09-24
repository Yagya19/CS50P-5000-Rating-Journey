#PROBLEM 87 - ANOMALY DETECTION SYSTEM (COMPLETE CHALLENGE FORMAT)
def main():
    result1 = anomaly_detector("statistical", "normal123⚠outlier456❗extreme⛔spike", 2, 3, 1)
    result2 = anomaly_detector("ml", "pattern248⚠anomaly567❗deviation", 1, 2, 2)
    result3 = anomaly_detector("rule", "baseline135❗breach⛔violation", 3, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def anomaly_detector(detection_type, sample_data, deviation_threshold, analysis_rounds, precision_level):
    #Step 1: Count Anomaly Detection Elements

    #sample_volume: Count total characters in sample_data
    sample_volume = len(sample_data)
    #measurement_points: Count digit characters (0-9) in sample_data
    measurement_points = sample_data.count("0") + sample_data.count("1") +  sample_data.count("2") + sample_data.count("3") +  sample_data.count("4") + sample_data.count("5") + sample_data.count("6") +  sample_data.count("7") + sample_data.count("8") +  sample_data.count("9") 
    #outlier_flags: Count anomaly flag characters ("⚠", "❗", "⛔") in sample_data
    outlier_flags = sample_data.count("⚠") + sample_data.count("❗") +  sample_data.count("⛔")

    Anomaly_Detection_Complexity_Score = (sample_volume * 20) + (measurement_points * 40) + (outlier_flags * 85)
    Detection_Multiplier = 6.9*(detection_type=="statistical") +  6.4*(detection_type=="ml") +  5.9*(detection_type=="rule") 
    Outlier_Analysis_Projection =  Anomaly_Detection_Complexity_Score * Detection_Multiplier * analysis_rounds
    Raw_Detection_Sensitivity_Index = Outlier_Analysis_Projection - (deviation_threshold * 220)
    Detection_Sensitivity_Index = Raw_Detection_Sensitivity_Index * (Raw_Detection_Sensitivity_Index >=440) + 440*(Raw_Detection_Sensitivity_Index <440)
    Anomaly_Concentration_Ratio = measurement_points / (sample_volume + (sample_volume==0)) * (sample_volume!=0) + 2.1*(sample_volume==0)
    Detection_Reliability = (Anomaly_Concentration_Ratio * 100) + (analysis_rounds * 110)
    Detection_Type_Complexity =  10*(detection_type=="statistical") +  12*(detection_type=="ml") +  8*(detection_type=="rule") 
    Sensitivity_Categories = "High_Sensitivity"*(Detection_Sensitivity_Index>=1100) + "Medium_Sensitivity"*(820<=Detection_Sensitivity_Index<1100) + "Low_Sensitivity"*(Detection_Sensitivity_Index<820) 
    Analysis_Categories = "Multi_Round_Analysis"*(analysis_rounds == 3) + "Dual_Round_Analysis"*(analysis_rounds == 2) + "Single_Round_Analysis"*(analysis_rounds == 1) 
    Outlier_Severity = (outlier_flags * 210) / (measurement_points+(measurement_points==0)) * (measurement_points!=0) + 230*(measurement_points==0)
    Detection_Signature = detection_type + str(analysis_rounds) + str(deviation_threshold) + Sensitivity_Categories 

    return f"DETECTED: {Analysis_Categories} | TYPE: {detection_type} | VOLUME: {sample_volume} | POINTS: {measurement_points} | FLAGS: {outlier_flags} | INDEX: {Detection_Sensitivity_Index:.1f} | RELIABILITY: {Detection_Reliability:.1f}% | CONCENTRATION: {Anomaly_Concentration_Ratio:.3f} | SEVERITY: {Outlier_Severity:.1f}% | CATEGORY: {Sensitivity_Categories} | COMPLEXITY: {Detection_Type_Complexity} | SIG: {Detection_Signature}"

main()
