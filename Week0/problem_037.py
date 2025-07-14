"""PROBLEM 37: Ultimate Quantum Computing Engine
Task: Write a function called quantum_engine that creates the ultimate quantum computing simulation system representing the pinnacle of computational physics and quantum mechanics modeling.
Requirements:
Function name: quantum_engine
result1 = quantum_engine("Quantum Nexus", 100, 15, 200, 99.5, 2.0, 2000, 50, 3.0, 0.05)
result2 = quantum_engine("Photonic Core", 60, 8, 140, 97.8, 3.5, 1200, 35, 2.5, 0.8)
result3 = quantum_engine("SuperCold Matrix", 150, 20, 300, 99.8, 1.5, 3000, 75, 4.0, 0.01)
Takes 10 parameters: quantum_system, qubit_count, entanglement_depth, coherence_time, gate_fidelity, error_rate, quantum_volume, algorithm_complexity, processing_frequency, temperature_kelvin
Calculate quantum_advantage: (qubit_count × entanglement_depth × coherence_time) ÷ (error_rate + 1)
Calculate computational_supremacy: (quantum_volume × gate_fidelity × processing_frequency) ÷ 1000
Calculate decoherence_factor: (100 - error_rate) × coherence_time ÷ (temperature_kelvin + 1)
Calculate quantum_efficiency: (quantum_advantage + computational_supremacy) × gate_fidelity ÷ 100
Calculate algorithm_performance: (algorithm_complexity × quantum_efficiency) ÷ decoherence_factor
Calculate entanglement_score: (entanglement_depth × qubit_count × coherence_time) ÷ (error_rate × temperature_kelvin + 1)
Create quantum_signature: first9_system + qubit_class + entanglement_tier + fidelity_grade + volume_scale + temp_category
Calculate supreme_quantum_index: (quantum_efficiency + algorithm_performance + entanglement_score) × processing_frequency ÷ 1000
Return formatted string: "QUANTUM: SYSTEM | ADVANTAGE: A.A | SUPREMACY: S.S | DECOHERENCE: D.D | EFFICIENCY: E.E | PERFORMANCE: P.P | ENTANGLEMENT: En.En | SIG: SIGNATURE | SUPREME: Sp.Sp"
Round all decimal values to 1 decimal place
Classification Logic:
qubit_class: "S" (≥100), "A" (50-99), "B" (20-49), "C" (<20)
entanglement_tier: "M" (≥10), "H" (5-9), "L" (<5)
fidelity_grade: "P" (≥99), "E" (95-98), "G" (90-94), "F" (<90)
volume_scale: "X" (≥1000), "Y" (500-999), "Z" (<500)
temp_category: "U" (≤0.1), "C" (0.1-1.0), "W" (>1.0)
Expected Output:
QUANTUM: QUANTUM NEXUS | ADVANTAGE: 19000.0 | SUPREMACY: 4851.0 | DECOHERENCE: 9800.0 | EFFICIENCY: 237.5 | PERFORMANCE: 1.2 | ENTANGLEMENT: 95000.0 | SIG: QUANTUMSMEPXU | SUPREME: 952.7
QUANTUM: PHOTONIC CORE | ADVANTAGE: 8400.0 | SUPREMACY: 2394.0 | DECOHERENCE: 4550.0 | EFFICIENCY: 107.9 | PERFORMANCE: 1.4 | ENTANGLEMENT: 42000.0 | SIG: PHOTONICAHEGYC | SUPREME: 425.3
QUANTUM: SUPERCOLD MATRIX | ADVANTAGE: 31500.0 | SUPREMACY: 7920.0 | DECOHERENCE: 29700.0 | EFFICIENCY: 394.2 | PERFORMANCE: 0.7 | ENTANGLEMENT: 157500.0 | SIG: SUPERCOLDSMEPXU | SUPREME: 1576.8"""

# define main
def main():
    # cretae storing variables for calling func with inputs relevant to each profile 
    result1 = quantum_engine("Quantum Nexus", 100, 15, 200, 99.5, 2.0, 2000, 50, 3.0, 0.05)
    result2 = quantum_engine("Photonic Core", 60, 8, 140, 97.8, 3.5, 1200, 35, 2.5, 0.8)
    result3 = quantum_engine("SuperCold Matrix", 150, 20, 300, 99.8, 1.5, 3000, 75, 4.0, 0.01)
    # print each item in storing variabel
    print(result1)
    print(result2)
    print(result3)

# define calling func with parameters
def quantum_engine(quantum_system, qubit_count, entanglement_depth, coherence_time, gate_fidelity, error_rate, quantum_volume, algorithm_complexity, processing_frequency, temperature_kelvin):
    # do all imp calculations
    quantum_advantage = (qubit_count * entanglement_depth * coherence_time) / (error_rate + 1)
    computational_supremacy = (quantum_volume * gate_fidelity * processing_frequency) / 1000
    decoherence_factor = (100 - error_rate) * coherence_time / (temperature_kelvin + 1)
    quantum_efficiency = (quantum_advantage + computational_supremacy) * gate_fidelity / 100
    algorithm_performance = (algorithm_complexity * quantum_efficiency) / decoherence_factor
    entanglement_score = (entanglement_depth * qubit_count * coherence_time) / (error_rate * temperature_kelvin + 1)
    # get sig and index
    first,last=quantum_system.split() # create 2 variables 
    first9_system= first[:9] # slice first to get 1st 9 letters
    # class logics
    qubit_class = "S"*(qubit_count>=100) + "A"*(50<qubit_count<99) + "B"*(20<qubit_count<49) + "C"*(qubit_count<20)
    entanglement_tier = "M"*(entanglement_depth>=10) + "H"*(5<qubit_count<9)+"L"*(qubit_count<5)
    fidelity_grade = "P"*(gate_fidelity >=99)+ "E"*(95<qubit_count<98)+"G"*(90<qubit_count<94)+"F"*(qubit_count<90)
    volume_scale = "X"*(quantum_volume>=1000)+ "Y"*(500<qubit_count<999) + "Z"*(qubit_count<500)
    temp_category = "U"*(temperature_kelvin<=0.1)+ "C"*(0.1<qubit_count<1.0)+ "W"*(qubit_count>1.0)
    # final formulas
    quantum_signature = first9_system + qubit_class + entanglement_tier + fidelity_grade + volume_scale + temp_category
    supreme_quantum_index = (quantum_efficiency + algorithm_performance + entanglement_score) * processing_frequency / 1000
    
    #return f string 
    return f"QUANTUM: {quantum_system.upper()} | ADVANTAGE: {quantum_advantage:0.1f} | SUPREMACY: {computational_supremacy:0.1f} | DECOHERENCE: {decoherence_factor:0.1f} | EFFICIENCY: {quantum_efficiency:0.1f} | PERFORMANCE: {algorithm_performance:0.1f} | ENTANGLEMENT: { entanglement_score:0.2f} | SIG: {quantum_signature.upper()} | SUPREME: {supreme_quantum_index:0.2f}"

# call main
main()
