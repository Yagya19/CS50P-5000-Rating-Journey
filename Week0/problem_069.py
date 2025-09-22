# PROBLEM 69 - OPTIMIZATION CALCULATOR ENGINE (COMPLETE CHALLENGE FORMAT)Difficulty: Optimization Analysis Challenge
def main():
    result1 = optimization_calculator("time", "process=120+steps/45", 2, 3, 1)
    result2 = optimization_calculator("cost", "budget=5000/items=250", 1, 2, 2)
    result3 = optimization_calculator("resource", "cpu=75+memory=512", 3, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)


def optimization_calculator(optimization_type, resource_data, efficiency_target, optimization_level, precision_level): 
    #Step 1: Count Resource Elements

    #resource_length: Count total characters in resource_data
    resource_length = len(resource_data)

    #value_indicators: Count digit characters (0-9) in resource_data
    value_indicators =  resource_data.count("0") + resource_data.count("1") + resource_data.count("2") +  resource_data.count("3") + resource_data.count("4") + resource_data.count("5") + + resource_data.count("6") + resource_data.count("7") +  resource_data.count("8") + resource_data.count("9") 
    
    #separator_markers: Count separator characters ("=", "+", "/") in resource_data
    separator_markers = resource_data.count("=") + resource_data.count("+") + resource_data.count("/") 
    Resource_Complexity_Score =(resource_length * 2.5) + (value_indicators * 4) + (separator_markers * 8)
    Optimization_Multiplier = 1.9*(optimization_type=="Time") + 1.5*(optimization_type=="Cost") + 1.7*(optimization_type=="Resource")
    Optimization_Rating = Resource_Complexity_Score * Optimization_Multiplier * optimization_level
    Raw_Efficiency_Index =  Optimization_Rating  - (efficiency_target * 45)
    Efficiency_Index = Raw_Efficiency_Index*(Raw_Efficiency_Index>=90) + 90*(Raw_Efficiency_Index<90)
    Resource_Utilization_Ratio = value_indicators / (resource_length + (resource_length==0)) * (resource_length!=0) + 0.35*((resource_length==0))
    Optimization_Accuracy = (Resource_Utilization_Ratio * 100) + (optimization_level * 22)
    Optimization_Type_Complexity = 8*(optimization_type=="Time") + 6*(optimization_type=="Cost") + 7*(optimization_type=="Resource")
    Efficiency_Categories = "Low_Efficient" * (Efficiency_Index < 150)+ "Moderately_Efficient"*(150<=Efficiency_Index <220) + "Highly_Efficient"*(Efficiency_Index >= 220)
    Optimization_Categories = "Advanced_Optimization" * ( optimization_level==3) + "Standard_Optimization"*( optimization_level==2) + "Basic_Optimization" * ( optimization_level==1)
    Resource_Effectiveness = (separator_markers*35 / (value_indicators+(value_indicators==0))) * (value_indicators!=0) + 60*(value_indicators==0)
    Optimization_Signature = optimization_type + str(optimization_level) + str(efficiency_target) + Efficiency_Categories

    return f"OPTIMIZED: {Optimization_Categories} | TYPE: {optimization_type} | LENGTH: {resource_length} | VALUES: {value_indicators} | SEPARATORS: {separator_markers} | INDEX: {Efficiency_Index:.1f} | ACCURACY: {Optimization_Accuracy:.1f}% | RATIO: {Resource_Utilization_Ratio :.3f} | EFFECTIVENESS: {Resource_Effectiveness:.1f}% | CATEGORY: {Efficiency_Categories} | COMPLEXITY: {Optimization_Type_Complexity } | SIG: {Optimization_Signature }"

main()

