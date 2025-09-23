#PROBLEM 76 - ENERGY SYSTEM SIMULATION ENGINE (COMPLETE CHALLENGE FORMAT)
def main():
    result1 = energy_simulator("solar", "panels500⚡grid250⇒homes", 2, 3, 1)
    result2 = energy_simulator("nuclear", "reactor1000⇔turbine400⚡", 1, 2, 2)
    result3 = energy_simulator("wind", "turbines300⇒grid150⚡city", 3, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def energy_simulator(energy_type, grid_data, demand_variance, optimization_cycles, precision_level):

    #Step 1: Count Energy Elements

    #grid_capacity: Count total characters in grid_data
    grid_capacity = len(grid_data)
    #power_units: Count digit characters (0-9) in grid_data
    power_units = grid_data.count("0")+grid_data.count("1")+grid_data.count("2")+grid_data.count("3")+grid_data.count("4")+grid_data.count("5")+grid_data.count("6")+grid_data.count("7")+grid_data.count("8")+grid_data.count("9")
    #distribution_nodes: Count distribution marker characters ("⚡", "⇒", "⇔") in grid_data
    distribution_nodes = grid_data.count("⚡")+grid_data.count("⇒")+grid_data.count("⇔")

    #MATHEMATICAL FORMULAS (COMPLETE):
    Energy_Complexity_Score = (grid_capacity * 9) + (power_units * 18) + (distribution_nodes * 30)
    Energy_Multiplier =  3.5*(energy_type=="solar")+ 3.0*(energy_type=="nuclear")+ 2.6*(energy_type=="wind")
    Power_Projection = Energy_Complexity_Score *  Energy_Multiplier * optimization_cycles
    Raw_Grid_Stability_Index = Power_Projection - (demand_variance * 110)
    Grid_Stability_Index = Raw_Grid_Stability_Index*(Raw_Grid_Stability_Index>=220) + 220*(Raw_Grid_Stability_Index<220)
    Energy_Efficiency_Ratio = power_units / (grid_capacity + (grid_capacity==0) ) * (grid_capacity !=0) + 1*(grid_capacity==0)
    System_Reliability = (Energy_Efficiency_Ratio  * 100) + (optimization_cycles * 55)
    Energy_Type_Complexity =  6*(energy_type=="solar")+ 10*(energy_type=="nuclear")+ 8*(energy_type=="wind")
    Stability_Categories = "Unstable_Grid"*(Grid_Stability_Index<380)+"Moderately_Stable"*(380<=Grid_Stability_Index<550) +"Highly_Stable"*(Grid_Stability_Index>=550)
    Optimization_Categories = "Advanced_Optimization"*(optimization_cycles == 3)+"Standard_Optimization"*(optimization_cycles == 2)+"Basic_Optimization"*(optimization_cycles == 1)
    Power_Distribution_Efficiency = (distribution_nodes*100) / (power_units+( power_units==0)) * (power_units!=0) + 120*( power_units==0)
    Energy_Signature = energy_type + str(optimization_cycles) + str(demand_variance) + Stability_Categories 

    return f"OPTIMIZED: {Optimization_Categories} | TYPE: {energy_type} | CAPACITY: {grid_capacity} | POWER: {power_units} | NODES: {distribution_nodes} | INDEX: {Grid_Stability_Index:.1f} | RELIABILITY: {System_Reliability :.1f}% | EFFICIENCY: {Energy_Efficiency_Ratio:.3f} | DISTRIBUTION: {Power_Distribution_Efficiency :.1f}% | CATEGORY: {Stability_Categories} | COMPLEXITY: {Energy_Type_Complexity} | SIG: {Energy_Signature}"

main()
