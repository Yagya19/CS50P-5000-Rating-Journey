"""PROBLEM 36: Advanced AI Neural Engine
Task: Write a function called neural_engine that creates a sophisticated artificial intelligence system simulating advanced neural network operations and machine learning calculations.
Requirements:
Function name: neural_engine
result1 = neural_engine("DeepLearn Nexus", 1200, 8, 10, 0.15, 100, 95, 6, 1000)
result2 = neural_engine("Neural Network", 800, 5, 8, 0.08, 150, 88, 4, 800)
result3 = neural_engine("Quantum Brain", 1500, 12, 15, 0.20, 80, 97, 8, 1200)
Takes 9 parameters: ai_model, input_neurons, hidden_layers, output_neurons, learning_rate, training_epochs, accuracy_target, data_complexity, computational_budget
Calculate network_complexity: (input_neurons + output_neurons) × hidden_layers × data_complexity ÷ 100
Calculate learning_velocity: learning_rate × training_epochs × accuracy_target ÷ 10
Calculate computational_load: (network_complexity + learning_velocity) × computational_budget ÷ 1000
Calculate intelligence_quotient: (accuracy_target × learning_velocity) ÷ (data_complexity + 1)
Calculate optimization_factor: (computational_load × intelligence_quotient) ÷ (100 - accuracy_target + 1)
Calculate neural_efficiency: (network_complexity + optimization_factor) × learning_rate ÷ hidden_layers
Create ai_signature: first8_model + neuron_scale + layer_depth + learning_class + accuracy_tier + complexity_grade
Calculate ultimate_intelligence: (neural_efficiency + intelligence_quotient + optimization_factor) × training_epochs ÷ 100
Return formatted string: "AI: MODEL | COMPLEXITY: C.C | VELOCITY: V.V | LOAD: L.L | IQ: I.I | OPTIMIZATION: O.O | EFFICIENCY: E.E | SIG: SIGNATURE | INTELLIGENCE: INT.INT"
Round all decimal values to 1 decimal place
Classification Logic:
neuron_scale: "M" (≥1000), "K" (500-999), "H" (100-499), "L" (<100)
layer_depth: "D" (≥10), "M" (5-9), "S" (<5)
learning_class: "F" (≥0.1), "N" (0.01-0.099), "S" (<0.01)
accuracy_tier: "A" (≥95), "B" (85-94), "C" (<85)
complexity_grade: "X" (≥8), "Y" (5-7), "Z" (<5)
Expected Output:
AI: DEEPLEARN NEXUS | COMPLEXITY: 180.0 | VELOCITY: 9.5 | LOAD: 1896.0 | IQ: 95.0 | OPTIMIZATION: 1805.0 | EFFICIENCY: 358.0 | SIG: DEEPLEARMDFAZ | INTELLIGENCE: 2258.0
AI: NEURAL NETWORK | COMPLEXITY: 120.0 | VELOCITY: 6.0 | LOAD: 1260.0 | IQ: 60.0 | OPTIMIZATION: 756.0 | EFFICIENCY: 219.2 | SIG: NEURALKMNBY | INTELLIGENCE: 1035.2
AI: QUANTUM BRAIN | COMPLEXITY: 240.0 | VELOCITY: 12.0 | LOAD: 2520.0 | IQ: 120.0 | OPTIMIZATION: 3024.0 | EFFICIENCY: 651.2 | SIG: QUANTUMMDFAX | INTELLIGENCE: 3795.2 """

# define main
def main():
    # set storing variables or calling func having inputs related to each profile
    result1 = neural_engine("DeepLearn Nexus", 1200, 8, 10, 0.15, 100, 95, 6, 1000)
    result2 = neural_engine("Neural Network", 800, 5, 8, 0.08, 150, 88, 4, 800)
    result3 = neural_engine("Quantum Brain", 1500, 12, 15, 0.20, 80, 97, 8, 1200)
    # get print of item in each storing variables
    print(result1)
    print(result2)
    print(result3)

# def calling func and give it parameters
def neural_engine(ai_model, input_neurons, hidden_layers, output_neurons, learning_rate, training_epochs, accuracy_target, data_complexity, computational_budget):
    # do all imp calculations
    network_complexity = (input_neurons + output_neurons) * hidden_layers * data_complexity / 100
    learning_velocity = learning_rate * training_epochs * accuracy_target / 10
    computational_load = (network_complexity + learning_velocity) * computational_budget / 1000
    intelligence_quotient = (accuracy_target * learning_velocity) / (data_complexity + 1)
    optimization_factor = (computational_load * intelligence_quotient) / (100 - accuracy_target + 1)
    neural_efficiency = (network_complexity + optimization_factor) * learning_rate / hidden_layers
    # get bases for sig and ultimate index
    first,last=ai_model.split()
    first8_model= first[:8]
    # set class logics
    neuron_scale = "M" * (input_neurons >= 1000) + "K"*(500<input_neurons<999) + "H"*(100<input_neurons<499) + "L"*(input_neurons<100)
    layer_depth = "D"*(hidden_layers>=10) + "M"*(5<hidden_layers<9) + "S"*(hidden_layers<5)
    learning_class = "F"*(learning_rate>=0.1) + "N"*(0.01<learning_rate<0.099)+"S"*(learning_rate<0.01)
    accuracy_tier = "A"*(accuracy_target>=95)+"B"*(85<accuracy_target<94)+ "C"*(accuracy_target<85)
    complexity_grade = "X"*(data_complexity>=8)+"Y"*(5<data_complexity<7)+"Z"*(data_complexity<5)
    # final sig calulations for sig and intg
    ai_signature = first8_model + neuron_scale + layer_depth + learning_class + accuracy_tier + complexity_grade
    ultimate_intelligence = (neural_efficiency + intelligence_quotient + optimization_factor) * training_epochs / 100
    
    #return f string 
    return f"AI: {ai_model.upper()} | COMPLEXITY: {network_complexity:0.1f} | VELOCITY: {learning_velocity:0.1f} | LOAD: {computational_load:0.1f} | IQ: {intelligence_quotient:0.1f} | OPTIMIZATION: { optimization_factor:0.1f} | EFFICIENCY: {neural_efficiency:0.1f} | SIG: { ai_signature.upper()} | INTELLIGENCE: {ultimate_intelligence:0.3f}"

# call main 
main()
