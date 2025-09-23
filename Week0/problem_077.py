#PROBLEM 77 - MANUFACTURING SIMULATION ENGINE (COMPLETE CHALLENGE FORMAT)
def main():
    result1 = manufacturing_simulator("automotive", "factory500⚙assembly200🔧paint", 2, 3, 1)
    result2 = manufacturing_simulator("electronics", "plant300⚡chips150⚙test", 1, 2, 2)
    result3 = manufacturing_simulator("textile", "mill400🔧fabric100⚙dye", 3, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def manufacturing_simulator(production_type, factory_data, efficiency_loss, production_cycles, precision_level):
    #Step 1: Count Manufacturing Elements
    #facility_scale: Count total characters in factory_data
    facility_scale = len(factory_data)
    #output_units: Count digit characters (0-9) in factory_data
    output_units =  factory_data.count("0") +  factory_data.count("1") +  factory_data.count("2") +  factory_data.count("3") + factory_data.count("4") +  factory_data.count("5") +  factory_data.count("6") +  factory_data.count("7") +factory_data.count("8") + factory_data.count("9")
    #process_stages: Count process indicator characters ("⚙", "🔧", "⚡") in factory_data
    process_stages = factory_data.count("⚙") +  factory_data.count("🔧") +  factory_data.count("⚡") 

    #MATHEMATICAL FORMULAS (COMPLETE):
    Production_Complexity_Score = (facility_scale * 10) + (output_units * 20) + (process_stages * 35)
    Production_Multiplier = 3.8*(production_type=="automotive")+3.3*(production_type=="electronics")+2.9*(production_type=="textile")
    Manufacturing_Projection = Production_Complexity_Score * Production_Multiplier  * production_cycles
    Raw_Production_Efficiency_Index = Manufacturing_Projection  - (efficiency_loss * 120)
    Production_Efficiency_Index =  Raw_Production_Efficiency_Index*( Raw_Production_Efficiency_Index>=240) + 240*( Raw_Production_Efficiency_Index<240)
    Output_Density_Ratio = output_units / (facility_scale+(facility_scale==0)) *(facility_scale!=0) + 1.1*(facility_scale==0)
    Quality_Assurance_Rating = (Output_Density_Ratio * 100) + (production_cycles * 60)
    Production_Type_Complexity = 9*(production_type=="automotive")+8*(production_type=="electronics")+6*(production_type=="textile")
    Efficiency_Categories = "Low_Efficiency"*( Production_Efficiency_Index <420) + "Standard_Efficiency"*(420<=Production_Efficiency_Index<600)+"High_Efficiency"*(Production_Efficiency_Index>=600)
    Production_Categories = "Mass_Production"*(production_cycles == 3) +  "Batch_Production"*(production_cycles == 2) +  "Custom_Production"*(production_cycles == 1) 
    Process_Optimization = (process_stages *110) / (output_units+(output_units==0)) * (output_units!=0) + 130*(output_units==0)
    Manufacturing_Signature = production_type + str(production_cycles) + str(efficiency_loss) + Efficiency_Categories 

    return f"PRODUCED: {Production_Categories} | TYPE: {production_type} | SCALE: {facility_scale} | OUTPUT: {output_units} | STAGES: {process_stages} | INDEX: {Production_Efficiency_Index:.1f} | QUALITY: {Quality_Assurance_Rating:.1f}% | DENSITY: {Output_Density_Ratio:.3f} | OPTIMIZATION: { Process_Optimization:.1f}% | CATEGORY: {Efficiency_Categories} | COMPLEXITY: {Production_Type_Complexity} | SIG: {Manufacturing_Signature}"

main()
