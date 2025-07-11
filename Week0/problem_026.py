""" PROBLEM 26: Advanced Analytics Orchestrator
Task: Write a function called analytics_orchestrator that creates a comprehensive multi-dimensional analytics platform processing complex interconnected data streams.
Requirements:
Function name: analytics_orchestrator
result1 = analytics_orchestrator("TechCorp Solutions", "CloudCompute", 120, 25, 1000, 50, "US", 5, 150000)
result2 = analytics_orchestrator("DataFlow Systems", "Analytics", 90, 30, 500, 10, "EU", 8, 120000)
result3 = analytics_orchestrator("Global Networks", "Storage", 150, 20, 2000, 200, "AP", 4, 200500)   
Takes 9 parameters: client_name, service_type, usage_hours, data_volume_tb, transactions, error_count, region_code, priority_level, contract_value
Calculate usage_intensity: (usage_hours × data_volume_tb) ÷ 24
Calculate transaction_efficiency: (transactions - error_count) ÷ transactions × 100
Calculate error_ratio: (error_count ÷ transactions) × 1000
Calculate value_density: contract_value ÷ (usage_hours + data_volume_tb + transactions)
Calculate performance_matrix: (usage_intensity + transaction_efficiency + value_density) × priority_level
Calculate reliability_score: (100 - error_ratio) × (usage_hours ÷ 10) × priority_level
Create analytics_signature: first4_client + service_length + region_code + last3_contract_value
Calculate orchestration_index: (performance_matrix + reliability_score) ÷ (error_ratio + 1) × priority_level
Return formatted string: "ANALYTICS: CLIENT | SERVICE: S | INTENSITY: I.I | EFFICIENCY: E.E | MATRIX: M.M | SIGNATURE: SIG | INDEX: X.X"
Round intensity, efficiency, matrix, and index to 1 decimal place 
ANALYTICS: TECHCORP SOLUTIONS | SERVICE: CloudCompute | INTENSITY: 20.8 | EFFICIENCY: 95.0 | MATRIX: 1595.0 | SIGNATURE: TechCloudComputeUS000 | INDEX: 15950.0
ANALYTICS: DATAFLOW SYSTEMS | SERVICE: Analytics | INTENSITY: 18.8 | EFFICIENCY: 98.0 | MATRIX: 1372.0 | SIGNATURE: DataAnalyticsEU000 | INDEX: 27440.0
ANALYTICS: GLOBAL NETWORKS | SERVICE: Storage | INTENSITY: 31.3 | EFFICIENCY: 90.0 | MATRIX: 2034.0 | SIGNATURE: GlobStorageAP500 | INDEX: 20340.0 """

#defined main
def main():
    # created storing variables for calling function alongwith inputs for each profile
    result1 = analytics_orchestrator("TechCorp Solutions", "CloudCompute", 120, 25, 1000, 50, "US", 5, 150000)
    result2 = analytics_orchestrator("DataFlow Systems", "Analytics", 90, 30, 500, 10, "EU", 8, 120000)
    result3 = analytics_orchestrator("Global Networks", "Storage", 150, 20, 2000, 200, "AP", 4, 200500)
    # print items stored in storing variables 
    print(result1)
    print(result2)
    print(result3)
#defined calling function with temp storing variables 
def analytics_orchestrator(client_name, service_type, usage_hours, data_volume_tb, transactions, error_count, region_code, priority_level, contract_value):
    # all calculations 
    usage_intensity = (usage_hours * data_volume_tb) / 24
    transaction_efficiency = (transactions - error_count) / transactions * 100
    error_ratio = (error_count / transactions) * 1000
    value_density = contract_value / (usage_hours + data_volume_tb + transactions)
    performance_matrix = (usage_intensity + transaction_efficiency + value_density) * priority_level
    reliability_score = (100 - error_ratio) * (usage_hours / 10) * priority_level
    #Create analytics_signature = first4_client + service_length + region_code + str(last3_contract_value)
    first,last=client_name.split()
    first4_client=first[:4]
    service_length=len(service_type)
    contract_value_str=str(contract_value)
    last3_contract_value=contract_value_str[-3:]
    analytics_signature = first4_client + str(service_length) + region_code + str(last3_contract_value)
    # calculate orch index
    orchestration_index = (performance_matrix + reliability_score) / (error_ratio + 1) * priority_level
    # Caps name
    NAME=client_name.upper()

    # return f string
    return f"ANALYTICS: {NAME} | SERVICE: {service_type} | INTENSITY: {usage_intensity:0.1f} | EFFICIENCY: { transaction_efficiency:0.1f} | MATRIX: {performance_matrix:0.1f} | SIGNATURE: {analytics_signature} | INDEX:{orchestration_index:0.1f}"

# call main 
main()
