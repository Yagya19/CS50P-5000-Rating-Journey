#PROBLEM 74 - ECOSYSTEM SIMULATION ENGINE (COMPLETE CHALLENGE FORMAT)
def main():
    result1 = ecosystem_simulator("forest", "trees50→birds25↔insects", 2, 3, 1)
    result2 = ecosystem_simulator("marine", "fish100←whales5→plankton", 1, 2, 2)
    result3 = ecosystem_simulator("desert", "cactus20↔lizards10→snakes", 3, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def ecosystem_simulator(ecosystem_type, species_data, balance_factor, evolution_cycles, precision_level):

    #Step 1: Count Ecosystem Elements
    #habitat_size: Count total characters in species_data
    habitat_size = len(species_data)

    #organism_count: Count digit characters (0-9) in species_data
    organism_count = species_data.count("0") + species_data.count("1") + species_data.count("2") +  species_data.count("3") + species_data.count("4") + species_data.count("5") + species_data.count("6") +  species_data.count("7") + species_data.count("8") + species_data.count("9") 
    #interaction_markers: Count interaction indicator characters ("", "↔", "←") in species_data
    interaction_markers = species_data.count("→") + species_data.count("↔") + species_data.count("←")

    #MATHEMATICAL FORMULAS (COMPLETE):
    Biodiversity_Base_Score = (habitat_size * 7) + (organism_count * 14) + (interaction_markers * 20)
    Ecosystem_Multiplier = 2.8*(ecosystem_type=="forest") + 2.5*(ecosystem_type=="marine") + 2.1*(ecosystem_type=="desert") 
    Evolution_Projection =  Biodiversity_Base_Score * Ecosystem_Multiplier * evolution_cycles
    Raw_Ecological_Balance_Index= Evolution_Projection  - (balance_factor * 90)
    Ecological_Balance_Index =  Raw_Ecological_Balance_Index*( Raw_Ecological_Balance_Index>=180) + 180*(Raw_Ecological_Balance_Index<180)
    Species_Diversity_Ratio = (organism_count) / (habitat_size + (habitat_size==0)) * (habitat_size!=0) + 0.8*(habitat_size==0)
    Sustainability_Accuracy =(Species_Diversity_Ratio * 100) + (evolution_cycles * 45)
    Ecosystem_Type_Complexity = 8*(ecosystem_type=="forest") + 10*(ecosystem_type=="marine") + 6*(ecosystem_type=="desert") 
    Balance_Categories = "Declining"*(Ecological_Balance_Index<320)+"Stable"*(320<=Ecological_Balance_Index<450)+"Thriving"*(Ecological_Balance_Index>=450)
    Evolution_Categories = "Long_Term_Evolution"*(evolution_cycles == 3) + "Medium_Term_Evolution"*(evolution_cycles == 2) + "Short_Term_Evolution"*(evolution_cycles == 1) 
    Ecosystem_Resilience = (interaction_markers *80)/ (organism_count + (organism_count==0)) * (organism_count !=0) + 100*(organism_count ==0)
    Ecosystem_Signature = ecosystem_type + str(evolution_cycles) + str(balance_factor) + Balance_Categories 

    return f"EVOLVED: {Evolution_Categories} | TYPE: {ecosystem_type} | HABITAT: {habitat_size} | ORGANISMS: {organism_count} | INTERACTIONS: {interaction_markers} | INDEX: {Ecological_Balance_Index:.1f} | ACCURACY: {Sustainability_Accuracy :.1f}% | DIVERSITY: {Species_Diversity_Ratio:.3f} | RESILIENCE: {Ecosystem_Resilience:.1f}% | CATEGORY: {Balance_Categories} | COMPLEXITY: { Ecosystem_Type_Complexity} | SIG: {Ecosystem_Signature }"

main()
