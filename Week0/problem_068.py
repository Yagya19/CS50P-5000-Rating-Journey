#PROBLEM 68 - PERFORMANCE ANALYZER ENGINE (COMPLETE CHALLENGE FORMAT)

def main():
    result1 = performance_analyzer("speed", "rate-98.5,time-12.3", 2, 2, 1)
    result2 = performance_analyzer("accuracy", "score-85.7,error-0.02", 3, 3, 2)
    result3 = performance_analyzer("efficiency", "cpu-45.2,mem-67.8", 1, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def performance_analyzer(metric_type, performance_data, benchmark_level, analysis_depth, precision_level):
    #Step 1: Count Performance Elements

    #data_points: Count total characters in performance_data
    data_points=len(performance_data)

    #numeric_values: Count digit characters (0-9) in performance_data
    numeric_values = performance_data.count("0") + performance_data.count("1") + performance_data.count("2") + performance_data.count("3") + performance_data.count("4") + performance_data.count("5") + performance_data.count("6") + performance_data.count("7") + performance_data.count("8") + performance_data.count("9")
    
    #delimiter_count: Count delimiter characters (",", ".", "-") in performance_data
    delimiter_count = performance_data.count(",") + performance_data.count(".") + performance_data.count("-") 
    Performance_Base_Score =(data_points * 4) + (numeric_values * 6) + (delimiter_count * 2)
    Performance_Multiplier = 1.8*(metric_type=="speed") + 1.4*(metric_type=="accuracy")+ 1.6*(metric_type=="efficiency")
    Metric_Rating = Performance_Base_Score * Performance_Multiplier * analysis_depth
    Raw_Performance_Index = Metric_Rating - (benchmark_level * 35) 
    Performance_Index = Raw_Performance_Index * ( Raw_Performance_Index>=70) + 70*(Raw_Performance_Index<70)
    Data_Completeness_Ratio = (numeric_values / data_points)*(data_points != 0) + 0.4*(data_points == 0)
    Analysis_Precision = (Data_Completeness_Ratio * 100) + (analysis_depth * 15)
    Metric_Type_Complexity = 5*(metric_type=="speed") + 7*(metric_type=="accuracy")+ 6*(metric_type=="efficiency")
    Performance_Categories = "Suboptimal"*(Performance_Index <110)+ "Satisfactory"*(110<=Performance_Index<180) +"optimal"*(Performance_Index>=180)
    Analysis_Categories = "Comprehensive_Analysis"*(analysis_depth == 3) + "Detailed_Analysis"*(analysis_depth == 2) + " Basic_Analysis"*(analysis_depth == 1)
    Metric_Stability = (delimiter_count*25) / (numeric_values+(numeric_values==0))*(numeric_values!=0) + 50*(numeric_values==0)
    Performance_Signature = metric_type + str(analysis_depth) + str(benchmark_level) + Performance_Categories

    # return the f string to called functions
    return f"ANALYZED: {Analysis_Categories} | TYPE: {metric_type} | POINTS: {data_points} | NUMERIC: {numeric_values} | DELIMITERS: {delimiter_count} | INDEX: {Performance_Index:.1f} | PRECISION: {Analysis_Precision :.1f}% | RATIO: {Data_Completeness_Ratio:.3f} | STABILITY: {Metric_Stability:.1f}% | CATEGORY: {Performance_Categories} | COMPLEXITY: {Metric_Type_Complexity} | SIG: {Performance_Signature }"

main()
