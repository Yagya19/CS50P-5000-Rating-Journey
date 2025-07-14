"""PROBLEM 35: Ultimate Computational Synthesizer
Task: Write a function called ultimate_synthesizer that creates the pinnacle of computational excellence, representing the absolute mastery of Week 0 concepts.
Requirements:
Function name: ultimate_synthesizer
result1 = ultimate_synthesizer("Quantum Nexus", 96, 128, 120, 98, 90, 80, 95)
result2 = ultimate_synthesizer("Neural Core", 80, 64, 90, 92, 85, 78, 88)
result3 = ultimate_synthesizer("Fusion Matrix", 100, 256, 150, 97, 95, 85, 92)
Takes 8 parameters: system_name, processing_power, memory_capacity, bandwidth_gbps, efficiency_rating, innovation_index, scalability_factor, reliability_score
Calculate computational_density: (processing_power × memory_capacity) ÷ (bandwidth_gbps × 1000)
Calculate performance_matrix: (efficiency_rating × innovation_index × scalability_factor) ÷ 100
Calculate system_throughput: (bandwidth_gbps × memory_capacity × reliability_score) ÷ processing_power
Calculate optimization_index: (computational_density + performance_matrix) × efficiency_rating ÷ 10
Calculate scalability_quotient: (scalability_factor × innovation_index) ÷ (100 - reliability_score + 1)
Calculate ultimate_metric: (system_throughput + optimization_index + scalability_quotient) × processing_power ÷ 1000
Create synthesis_signature: first7_system + power_tier + memory_class + bandwidth_grade + efficiency_level + innovation_rank
Calculate grandmaster_index: (ultimate_metric × performance_matrix × computational_density) ÷ (efficiency_rating + reliability_score)
Return formatted string: "ULTIMATE: SYSTEM | DENSITY: D.D | MATRIX: M.M | THROUGHPUT: T.T | OPTIMIZATION: O.O | SCALABILITY: S.S | METRIC: Me.Me | SIG: SIGNATURE | GRANDMASTER: G.G"
Round all decimal values to 1 decimal place
Classification Logic:
power_tier: "A" (≥90), "B" (70-89), "C" (50-69), "D" (<50)
memory_class: "X" (≥128), "Y" (64-127), "Z" (<64)
bandwidth_grade: "1" (≥100), "2" (50-99), "3" (<50)
efficiency_level: "α" (≥95), "β" (85-94), "γ" (<85)
innovation_rank: "★" (≥90), "◆" (75-89), "●" (<75)
Expected Output:
ULTIMATE: QUANTUM NEXUS | DENSITY: 9.6 | MATRIX: 72.0 | THROUGHPUT: 1152.0 | OPTIMIZATION: 817.6 | SCALABILITY: 180.0 | METRIC: 2149.6 | SIG: QUANTUMAY1α★ | GRANDMASTER: 1663.7
ULTIMATE: NEURAL CORE | DENSITY: 6.4 | MATRIX: 63.0 | THROUGHPUT: 864.0 | OPTIMIZATION: 693.4 | SCALABILITY: 162.0 | METRIC: 1719.4 | SIG: NEURALBZ2β◆ | GRANDMASTER: 1248.1
ULTIMATE: FUSION MATRIX | DENSITY: 12.8 | MATRIX: 81.0 | THROUGHPUT: 1440.0 | OPTIMIZATION: 938.8 | SCALABILITY: 202.5 | METRIC: 2581.3 | SIG: FUSIONAX1α★ | GRANDMASTER: 2113.5 """

# define main
def main():
    # set stroing variabels for calling func with its input from each profile
    result1 = ultimate_synthesizer("Quantum Nexus", 96, 128, 120, 98, 90, 80, 95)
    result2 = ultimate_synthesizer("Neural Core", 80, 64, 90, 92, 85, 78, 88)
    result3 = ultimate_synthesizer("Fusion Matrix", 100, 256, 150, 97, 95, 85, 92)
    # print item in storing variable
    print(result1)
    print(result2)
    print(result3)
# define calling func with parameters
def ultimate_synthesizer(system_name, processing_power, memory_capacity, bandwidth_gbps, efficiency_rating, innovation_index, scalability_factor, reliability_score):
    # d all imp calculations
    computational_density = (processing_power * memory_capacity) / (bandwidth_gbps * 1000)
    performance_matrix = (efficiency_rating * innovation_index * scalability_factor) / 100
    system_throughput = (bandwidth_gbps * memory_capacity * reliability_score) / processing_power
    optimization_index = (computational_density + performance_matrix) * efficiency_rating / 10
    scalability_quotient = (scalability_factor * innovation_index) / (100 - reliability_score + 1)
    ultimate_metric = (system_throughput + optimization_index + scalability_quotient) * processing_power / 1000
    # get sig and index basics
    first,last=system_name.split()
    first7_system=first[:7]
    # do classification logic
    power_tier = "A"* (processing_power>=90) + "B"* (70<processing_power<89) + "C"* (50<processing_power<69) + "D"* (processing_power<50)
    memory_class = "X" * (memory_capacity>=128) + "Y"*(64<processing_power<127) + "Z"*(processing_power<64)
    bandwidth_grade = "1"* (bandwidth_gbps>=100) + "2"* (50<bandwidth_gbps<99) + "3"* (bandwidth_gbps<50)
    efficiency_level= "α" * (efficiency_rating>=95) + "β" * (85<efficiency_rating<94) + "γ"* (efficiency_rating<85)
    innovation_rank = "★" * (innovation_index>=90)+ "◆"* (75<innovation_index<89)+"●"*(innovation_index<75)
    # final values of sig and index
    synthesis_signature = first7_system + power_tier + memory_class + bandwidth_grade + efficiency_level + innovation_rank
    grandmaster_index = (ultimate_metric * performance_matrix * computational_density) / (efficiency_rating + reliability_score)

    #return f string 
    return f"ULTIMATE: {system_name.upper()} | DENSITY: {computational_density:0.1f} | MATRIX: {performance_matrix:0.1f} | THROUGHPUT: {system_throughput:0.1f} | OPTIMIZATION: {optimization_index:0.1f} | SCALABILITY: {scalability_quotient:0.1f} | METRIC: {ultimate_metric:0.2f} | SIG: {synthesis_signature.upper()} | GRANDMASTER: {grandmaster_index :0.1f}"

# call main 
main()
