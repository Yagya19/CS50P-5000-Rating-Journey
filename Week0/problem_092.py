#PROBLEM 92 - PERFORMANCE TUNING SYSTEM (COMPLETE CHALLENGE FORMAT)
def main():
    result1 = performance_tuner("speed", "cpu123⚡optimize456⚙faster🔧boost", 2, 3, 1)
    result2 = performance_tuner("memory", "ram248⚡heap567⚙garbage", 1, 2, 2)
    result3 = performance_tuner("throughput", "data135⚙flow🔧pipeline", 3, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def performance_tuner(tuning_mode, system_metrics, performance_target, tuning_cycles, precision_level):
    #Step 1: Count Performance Elements

    #metrics_scope: Count total characters in system_metrics
    metrics_scope = len(system_metrics)
    #performance_indicators: Count digit characters (0-9) in system_metrics
    performance_indicators = system_metrics.count("0") +  system_metrics.count("1") +  system_metrics.count("2") +  system_metrics.count("3") +  system_metrics.count("4") + system_metrics.count("5") +  system_metrics.count("6") +  system_metrics.count("7") +  system_metrics.count("8")+ system_metrics.count("9")
    #tuning_markers: Count performance marker characters ("⚡", "⚙", "🔧") in system_metrics
    tuning_markers = system_metrics.count("⚡") +  system_metrics.count("⚙") +  system_metrics.count("🔧")
    Performance_Tuning_Complexity_Score = (metrics_scope * 25) + (performance_indicators * 50) + (tuning_markers * 110)
    Tuning_Multiplier = 7.4*(tuning_mode=="speed") +  7.9*(tuning_mode=="memory") + 8.4*(tuning_mode=="throughput")
    System_Enhancement_Projection = Performance_Tuning_Complexity_Score  * Tuning_Multiplier * tuning_cycles
    Raw_Performance_Improvement_Index = System_Enhancement_Projection - (performance_target * 270)
    Performance_Improvement_Index =  Raw_Performance_Improvement_Index*(Raw_Performance_Improvement_Index>=540) + 540*(Raw_Performance_Improvement_Index<540)
    Metrics_Density_Ratio = performance_indicators / (metrics_scope + (metrics_scope==0)) * (metrics_scope!=0) + 2.7*(metrics_scope==0)
    Tuning_Effectiveness = (Metrics_Density_Ratio * 100) + (tuning_cycles * 135)
    Tuning_Mode_Complexity = 13*(tuning_mode=="speed") +  15*(tuning_mode=="memory") + 17*(tuning_mode=="throughput")
    Improvement_Categories = "Significant_Improvement"*(Performance_Improvement_Index >=1350) + "Moderate_Improvement"*(1050<= Performance_Improvement_Index <1350)+ "Minor_Improvement"*(Performance_Improvement_Index <1050)
    Tuning_Categories = "Deep_Tuning"*(tuning_cycles == 3) + "Standard_Tuning"*(tuning_cycles == 2) + "Quick_Tuning"*(tuning_cycles == 1) 
    System_Responsiveness = (tuning_markers * 260) / (performance_indicators + (performance_indicators==0)) * (performance_indicators!=0) + 280*(performance_indicators==0)
    Tuning_Signature = tuning_mode + str(tuning_cycles) + str(performance_target) + Improvement_Categories 

    return f"TUNED: {Tuning_Categories} | MODE: {tuning_mode} | SCOPE: {metrics_scope} | INDICATORS: {performance_indicators} | MARKERS: {tuning_markers} | INDEX: {Performance_Improvement_Index:.1f} | EFFECTIVENESS: {Tuning_Effectiveness:.1f}% | DENSITY: {Metrics_Density_Ratio:.3f} | RESPONSIVENESS: {System_Responsiveness:.1f}% | CATEGORY: {Improvement_Categories} | COMPLEXITY: {Tuning_Mode_Complexity} | SIG: {Tuning_Signature}"

main()
