"""PROBLEM 29: Grandmaster Algorithm Engine
Task: Write a function called grandmaster_engine that creates the ultimate computational engine representing the pinnacle of Week 0 algorithmic mastery.
Requirements:
Function name: grandmaster_engine
result1 = grandmaster_engine("Quantum Dynamics", "Quantum Computing", "Dr. Sarah Chen", 8000, 1480000000, 90, 78, 85, 75, 24, 50, 2010)
result2 = grandmaster_engine("Neural Networks", "AI Research", "Prof. Mike Wang", 4000, 850000000, 88, 72, 70, 63, 18, 35, 2017)
result3 = grandmaster_engine("Fusion Systems", "Energy", "Dr. Lisa Rodriguez", 10000, 2000000000, 92, 80, 90, 72, 25, 60, 1995)
Takes 12 parameters: enterprise, domain, leader, workforce, capital, efficiency, innovation, market_position, sustainability, technology_stack, geographic_reach, establishment_year
Calculate enterprise_maturity: (2025 - establishment_year) × (workforce ÷ 100) × efficiency ÷ 10
Calculate capital_velocity: capital ÷ (workforce + geographic_reach + technology_stack)
Calculate innovation_momentum: (innovation × market_position × sustainability) ÷ efficiency
Calculate market_synthesis: (market_position × geographic_reach × technology_stack) ÷ (2025 - establishment_year)
Calculate efficiency_matrix: (efficiency × innovation × sustainability) ÷ (100 - market_position)
Calculate technological_advantage: technology_stack × geographic_reach × innovation ÷ 1000
Create grandmaster_signature: first7_enterprise + domain_length + leader_initials + capital_millions + tech_code + establishment_decade
Calculate ultimate_mastery: (enterprise_maturity + capital_velocity + innovation_momentum + market_synthesis + efficiency_matrix + technological_advantage) × workforce ÷ 10000
Return formatted string: "GRANDMASTER: ENTERPRISE | DOMAIN: D | LEADER: L | MATURITY: M.M | VELOCITY: V.V | MOMENTUM: Mo.Mo | SYNTHESIS: S.S | MATRIX: Ma.Ma | ADVANTAGE: A.A | SIGNATURE: SIG | MASTERY: Ma.Ma"
Round all decimal values to 1 decimal place.
GRANDMASTER: QUANTUM DYNAMICS | DOMAIN: Quantum Computing | LEADER: Dr. Sarah Chen | MATURITY: 180.0 | VELOCITY: 6757.0 | MOMENTUM: 2340.0 | SYNTHESIS: 2500.0 | MATRIX: 1800.0 | ADVANTAGE: 720.0 | SIGNATURE: Quantum16SC148201 | MASTERY: 1429.7
GRANDMASTER: NEURAL NETWORKS | DOMAIN: AI Research | LEADER: Prof. Mike Wang | MATURITY: 96.0 | VELOCITY: 4255.0 | MOMENTUM: 1575.0 | SYNTHESIS: 1200.0 | MATRIX: 1134.0 | ADVANTAGE: 504.0 | SIGNATURE: Neural11MW85200 | MASTERY: 861.8
GRANDMASTER: FUSION SYSTEMS | DOMAIN: Energy | LEADER: Dr. Lisa Rodriguez | MATURITY: 240.0 | VELOCITY: 8000.0 | MOMENTUM: 2880.0 | SYNTHESIS: 4000.0 | MATRIX: 2160.0 | ADVANTAGE: 1000.0 | SIGNATURE: Fusion6LR200199 | MASTERY: 1828.0 """ 

# def main 
def main():
    # set storing variable for calling function with inputs 
    result1 = grandmaster_engine("Quantum Dynamics", "Quantum Computing", "Dr. Sarah Chen", 8000, 1480000000, 90, 78, 85, 75, 24, 50, 2010)
    result2 = grandmaster_engine("Neural Networks", "AI Research", "Prof. Mike Wang", 4000, 850000000, 88, 72, 70, 63, 18, 35, 2017)
    result3 = grandmaster_engine("Fusion Systems", "Energy", "Dr. Lisa Rodriguez", 10000, 2000000000, 92, 80, 90, 72, 25, 60, 1995)
    # print the stored items in storing variables
    print(result1)
    print(result2)
    print(result3)
# def calling function and set temp variables for it
def grandmaster_engine(enterprise, domain, leader, workforce, capital, efficiency, innovation, market_position, sustainability, technology_stack, geographic_reach, establishment_year):
    # do all calculations 
        enterprise_maturity = (2025 - establishment_year) * (workforce / 100) * efficiency / 10
        capital_velocity = capital / (workforce + geographic_reach + technology_stack)
        innovation_momentum = (innovation * market_position * sustainability) / efficiency
        market_synthesis = (market_position * geographic_reach * technology_stack) / (2025 - establishment_year)
        efficiency_matrix = (efficiency * innovation * sustainability) / (100 - market_position)
        technological_advantage = technology_stack * geographic_reach * innovation / 1000
        # Create grandmaster_signature: first7_enterprise + str(domain_length) + leader_initials + str(capital_millions) + str(tech_code) + str(establishment_decade)
        first,last=enterprise.split()
        first7_enterprise=first[:7]
        domain_length=len(domain)
        title,ini_first,ini_last=leader.split()
        leader_initials=ini_first[:1]+ini_last[:1]
        capital_millions=[str(capital)[:3]]
        tech_code=technology_stack
        establishment_decade = [str(establishment_year)[:3]]
        grandmaster_signature = first7_enterprise + str(domain_length) + leader_initials + str(capital_millions) + str(tech_code) + str(establishment_decade)
        # get ultimate mastery 
        ultimate_mastery = (enterprise_maturity + capital_velocity + innovation_momentum + market_synthesis + efficiency_matrix + technological_advantage) * workforce / 10000
        # return f string 
        return f"GRANDMASTER: {enterprise.upper()} | DOMAIN: {domain} | LEADER: {leader} | MATURITY: {enterprise_maturity:0.1f} | VELOCITY: {capital_velocity:0.1f} | MOMENTUM: {innovation_momentum:0.2f} | SYNTHESIS: {market_synthesis:0.1f} | MATRIX: {efficiency_matrix:0.2f} | ADVANTAGE: {technological_advantage:0.1f} | SIGNATURE: {grandmaster_signature} | MASTERY: {ultimate_mastery:0.2f}"
# call main
main()
