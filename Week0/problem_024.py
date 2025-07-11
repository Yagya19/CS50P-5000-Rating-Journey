"""
PROBLEM 24: Advanced Data Intelligence System
Task: Write a function called intelligence_system that creates a comprehensive data intelligence platform analyzing multiple interconnected metrics.
Requirements:
Function name: intelligence_system
result1 = intelligence_system("Alice Johnson", 20, 10, 20, 5, "USA", 5)
result2 = intelligence_system("Bob Smith", 15, 5, 15, 2, "Canada", 8)
result3 = intelligence_system("Carol Davis", 30, 20, 20, 5, "UK", 10)
Takes 7 parameters: user_name, login_count, data_size_gb, processing_time, error_rate, region, tier_level
Calculate efficiency_score: (data_size_gb × 1000) ÷ processing_time
Calculate reliability_index: (100 - error_rate) × login_count ÷ 100
Calculate performance_rating: (efficiency_score + reliability_index) × tier_level
Calculate data_throughput: data_size_gb × login_count × (100 - error_rate)
Create system_signature: first2_user + region_length + tier_level + last2_processing_time
Calculate intelligence_quotient: (performance_rating + data_throughput) ÷ (error_rate + 1)
Return formatted string: "SYSTEM: USER | EFF: X.X | REL: Y.Y | PERF: Z.Z | THRU: W | SIG: S | IQ: Q.Q"
Round efficiency, reliability, performance, and IQ to 1 decimal place 
---------------------------------------------------------------------------
SYSTEM: ALICE JOHNSON | EFF: 500.0 | REL: 190.0 | PERF: 3450.0 | THRU: 9500 | SIG: Al8515 | SIG: AliceJ85150 | IQ: 2164.7
SYSTEM: BOB SMITH | EFF: 333.3 | REL: 147.0 | PERF: 2403.3 | THRU: 4900 | SIG: Bo8212 | IQ: 916.4
SYSTEM: CAROL DAVIS | EFF: 1000.0 | REL: 285.0 | PERF: 9630.0 | THRU: 22800 | SIG: Ca10320 | IQ: 4076.3 """

#defined main 
def main():
    # create 3 storing variable for calling funct. with 7 inputs related to each profile
    profile1 = intelligence_system("Alice Johnson", 20, 10, 20, 5, "USA", 5)
    profile2 = intelligence_system("Bob Smith", 15, 5, 15, 2, "Canada", 8)
    profile3 = intelligence_system("Carol Davis", 30, 20, 20, 5, "UK", 10)
    # print the stored item ie returned value by calling funct
    print(profile1)
    print(profile2)
    print(profile3)

# def calling funct and assinging temp variables to store inputs of each profile
def intelligence_system(user_name, login_count, data_size_gb, processing_time, error_rate, region, tier_level):
    # imp formulas to calculate
    efficiency_score=(data_size_gb * 1000) / processing_time
    reliability_index = (100 - error_rate) * login_count / 100
    performance_rating = (efficiency_score + reliability_index) * tier_level
    data_throughput = data_size_gb * login_count * (100 - error_rate)
    # create system_signature:
    first,last=user_name.split()
    first2_user = first[:2]
    region_length=len(region)
    system_signature = first2_user + str(region_length) + str(tier_level) + str(processing_time)
    intelligence_quotient = (performance_rating + data_throughput) / (error_rate + 1)
    # name in caps
    NAME=user_name.upper()
    # return the f string 
    return f"SYSTEM: {NAME} | EFF: {efficiency_score:0.1f} | REL: {reliability_index:0.1f} | PERF: {performance_rating:0.1f} | THRU: {data_throughput:0.1f} | SIG: {system_signature} | IQ: {intelligence_quotient:0.1f}"

main()


