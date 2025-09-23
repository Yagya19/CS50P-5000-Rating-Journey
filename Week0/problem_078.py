#PROBLEM 78 - NETWORK SIMULATION ENGINE (COMPLETE CHALLENGE FORMAT)
def main():
    result1 = network_simulator("fiber", "cable1000→router500⟷switch", 2, 3, 1)
    result2 = network_simulator("wireless", "ap300↔device150→gateway", 1, 2, 2)
    result3 = network_simulator("ethernet", "hub200⟷pc100→server", 3, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def network_simulator(network_type, topology_data, latency_factor, transmission_cycles, precision_level):

    #Step 1: Count Network Elements
    #network_size: Count total characters in topology_data
    network_size = len(topology_data)
    #data_packets: Count digit characters (0-9) in topology_data
    data_packets = topology_data.count("0")+ topology_data.count("1")+ topology_data.count("2")+ topology_data.count("3")+ topology_data.count("4")+topology_data.count("5")+ topology_data.count("6")+ topology_data.count("7")+ topology_data.count("8")+ topology_data.count("9")
    #connection_points: Count network connector characters ("→", "↔", "⟷") in topology_data
    connection_points = topology_data.count("→")+ topology_data.count("↔")+ topology_data.count("⟷")
    Network_Complexity_Score = (network_size * 11) + (data_packets * 22) + (connection_points * 40)
    Network_Multiplier= 4.2*(network_type=="fiber") + 3.6*(network_type=="wireless") + 3.1*(network_type=="ethernet") 
    Transmission_Projection = Network_Complexity_Score * Network_Multiplier * transmission_cycles
    Raw_Network_Performance_Index = Transmission_Projection  - (latency_factor * 130)
    Network_Performance_Index = Raw_Network_Performance_Index *(Raw_Network_Performance_Index >=260) + 260*(Raw_Network_Performance_Index <260)
    Bandwidth_Utilization_Ratio = data_packets / (network_size + (network_size==0)) * (network_size!=0) + 1.2*(network_size==0)
    Connection_Reliability= (Bandwidth_Utilization_Ratio * 100) + (transmission_cycles * 65)
    Network_Type_Complexity = 8*(network_type=="fiber") + 10*(network_type=="wireless") + 7*(network_type=="ethernet") 
    Performance_Categories = "Poor_Performance"*(Network_Performance_Index<460) + "Standard_Performance"*(460<=Network_Performance_Index<650) + "Optimal_Performance"*(Network_Performance_Index>=650)
    Transmission_Categories = "Low_Volume_Transmission"*(transmission_cycles == 1) + "Medium_Volume_Transmission"*(transmission_cycles == 2)+"High_Volume_Transmission"*(transmission_cycles == 3)
    Network_Throughput = (connection_points *120) / (data_packets+(data_packets==0)) * (data_packets!=0) + 140*(data_packets==0)
    Network_Signature = network_type + str(transmission_cycles) + str(latency_factor) + Performance_Categories 

    return f"TRANSMITTED: {Transmission_Categories} | TYPE: {network_type} | SIZE: {network_size} | PACKETS: {data_packets} | CONNECTIONS: {connection_points} | INDEX: { Network_Performance_Index:.1f} | RELIABILITY: { Connection_Reliability:.1f}% | UTILIZATION: {Bandwidth_Utilization_Ratio:.3f} | THROUGHPUT: {Network_Throughput:.1f}% | CATEGORY: {Performance_Categories} | COMPLEXITY: {Network_Type_Complexity} | SIG: {Network_Signature}"

main()
