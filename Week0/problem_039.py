"""PROBLEM 39: Supreme Reality Engineering Matrix
Task: Write a function called reality_matrix that creates the ultimate reality engineering system capable of manipulating and designing multidimensional existence across infinite possibility spaces.
Requirements:
Function name: reality_matrix
result1 = reality_matrix("Infinite Cosmos", 30, 125, 80, 96, 90, 180, 220, 99, 85, 95, 108, 75, 99, 99)
result2 = reality_matrix("Quantum Nexus", 20, 75, 60, 85, 72, 120, 140, 92, 70, 80, 72, 50, 90, 96)
result3 = reality_matrix("Transcendent Void", 60, 200, 100, 98, 95, 300, 400, 99, 95, 99, 180, 120, 99, 99)
Takes 15 parameters: reality_name, dimension_count, timeline_branches, probability_vectors, causality_strength, entropy_resistance, information_flow, consciousness_nodes, reality_stability, temporal_coherence, spatial_integrity, quantum_entanglement, field_density, emergence_factor, transcendence_coefficient
Calculate dimensional_architecture: (dimension_count × timeline_branches × probability_vectors) ÷ (causality_strength + entropy_resistance)
Calculate information_dynamics: (information_flow × consciousness_nodes × reality_stability) ÷ 100
Calculate temporal_matrix: (temporal_coherence × spatial_integrity × quantum_entanglement) ÷ field_density
Calculate emergence_quotient: (emergence_factor × transcendence_coefficient × dimensional_architecture) ÷ 1000
Calculate reality_synthesis: (information_dynamics + temporal_matrix + emergence_quotient) × dimension_count ÷ 100
Calculate consciousness_integration: (consciousness_nodes × transcendence_coefficient × reality_stability) ÷ (timeline_branches + 1)
Calculate quantum_coherence: (quantum_entanglement × field_density × emergence_factor) ÷ (entropy_resistance + 1)
Calculate multidimensional_mastery: (reality_synthesis × consciousness_integration × quantum_coherence) ÷ 10000
Create supreme_signature: first15_reality + dimension_tier + timeline_class + probability_grade + causality_level + entropy_rank + consciousness_scale + reality_category + transcendence_supreme
Calculate ultimate_reality_index: (multidimensional_mastery + dimensional_architecture + information_dynamics + temporal_matrix) × transcendence_coefficient ÷ 1000
Return formatted string: "REALITY: NAME | ARCHITECTURE: A.A | DYNAMICS: D.D | TEMPORAL: T.T | EMERGENCE: E.E | SYNTHESIS: S.S | CONSCIOUSNESS: C.C | QUANTUM: Q.Q | MASTERY: M.M | SIG: SIGNATURE | ULTIMATE: U.U"
Round all decimal values to 1 decimal place
Classification Logic:
dimension_tier: "∞" (≥50), "Ω" (30-49), "Φ" (20-29), "Ψ" (10-19), "Δ" (<10)
timeline_class: "⟡" (≥100), "⟢" (50-99), "⟣" (25-49), "◎" (<25)
probability_grade: "★" (≥90), "☆" (70-89), "◆" (50-69), "◊" (<50)
causality_level: "α" (≥95), "β" (80-94), "γ" (60-79), "δ" (<60)
entropy_rank: "Ξ" (≥85), "Σ" (65-84), "Π" (45-64), "Λ" (<45)
consciousness_scale: "◈" (≥200), "◇" (100-199), "◆" (50-99), "◉" (<50)
reality_category: "⚡" (≥98), "⚜" (90-97), "⚛" (80-89), "◎" (<80)
transcendence_supreme: "⟰" (≥99), "⟱" (95-98), "⟲" (90-94), "⟳" (<90)
Expected Output:
REALITY: INFINITE COSMOS | ARCHITECTURE: 7500.0 | DYNAMICS: 19800.0 | TEMPORAL: 1080.0 | EMERGENCE: 4950.0 | SYNTHESIS: 1651.5 | CONSCIOUSNESS: 1980.0 | QUANTUM: 8100.0 | MASTERY: 2635.4 | SIG: INFINITEΩ⟡★αΞ◈⚡⟰ | ULTIMATE: 15981.9
REALITY: QUANTUM NEXUS | ARCHITECTURE: 3000.0 | DYNAMICS: 8400.0 | TEMPORAL: 576.0 | EMERGENCE: 2700.0 | SYNTHESIS: 735.2 | CONSCIOUSNESS: 896.0 | QUANTUM: 3600.0 | MASTERY: 560.6 | SIG: QUANTUMΦ⟢☆βΣ◇⚜⟱ | ULTIMATE: 6531.8
REALITY: TRANSCENDENT VOID | ARCHITECTURE: 12000.0 | DYNAMICS: 36000.0 | TEMPORAL: 1800.0 | EMERGENCE: 9900.0 | SYNTHESIS: 3549.0 | CONSCIOUSNESS: 4950.0 | QUANTUM: 16200.0 | MASTERY: 28446.8 | SIG: TRANSCENDENT∞⟡★αΞ◈⚡⟰ | ULTIMATE: 59745.8 """

