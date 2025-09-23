#PROBLEM 79 - LOGISTICS SIMULATION ENGINE (COMPLETE CHALLENGE FORMAT)
def main():
    result1 = logistics_simulator("global", "port1000📦cargo500🚚warehouse", 2, 3, 1)
    result2 = logistics_simulator("regional", "depot300🏭truck150📦center", 1, 2, 2)
    result3 = logistics_simulator("local", "store200🚚van100📦pickup", 3, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def logistics_simulator( supply_type, chain_data, disruption_risk, delivery_cycles, precision_level):
    #Step 1: Count Supply Chain Elements

    #chain_length: Count total characters in chain_data
    chain_length = len(chain_data)
    #shipment_units: Count digit characters (0-9) in chain_data
    shipment_units = chain_data.count("0") +  chain_data.count("1") +  chain_data.count("2") +  chain_data.count("3") +  chain_data.count("4") + chain_data.count("5") +  chain_data.count("6") +  chain_data.count("7") +  chain_data.count("8") +  chain_data.count("9") 
    #distribution_hubs: Count distribution marker characters ("📦", "🚚", "🏭") in chain_data
    distribution_hubs = chain_data.count("📦") +  chain_data.count("🚚") +  chain_data.count("🏭") 

    #MATHEMATICAL FORMULAS (COMPLETE):
    Supply_Chain_Complexity_Score = (chain_length * 12) + (shipment_units * 24) + (distribution_hubs * 45)
    Supply_Multiplier = 4.5*(supply_type=="global")+3.9*(supply_type=="regional")+3.2*(supply_type=="local")
    Logistics_Projection = Supply_Chain_Complexity_Score * Supply_Multiplier * delivery_cycles
    Raw_Supply_Chain_Efficiency_Index = Logistics_Projection - (disruption_risk * 140)
    Supply_Chain_Efficiency_Index =  Raw_Supply_Chain_Efficiency_Index*( Raw_Supply_Chain_Efficiency_Index>=280) + 280*(Raw_Supply_Chain_Efficiency_Index<280)
    Inventory_Flow_Ratio = (shipment_units) / (chain_length + (chain_length==0)) * (chain_length!=0) + 1.3*(chain_length==0)
    Delivery_Reliability = (Inventory_Flow_Ratio * 100) + (delivery_cycles * 70)
    Supply_Type_Complexity = 10*(supply_type=="global")+ 8*(supply_type=="regional") + 6*(supply_type=="local")
    Efficiency_Categories = "Disrupted"*(Supply_Chain_Efficiency_Index<500)+"Functional"*(500<=Supply_Chain_Efficiency_Index<700)+"Streamlined"*(Supply_Chain_Efficiency_Index>=700)
    Delivery_Categories = "Express_Delivery"*(delivery_cycles == 3) + "Standard_Delivery"*(delivery_cycles == 2) +"Economy_Delivery"*(delivery_cycles == 1) 
    Supply_Chain_Resilience = (distribution_hubs*130) / (shipment_units+(shipment_units==0))  *(shipment_units!=0) + 150*(shipment_units==0)
    Logistics_Signature = supply_type + str(delivery_cycles) + str(disruption_risk) + Efficiency_Categories 

    return f"DELIVERED: {Delivery_Categories} | TYPE: {supply_type} | CHAIN: {chain_length} | SHIPMENTS: {shipment_units} | HUBS: {distribution_hubs} | INDEX: {Supply_Chain_Efficiency_Index:.1f} | RELIABILITY: { Delivery_Reliability :.1f}% | FLOW: {Inventory_Flow_Ratio:.3f} | RESILIENCE: {Supply_Chain_Resilience :.1f}% | CATEGORY: {Efficiency_Categories} | COMPLEXITY: {Supply_Type_Complexity } | SIG: {Logistics_Signature}"

main()
