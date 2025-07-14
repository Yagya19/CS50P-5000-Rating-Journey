"""PROBLEM 34: Advanced Engineering Design Engine
Task: Write a function called engineering_engine that creates a comprehensive engineering design system for advanced structural and mechanical analysis.
Requirements:
Function name: engineering_engine
result1 = engineering_engine("Bridge Construction", 95, 800, 4.5, 20, 7, 80)
result2 = engineering_engine("Skyscraper Design", 100, 1200, 5.0, 15, 6, 75)
result3 = engineering_engine("Aircraft Engine", 85, 600, 3.0, 25, 9, 90)
Takes 7 parameters: project_name, material_strength, load_capacity, safety_factor, environmental_stress, design_complexity, efficiency_target
Calculate stress_analysis: (load_capacity × environmental_stress) ÷ (material_strength × safety_factor)
Calculate structural_integrity: material_strength × safety_factor ÷ (environmental_stress + 1)
Calculate design_optimization: (efficiency_target × design_complexity) ÷ stress_analysis
Calculate performance_index: (structural_integrity + design_optimization) × safety_factor ÷ 100
Calculate engineering_ratio: (load_capacity × efficiency_target) ÷ (material_strength + environmental_stress)
Calculate system_reliability: (100 - stress_analysis) × performance_index ÷ design_complexity
Create engineering_signature: first6_project + material_grade + load_class + safety_level + complexity_tier
Calculate excellence_factor: (performance_index + system_reliability + engineering_ratio) × efficiency_target ÷ 10
Return formatted string: "ENGINEERING: PROJECT | STRESS: S.S | INTEGRITY: I.I | OPTIMIZATION: O.O | PERFORMANCE: P.P | RELIABILITY: R.R | SIG: SIGNATURE | EXCELLENCE: E.E"
Round all decimal values to 1 decimal place
Classification Logic:
material_grade: "A" (≥90), "B" (70-89), "C" (<70)
load_class: "H" (≥1000), "M" (500-999), "L" (<500)
safety_level: "1" (≥4.0), "2" (2.0-3.9), "3" (<2.0)
complexity_tier: "X" (≥8), "Y" (5-7), "Z" (<5)
Expected Output:
ENGINEERING: BRIDGE CONSTRUCTION | STRESS: 1.1 | INTEGRITY: 180.0 | OPTIMIZATION: 636.4 | PERFORMANCE: 40.8 | RELIABILITY: 407.8 | SIG: BRIDGEAHX | EXCELLENCE: 358.5
ENGINEERING: SKYSCRAPER DESIGN | STRESS: 0.8 | INTEGRITY: 250.0 | OPTIMIZATION: 750.0 | PERFORMANCE: 50.0 | RELIABILITY: 624.0 | SIG: SKYSCH2Y | EXCELLENCE: 467.2
ENGINEERING: AIRCRAFT ENGINE | STRESS: 2.2 | INTEGRITY: 136.4 | OPTIMIZATION: 409.1 | PERFORMANCE: 27.3 | RELIABILITY: 270.7 | SIG: AIRCR1H1X | EXCELLENCE: 279.4 """

# define main
def main():
    # set storing variable for calling func with inputs relevant to each profiles
    result1 = engineering_engine("Bridge Construction", 95, 800, 4.5, 20, 7, 80)
    result2 = engineering_engine("Skyscraper Design", 100, 1200, 5.0, 15, 6, 75)
    result3 = engineering_engine("Aircraft Engine", 85, 600, 3.0, 25, 9, 90)
    # print items stored in storing variables 
    print(result1)
    print(result2)
    print(result3)
# def calling function and set parameters for it 
def engineering_engine(project_name, material_strength, load_capacity, safety_factor, environmental_stress, design_complexity, efficiency_target):
    stress_analysis = (load_capacity * environmental_stress) / (material_strength * safety_factor)
    structural_integrity = material_strength * safety_factor / (environmental_stress + 1)
    design_optimization = (efficiency_target * design_complexity) / stress_analysis
    performance_index = (structural_integrity + design_optimization) * safety_factor / 100
    engineering_ratio = (load_capacity * efficiency_target) / (material_strength + environmental_stress)
    system_reliability = (100 - stress_analysis) * performance_index / design_complexity
    # get sig and desg factor bases
    first,last=project_name.split()
    first6_project=first[:6]
    # set class conditions
    material_grade ="A" * (material_strength >= 90) + "B"*(70<material_strength<89) + "C"*(material_strength<70)
    load_class = "H"*(load_capacity>=1000) + "M"*(500<load_capacity<999) + "L"*(load_capacity<500)
    safety_level = "1"*(safety_factor>=4.0) + "2"*(2.0<safety_factor<3.9)+"3"*(safety_factor<2.0)
    complexity_tier = "X"*(design_complexity>=8)+"Y"*(5<design_complexity<7)+"Z"*(design_complexity<5)
    # get sig and desgn values
    engineering_signature = first6_project + material_grade + load_class + safety_level + complexity_tier
    excellence_factor = (performance_index + system_reliability + engineering_ratio) * efficiency_target / 10

    # return f string 
    return f"ENGINEERING: {project_name.upper()} | STRESS: {stress_analysis:0.1f} | INTEGRITY: {structural_integrity:0.1f} | OPTIMIZATION: {design_optimization:0.1f} | PERFORMANCE: {performance_index:0.1f} | RELIABILITY: {system_reliability:0.1f} | SIG: {engineering_signature.upper()} | EXCELLENCE: {excellence_factor:0.1f}"

# call main
main()