# define main
def main():
    # set storing variables for calling func with inputs from each profile
    result1 = reality_matrix("Infinite Cosmos", 30, 125, 80, 96, 90, 180, 220, 99, 85, 95, 108, 75, 99, 99)
    result2 = reality_matrix("Quantum Nexus", 20, 75, 60, 85, 72, 120, 140, 92, 70, 80, 72, 50, 90, 96)
    result3 = reality_matrix("Transcendent Void", 60, 200, 100, 98, 95, 300, 400, 99, 95, 99, 180, 120, 99, 99)
    # print each item stored in storing variables 
    print(result1)
    print(result2)
    print(result3) 

# def calling funct with parameters
def reality_matrix(reality_name, dimension_count, timeline_branches, probability_vectors, causality_strength, entropy_resistance, information_flow, consciousness_nodes, reality_stability, temporal_coherence, spatial_integrity, quantum_entanglement, field_density, emergence_factor, transcendence_coefficient):
    # get all imp formulas 
    dimensional_architecture = (dimension_count * timeline_branches * probability_vectors) / (causality_strength + entropy_resistance)
    information_dynamics = (information_flow * consciousness_nodes * reality_stability) / 100
    temporal_matrix = (temporal_coherence * spatial_integrity * quantum_entanglement) / field_density
    emergence_quotient = (emergence_factor * transcendence_coefficient * dimensional_architecture) / 1000
    reality_synthesis = (information_dynamics + temporal_matrix + emergence_quotient) * dimension_count / 100
    consciousness_integration = (consciousness_nodes * transcendence_coefficient * reality_stability) / (timeline_branches + 1)
    quantum_coherence = (quantum_entanglement * field_density * emergence_factor) / (entropy_resistance + 1)
    multidimensional_mastery = (reality_synthesis * consciousness_integration * quantum_coherence) / 10000 
    # get sig and index 
    first,last = reality_name.split() # get 2 parts  
    first15_reality=first[:15] # get first 15 letters from 1st part 
    # class logic
    dimension_tier =  "∞"*(dimension_count >= 50) + "Ω"*(30<dimension_count<49) + "Φ"*(20<dimension_count<29) + "Ψ"*(10<dimension_count<19) + "Δ"*(dimension_count<10)
    timeline_class = "⟡"* (timeline_branches>=100)+ "⟢"* (50<timeline_branches<99)+ "⟣"* (25<timeline_branches<49)+ "◎"* (timeline_branches<25)
    probability_grade = "★"* (probability_vectors>=90) + "☆"*(70 < probability_vectors< 89) + "◆"* (50<probability_vectors<69) + "◊"*(probability_vectors<50)
    causality_level = "α"*(causality_strength>=95)+ "β"*(80<causality_strength<94)+ "γ"* (60<causality_strength<79)+"δ"*(causality_strength<60)
    entropy_rank =  "Ξ"* (entropy_resistance>=85) + "Σ"* (65<entropy_resistance<84)+ "Π"* (45<entropy_resistance<64)+ "Λ"*(entropy_resistance<45)
    consciousness_scale = "◈"*(consciousness_nodes>=200) + "◇"* (100<consciousness_nodes<199)+ "◆"* (50<consciousness_nodes<99)+"◉"*(consciousness_nodes<50)
    reality_category = "⚡"*(reality_stability>=98)+ "⚜"*(90<reality_stability<97)+ "⚛"* (80<reality_stability<89)+ "◎"* (reality_stability<80)
    transcendence_supreme = "⟰"* (transcendence_coefficient>=99) + "⟱"*(95<transcendence_coefficient<98)+ "⟲"*(90<transcendence_coefficient<94) + "⟳"*(transcendence_coefficient<90)
    # final values 
    supreme_signature = first15_reality + dimension_tier + timeline_class + probability_grade + causality_level + entropy_rank + consciousness_scale + reality_category + transcendence_supreme
    ultimate_reality_index = (multidimensional_mastery + dimensional_architecture + information_dynamics + temporal_matrix) * transcendence_coefficient / 1000

    # return f string 
    return f"REALITY: {reality_name.upper()} | ARCHITECTURE: {dimensional_architecture:0.1f} | DYNAMICS: {information_dynamics:0.1f} | TEMPORAL: {temporal_matrix:0.1f} | EMERGENCE: {emergence_quotient:0.1f} | SYNTHESIS: {reality_synthesis:0.1f} | CONSCIOUSNESS: {consciousness_integration:0.1f} | QUANTUM: {quantum_coherence:0.1f} | MASTERY: { multidimensional_mastery:0.1f} | SIG: {supreme_signature.upper()} | ULTIMATE: {ultimate_reality_index:0.1f}"

# call main
main()
