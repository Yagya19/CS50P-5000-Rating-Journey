#PROBLEM 83 - DATA PATTERN ANALYZER (COMPLETE CHALLENGE FORMAT)

def main():
    result1 = data_pattern_analyzer("trend", "values123!456?789▲spike", 2, 3, 1)
    result2 = data_pattern_analyzer("outlier", "dataset248!anomaly?916", 1, 2, 2)
    result3 = data_pattern_analyzer("cyclical", "cycle135?pattern▲847", 3, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def data_pattern_analyzer(analysis_mode, data_stream, anomaly_threshold, pattern_depth, precision_level):
    #Step 1: Count Data Pattern Elements

    #stream_volume: Count total characters in data_stream
    stream_volume = len(data_stream)
    #numerical_values: Count digit characters (0-9) in data_stream
    numerical_values = data_stream.count("0") + data_stream.count("1") + data_stream.count("2") + data_stream.count("3") + data_stream.count("4") + data_stream.count("5") + data_stream.count("6") + data_stream.count("7") + data_stream.count("8") + data_stream.count("9") 
    #anomaly_indicators: Count anomaly marker characters ("!", "?", "▲") in data_stream
    anomaly_indicators = data_stream.count("!") + data_stream.count("?") + data_stream.count("▲")

    #MATHEMATICAL FORMULAS (COMPLETE):
    Data_Analysis_Complexity_Score = (stream_volume * 16) + (numerical_values * 32) + (anomaly_indicators * 65)
    Analysis_Multiplier = 5.7*(analysis_mode=="trend") + 5.2*(analysis_mode=="outlier") +  4.8*(analysis_mode=="cyclical")
    Pattern_Detection_Projection = Data_Analysis_Complexity_Score * Analysis_Multiplier * pattern_depth
    Raw_Anomaly_Detection_Index = Pattern_Detection_Projection - (anomaly_threshold * 180) 
    Anomaly_Detection_Index =  Raw_Anomaly_Detection_Index * ( Raw_Anomaly_Detection_Index>=360) + 360*( Raw_Anomaly_Detection_Index <360)
    Data_Consistency_Ratio = numerical_values / (stream_volume + ( stream_volume == 0)) * ( stream_volume !=0) + 1.7*( stream_volume ==0)
    Detection_Reliability = (Data_Consistency_Ratio * 100) + (pattern_depth * 90)
    Analysis_Mode_Complexity = 8*(analysis_mode=="trend") + 10*(analysis_mode=="outlier") +  12*(analysis_mode=="cyclical")
    Detection_Categories = "Strong_Detection"*(Anomaly_Detection_Index >=900) + "Moderate_Detection"*(660<=Anomaly_Detection_Index<900) + "Weak_Detection"*(Anomaly_Detection_Index<660) 
    Pattern_Categories = "Deep_Data_Analysis"*( pattern_depth == 3) + "Standard_Data_Analysis"*( pattern_depth == 2) + "Surface_Data_Analysis"*( pattern_depth == 2) 
    Anomaly_Severity = (anomaly_indicators * 170 )/ (numerical_values + (numerical_values==0)) * (numerical_values!=0) + 190*(numerical_values==0)
    Analysis_Signature = analysis_mode + str(pattern_depth) + str(anomaly_threshold) + Detection_Categories

    return f"ANALYZED: {Pattern_Categories} | MODE: {analysis_mode} | VOLUME: {stream_volume} | VALUES: {numerical_values} | ANOMALIES: {anomaly_indicators} | INDEX: {Anomaly_Detection_Index:.1f} | RELIABILITY: {Detection_Reliability:.1f}% | CONSISTENCY: {Data_Consistency_Ratio:.3f} | SEVERITY: {Anomaly_Severity:.1f}% | CATEGORY: {Detection_Categories} | COMPLEXITY: {Analysis_Mode_Complexity} | SIG: {Analysis_Signature}"

main()
