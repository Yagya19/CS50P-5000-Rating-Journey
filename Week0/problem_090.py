#PROBLEM 90 - INTEGRATED PATTERN RECOGNITION SYSTEM (COMPLETE CHALLENGE FORMAT)
def main():
    result1 = pattern_integration_system("full", "multi123⚡pattern456🔀analysis⟲comprehensive", 2, 3, 1)
    result2 = pattern_integration_system("partial", "detect248⚡classify567🔀recognition", 1, 2, 2)
    result3 = pattern_integration_system("selective", "analyze135🔀pattern⟲focused", 3, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def pattern_integration_system(integration_scope, pattern_data, recognition_complexity, analysis_iterations, precision_level):
    #Step 1: Count Integration Pattern Elements

    #pattern_universe: Count total characters in pattern_data
    pattern_universe = len(pattern_data)
    #recognition_elements: Count digit characters (0-9) in pattern_data
    recognition_elements =  pattern_data.count("0") + pattern_data.count("1") + pattern_data.count("2") +  pattern_data.count("3") + pattern_data.count("4") + pattern_data.count("5") +  pattern_data.count("6") + pattern_data.count("7") + pattern_data.count("8") + pattern_data.count("9") 
    #integration_markers: Count multi-pattern indicator characters ("⚡", "🔀", "⟲") in pattern_data
    integration_markers = pattern_data.count("⚡") + pattern_data.count("🔀") + pattern_data.count("⟲")
    Pattern_Integration_Complexity_Score = (pattern_universe * 23) + ( recognition_elements * 46) + (integration_markers * 100)
    Integration_Multiplier = 7.8*(integration_scope=="full") + 7.3*(integration_scope=="partial") + 6.8*(integration_scope=="selective") 
    Multi_Pattern_Recognition_Projection = Pattern_Integration_Complexity_Score * Integration_Multiplier * analysis_iterations
    Raw_Recognition_Mastery_Index = Multi_Pattern_Recognition_Projection  - (recognition_complexity * 250)
    Recognition_Mastery_Index = Raw_Recognition_Mastery_Index * (Raw_Recognition_Mastery_Index >=500) + 500*(Raw_Recognition_Mastery_Index<500)
    Pattern_Synthesis_Ratio =  recognition_elements / (pattern_universe + (pattern_universe==0)) * (pattern_universe!=0) + 2.4*(pattern_universe==0)
    Integration_Accuracy = (Pattern_Synthesis_Ratio * 100) + (analysis_iterations * 125)
    Integration_Scope_Complexity = 15*(integration_scope=="full") + 12*(integration_scope=="partial") + 10*(integration_scope=="selective")
    Mastery_Categories = "Expert_Recognition"*(Recognition_Mastery_Index>=1250) + "Advanced_Recognition"*(950<=Recognition_Mastery_Index<1250) + "Basic_Recognition"*(Recognition_Mastery_Index<950) 
    Integration_Categories = "Comprehensive_Integration"*(analysis_iterations == 3) +  "Standard_Integration"*(analysis_iterations == 2) +  "Limited_Integration"*(analysis_iterations == 1) 
    Pattern_Coherence =  (integration_markers * 240) / (recognition_elements+(recognition_elements==0)) * (recognition_elements!=0) + 260*(recognition_elements==0)
    Integration_Signature = integration_scope + str(analysis_iterations) + str(recognition_complexity) + Mastery_Categories 

    return f"INTEGRATED: {Integration_Categories} | SCOPE: {integration_scope} | UNIVERSE: {pattern_universe} | ELEMENTS: {recognition_elements} | MARKERS: {integration_markers} | INDEX: {Recognition_Mastery_Index:.1f} | ACCURACY: {Integration_Accuracy:.1f}% | SYNTHESIS: {Pattern_Synthesis_Ratio:.3f} | COHERENCE: {Pattern_Coherence:.1f}% | CATEGORY: {Mastery_Categories} | COMPLEXITY: {Integration_Scope_Complexity} | SIG: {Integration_Signature}"

main()
