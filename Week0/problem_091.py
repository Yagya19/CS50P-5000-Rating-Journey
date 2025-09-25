#PROBLEM 91 - RESOURCE OPTIMIZATION ENGINE (COMPLETE CHALLENGE FORMAT)
def main():
    result1 = resource_optimizer("cost", "budget123▲reduce456▼optimize◄efficient", 2, 3, 1)
    result2 = resource_optimizer("time", "schedule248▲speed567▼deadline", 1, 2, 2)
    result3 = resource_optimizer("quality", "improve135▼enhance◄standard", 3, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def resource_optimizer(optimization_target, resource_data, efficiency_goal, optimization_rounds, precision_level):
    #Step 1: Count Resource Elements

    #resource_pool: Count total characters in resource_data
    resource_pool = len(resource_data)
    #allocation_units: Count digit characters (0-9) in resource_data
    allocation_units = resource_data.count("0")+resource_data.count("1")+resource_data.count("2")+resource_data.count("3")+resource_data.count("4")+resource_data.count("5")+resource_data.count("6")+ resource_data.count("7")+resource_data.count("8")+resource_data.count("9")
    #optimization_flags: Count optimization indicator characters ("▲", "▼", "◄") in resource_data
    optimization_flags = resource_data.count("▲")+resource_data.count("▼")+resource_data.count("◄")

    Resource_Optimization_Complexity_Score = (resource_pool * 24) + (allocation_units * 48) + (optimization_flags * 105)
    Optimization_Multiplier = 8.1*(optimization_target=="cost") + 7.6*(optimization_target=="time") + 7.1*(optimization_target=="quality")
    Efficiency_Enhancement_Projection =  Resource_Optimization_Complexity_Score  * Optimization_Multiplier  * optimization_rounds
    Raw_Optimization_Success_Index = Efficiency_Enhancement_Projection - (efficiency_goal * 260)
    Optimization_Success_Index = Raw_Optimization_Success_Index*(Raw_Optimization_Success_Index>=520) + 520*(Raw_Optimization_Success_Index<520)
    Resource_Utilization_Ratio = allocation_units / (resource_pool + (resource_pool==0)) * (resource_pool!=0) +2.6*(resource_pool==0))
    Optimization_Efficiency = (Resource_Utilization_Ratio * 100) + (optimization_rounds * 130)
    Optimization_Target_Complexity = 12*(optimization_target=="cost") + 14*(optimization_target=="time") + 16*(optimization_target=="quality")
    Success_Categories = "Optimal_Performance"*(Optimization_Success_Index >=1300) + "Improved_Performance"*(1000<=Optimization_Success_Index <1300) +  "Baseline_Performance"*(Optimization_Success_Index<1000)  
    Optimization_Categories = "Intensive_Optimization"*(optimization_rounds == 3) + "Standard_Optimization"*(optimization_rounds == 2) + "Basic_Optimization"*(optimization_rounds == 1) 
    Resource_Efficiency=(optimization_flags*250) / (allocation_units+(allocation_units==0)) *(allocation_units!=0) + 270*(allocation_units==0)
    Optimization_Signature = optimization_target + str(optimization_rounds) + str(efficiency_goal) + Success_Categories 

    return f"OPTIMIZED: {Optimization_Categories} | TARGET: {optimization_target} | POOL: {resource_pool} | UNITS: {allocation_units} | FLAGS: {optimization_flags} | INDEX: {Optimization_Success_Index:.1f} | EFFICIENCY: {Optimization_Efficiency:.1f}% | UTILIZATION: {Resource_Utilization_Ratio:.3f} | RESOURCE_EFF: {Resource_Efficiency:.1f}% | CATEGORY: {Success_Categories} | COMPLEXITY: {Optimization_Target_Complexity} | SIG: {Optimization_Signature}"

main()
