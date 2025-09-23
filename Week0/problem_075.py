#PROBLEM 75 - TRAFFIC SIMULATION ENGINE (COMPLETE CHALLENGE FORMAT)
def main():
    result1 = traffic_simulator("highway", "cars200→trucks50↑buses25", 2, 3, 1)
    result2 = traffic_simulator("urban", "vehicles150↓bikes30→taxis", 1, 2, 2)
    result3 = traffic_simulator("rural", "cars75→farm20↑delivery", 3, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def traffic_simulator(road_type, traffic_data, congestion_level, simulation_hours, precision_level):
    #Step 1: Count Traffic Elements

    #route_length: Count total characters in traffic_data
    route_length = len(traffic_data)
    #vehicle_count: Count digit characters (0-9) in traffic_data
    vehicle_count = traffic_data.count("0") + traffic_data.count("1") + traffic_data.count("2") + traffic_data.count("3") +  traffic_data.count("4") + traffic_data.count("5") + traffic_data.count("6") + traffic_data.count("7") + +  traffic_data.count("8") + traffic_data.count("9") 
    #flow_indicators: Count traffic flow characters ("→", "↑", "↓") in traffic_data
    flow_indicators = traffic_data.count("→") + traffic_data.count("↑") + traffic_data.count("↓") 


    Traffic_Complexity_Score = (route_length * 8) + (vehicle_count * 16) + (flow_indicators * 25)
    Road_Multiplier = 3.2*(road_type=="highway") + 2.7*(road_type=="urban") + 2.3*(road_type=="rural")
    Flow_Projection = Traffic_Complexity_Score * Road_Multiplier  * simulation_hours
    Raw_Traffic_Efficiency_Index = Flow_Projection - (congestion_level * 100)
    Traffic_Efficiency_Index = Raw_Traffic_Efficiency_Index *(Raw_Traffic_Efficiency_Index >=200) + 200*(Raw_Traffic_Efficiency_Index<200)
    Vehicle_Density_Ratio = vehicle_count / (route_length+(route_length==0)) * (route_length!=0) + 0.9*(route_length==0)
    Flow_Prediction_Accuracy = (Vehicle_Density_Ratio * 100) + (simulation_hours * 50)
    Road_Type_Complexity = 7*(road_type=="highway") + 9*(road_type=="urban") + 5*(road_type=="rural")
    Efficiency_Categories = "Congested_Flow"*(Traffic_Efficiency_Index <350)+"Optimal_Flow"*(350<=Traffic_Efficiency_Index<500)+"Optimal_Flow"*(Traffic_Efficiency_Index >=500)
    Simulation_Categories = "Extended_Traffic_Simulation"*(simulation_hours == 3) + "Standard_Traffic_Simulation"*(simulation_hours == 2) + "Brief_Traffic_Simulation"*(simulation_hours == 1) 
    Traffic_Reliability = (flow_indicators*90)/ (vehicle_count+(vehicle_count==0)) * (vehicle_count!=0) + 110*(vehicle_count==0)
    Traffic_Signature = road_type + str(simulation_hours) + str(congestion_level) +  Efficiency_Categories 

    return f"SIMULATED: {Simulation_Categories} | TYPE: {road_type} | ROUTE: {route_length} | VEHICLES: {vehicle_count} | FLOWS: {flow_indicators} | INDEX: {Traffic_Efficiency_Index:.1f} | ACCURACY: { Flow_Prediction_Accuracy :.1f}% | DENSITY: {Vehicle_Density_Ratio :.3f} | RELIABILITY: {Traffic_Reliability :.1f}% | CATEGORY: { Efficiency_Categories} | COMPLEXITY: {Road_Type_Complexity} | SIG: {Traffic_Signature}"

main()
