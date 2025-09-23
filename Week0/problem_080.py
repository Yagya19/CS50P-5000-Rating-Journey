#PROBLEM 80 - INTEGRATED SYSTEM SIMULATION ENGINE (COMPLETE CHALLENGE FORMAT)
def main():
    result1 = system_integrator("full", "core2000⚡network800🔗database", 2, 3, 1)
    result2 = system_integrator("partial", "app1500⇔service600🔗cache", 1, 2, 2)
    result3 = system_integrator("minimal", "module1000🔗api400⚡storage", 3, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def system_integrator(integration_mode, system_data, complexity_scaling, synchronization_cycles, precision_level):
    #Step 1: Count Integration Elements

    #system_scope: Count total characters in system_data
    system_scope = len(system_data)
    #operational_units: Count digit characters (0-9) in system_data
    operational_units = system_data.count("0")+system_data.count("1")+system_data.count("2")+system_data.count("3")+system_data.count("4")+system_data.count("5")+system_data.count("6")+system_data.count("7")+system_data.count("8")+system_data.count("9")
    #interface_connectors: Count integration marker characters ("⚡", "⇔", "🔗") in system_data
    interface_connectors = system_data.count("⚡")+system_data.count("⇔")+system_data.count("🔗")

    #MATHEMATICAL FORMULAS (COMPLETE):
    System_Integration_Complexity_Score = (system_scope * 13) + (operational_units * 26) + (interface_connectors * 50)
    Integration_Multiplier = 4.8*(integration_mode=="full")+4.1*(integration_mode=="partial")+ 3.4*(integration_mode=="minimal")
    System_Synchronization_Projection = System_Integration_Complexity_Score * Integration_Multiplier * synchronization_cycles
    Raw_Multi_System_Performance_Index = System_Synchronization_Projection  - (complexity_scaling * 150)
    Multi_System_Performance_Index = Raw_Multi_System_Performance_Index *(Raw_Multi_System_Performance_Index >=300) + 300*(Raw_Multi_System_Performance_Index<300)
    Cross_Domain_Efficiency_Ratio = operational_units / (system_scope + ( system_scope==0)) * ( system_scope!=0) + 1.4*(system_scope==0)
    Integration_Stability = (Cross_Domain_Efficiency_Ratio  * 100) + (synchronization_cycles * 75)
    Integration_Mode_Complexity = 12*(integration_mode=="full")+9*(integration_mode=="partial")+7*(integration_mode=="minimal")
    Performance_Categories ="Fragmented_Integration"*(Multi_System_Performance_Index < 550)+"Stable_Integration"*(550<=Multi_System_Performance_Index<750)+"Seamless_Integration"*(Multi_System_Performance_Index>=750)
    Synchronization_Categories = "Real_Time_Sync"*( synchronization_cycles == 3) + "Batch_Sync"*( synchronization_cycles == 2) + "Periodic_Sync"*( synchronization_cycles == 1) 
    System_Interoperability = (interface_connectors*140) / (operational_units+(operational_units==0)) * (operational_units!=0) + 160*(operational_units==0)
    Integration_Signature =integration_mode + str(synchronization_cycles) + str(complexity_scaling) + Performance_Categories 

    return f"INTEGRATED: {Synchronization_Categories} | MODE: {integration_mode} | SCOPE: {system_scope} | UNITS: {operational_units} | INTERFACES: {interface_connectors} | INDEX: {Multi_System_Performance_Index :.1f} | STABILITY: {Integration_Stability:.1f}% | EFFICIENCY: {Cross_Domain_Efficiency_Ratio:.3f} | INTEROPERABILITY: {System_Interoperability :.1f}% | CATEGORY: {Performance_Categories} | COMPLEXITY: {Integration_Mode_Complexity} | SIG: {Integration_Signature }"

main()
