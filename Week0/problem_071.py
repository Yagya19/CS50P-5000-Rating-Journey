# PROBLEM 71 - POPULATION SIMULATION ENGINE (COMPLETE CHALLENGE FORMAT)
def main():
    result1 = population_simulator("exponential", "pop1000+growth*rate^2", 2, 3, 1)
    result2 = population_simulator("linear", "base500+increase*factor", 1, 2, 2)
    result3 = population_simulator("logistic", "start200^limit*capacity", 3, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def population_simulator(simulation_type, population_data, growth_factor, simulation_cycles, precision_level):

    #Step 1: Count Population Elements
    #data_size: Count total characters in population_data
    data_size = len(population_data)

    #numeric_population: Count digit characters (0-9) in population_data
    numeric_population = population_data.count("0")+ population_data.count("1")+ population_data.count("2")+population_data.count("3")+ population_data.count("4")+ population_data.count("5")+population_data.count("6")+ population_data.count("7")+population_data.count("8")+ population_data.count("9")
    #growth_indicators: Count growth marker characters ("+", "*", "^") in population_data
    growth_indicators = population_data.count("+")+ population_data.count("*")+ population_data.count("^")

    # Maths Formulas
    Population_Base_Score = (data_size * 4.5) + (numeric_population * 8) + (growth_indicators * 12)
    Simulation_Multiplier = 2.3*(simulation_type=="exponential") + 1.9*(simulation_type=="linear") + 2.1*(simulation_type=="logistic")
    Growth_Projection = Population_Base_Score * Simulation_Multiplier*simulation_cycles
    Raw_Population_Stability_Index = Growth_Projection  - (growth_factor * 60)
    Population_Stability_Index = Raw_Population_Stability_Index*(Raw_Population_Stability_Index>120) + 120*(Raw_Population_Stability_Index<120)
    Demographic_Density_Ratio = numeric_population / (data_size + (data_size ==0))*(data_size !=0) + 0.5*(data_size ==0)
    Simulation_Accuracy = (Demographic_Density_Ratio * 100) + (simulation_cycles * 30)
    Simulation_Type_Complexity =  9*(simulation_type=="exponential") + 6*(simulation_type=="linear") + 8*(simulation_type=="logistic")
    Stability_Categories = "Unstable"*(Population_Stability_Index < 200)+"Stable"*(200<=Population_Stability_Index < 300)+"Unstable"*(Population_Stability_Index<=300)
    Simulation_Categories = "Long_Term_Simulation" * (simulation_cycles == 3) + " Medium_Term_Simulation" * (simulation_cycles == 2) + "Short_Term_Simulation" * (simulation_cycles == 1) 
    Raw_Population_Efficiency = (growth_indicators / numeric_population) * 50
    Population_Efficiency =  Raw_Population_Efficiency*(numeric_population!=0) + 75*(numeric_population==0)
    Simulation_Signature = simulation_type + str(simulation_cycles) + str(growth_factor) + Stability_Categories 

    return f"SIMULATED: {Simulation_Categories} | TYPE: {simulation_type} | SIZE: {data_size} | POPULATION: {numeric_population} | GROWTH: {growth_indicators} | INDEX: {Population_Stability_Index :.1f} | ACCURACY: {Simulation_Accuracy:.1f}% | DENSITY: {Demographic_Density_Ratio :.3f} | EFFICIENCY: {Population_Efficiency:.1f}% | CATEGORY: {Stability_Categories} | COMPLEXITY: {Simulation_Type_Complexity} | SIG: {Simulation_Signature}"

main()
