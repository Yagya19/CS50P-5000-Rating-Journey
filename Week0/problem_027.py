""""PROBLEM 27: Ultimate System Synthesizer
Task: Write a function called system_synthesizer that creates the ultimate computational platform integrating all advanced Week 0 concepts at peak complexity.
Requirements:
Function name: system_synthesizer
result1 = system_synthesizer("Innovate Tech", "AI Platform", "Sarah Johnson", 850000, 180, 8, 3, 90, "NYC", 12)
result2 = system_synthesizer("Future Systems", "Blockchain", "Mike Chen", 750000, 150, 7, 4, 80, "LAX", 10)
result3 = system_synthesizer("Global Solutions", "Cloud", "Lisa Wang", 980000, 120, 9, 2, 95, "CHI", 15)
Takes 10 parameters: organization, project_type, team_lead, budget, timeline_days, complexity_score, risk_factor, success_probability, location, stakeholders
Calculate budget_efficiency: budget ÷ (timeline_days × team_lead_length × complexity_score)
Calculate risk_adjusted_value: (budget × success_probability ÷ 100) ÷ (risk_factor + 1)
Calculate project_velocity: (complexity_score × success_probability) ÷ timeline_days
Calculate stakeholder_impact: stakeholders × budget ÷ 1000000 × (100 - risk_factor)
Calculate timeline_pressure: (complexity_score + risk_factor) ÷ timeline_days × 100
Calculate synthesis_rating: (budget_efficiency + risk_adjusted_value + project_velocity + stakeholder_impact) ÷ timeline_pressure
Create master_identifier: first5_org + project_length + lead_initials + last4_budget + location_code
Calculate ultimate_synthesis: synthesis_rating × (success_probability ÷ 10) × (stakeholders ÷ 5) × complexity_score
Return formatted string: "SYNTHESIS: ORG | PROJECT: P | LEAD: L | EFFICIENCY: E.E | VALUE: V.V | VELOCITY: Ve.Ve | RATING: R.R | ID: I | ULTIMATE: U.U"
Round all decimal values to 1 decimal place
SYNTHESIS: INNOVATE TECH | PROJECT: AI Platform | LEAD: Sarah Johnson | EFFICIENCY: 2.1 | VALUE: 76500.0 | VELOCITY: 6.0 | RATING: 1043.0 | ID: Innov11SJ5000NYC | ULTIMATE: 562320.0
SYNTHESIS: FUTURE SYSTEMS | PROJECT: Blockchain | LEAD: Mike Chen | EFFICIENCY: 1.8 | VALUE: 67500.0 | VELOCITY: 5.6 | RATING: 896.3 | ID: Futur10MC0000LAX | ULTIMATE: 448150.0
SYNTHESIS: GLOBAL SOLUTIONS | PROJECT: Cloud | LEAD: Lisa Wang | EFFICIENCY: 3.2 | VALUE: 95000.0 | VELOCITY: 7.5 | RATING: 1305.7 | ID: Globa5LW8000CHI | ULTIMATE: 782850.0  
"""
#def main function
def main():
    # set storing variabels for calling function with inputs for each profile
    result1 = system_synthesizer("Innovate Tech", "AI Platform", "Sarah Johnson", 850000, 180, 8, 3, 90, "NYC", 12)
    result2 = system_synthesizer("Future Systems", "Blockchain", "Mike Chen", 750000, 150, 7, 4, 80, "LAX", 10)
    result3 = system_synthesizer("Global Solutions", "Cloud", "Lisa Wang", 980000, 120, 9, 2, 95, "CHI", 15)
    # print item of each storing variable 
    print(result1)
    print(result2)
    print(result3)
# def calling function with temp varaibales 
def system_synthesizer(organization, project_type, team_lead, budget, timeline_days, complexity_score, risk_factor, success_probability, location, stakeholders):
    # al imp calculations 
    team_lead_length=len(team_lead)
    budget_efficiency= budget / (timeline_days * team_lead_length * complexity_score)
    risk_adjusted_value = (budget * success_probability / 100) / (risk_factor + 1)
    project_velocity = (complexity_score * success_probability) / timeline_days
    stakeholder_impact = stakeholders * budget / 1000000 * (100 - risk_factor)
    timeline_pressure = (complexity_score + risk_factor) / timeline_days * 100
    synthesis_rating = (budget_efficiency + risk_adjusted_value + project_velocity + stakeholder_impact) / timeline_pressure

    #Create master_identifier: first5_org + str(project_length) + lead_initials + str(last4_budget) + location_code
    first,last=organization.split()
    first5_org=first[:5]
    project_length=len(project_type)
    first_lead,last_lead=team_lead.split()
    first_lead_initials=first_lead[:1]
    last_lead_initials=last_lead[:1]
    lead_initials=first_lead_initials+last_lead_initials
    budget_str=str(budget)
    last4_budget=budget_str[-4:]
    master_identifier = first5_org + str(project_length) + lead_initials + str(last4_budget) + location

    #Calculate ultimate_synthesis: synthesis_rating × (success_probability ÷ 10) × (stakeholders ÷ 5) × complexity_score
    ultimate_synthesis =  synthesis_rating * (success_probability / 10) * (stakeholders / 5) * complexity_score

    # org in caps , proj
    caps_org=organization.upper() 
    

    #return f string 
    return f"SYNTHESIS: {caps_org} | PROJECT: {project_type} | LEAD: {team_lead} | EFFICIENCY: {budget_efficiency:0.1f} | VALUE: {risk_adjusted_value:0.1f} | VELOCITY: {project_velocity:0.2f} | RATING: {synthesis_rating:0.1f} | ID: {master_identifier} | ULTIMATE: {ultimate_synthesis:0.1f}"

# calling main 
main ()
