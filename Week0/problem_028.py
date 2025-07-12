"""
PROBLEM 28: Advanced Intelligence Hub
Task: Write a function called intelligence_hub that creates a comprehensive intelligence processing system analyzing complex multi-faceted organizational data.
Requirements:
Function name: intelligence_hub
result1 = intelligence_hub("TechGlobal Corp", "Technology", "Sarah Johnson", 5000, 750000000, 12, 18, 7, 8, 25, 2010)
result2 = intelligence_hub("Innovate Systems", "Software", "Mike Chen", 2500, 500000000, 15, 9, 7, 6, 20, 2017)
result3 = intelligence_hub("Future Dynamics", "AI", "Lisa Wang", 3000, 500000000, 20, 12, 8, 9, 30, 2013)
Takes 11 parameters: company, sector, ceo_name, employees, revenue, growth_rate, market_share, innovation_score, sustainability_rating, global_presence, founding_year
Calculate company_age: 2025 - founding_year
Calculate revenue_per_employee: revenue ÷ employees
Calculate growth_momentum: (growth_rate × market_share × innovation_score) ÷ 100
Calculate sustainability_factor: sustainability_rating × global_presence ÷ 10
Calculate intelligence_quotient: (revenue_per_employee + growth_momentum + sustainability_factor) × company_age ÷ 1000
Calculate market_dominance: (market_share × innovation_score × sustainability_rating) ÷ (100 - growth_rate)
---------------------------------------------------------------------------------------------------------------------
Create intelligence_signature: first6_company + sector_length + ceo_initials + last3_revenue + founding_decade
Calculate hub_excellence: (intelligence_quotient + market_dominance) × (employees ÷ 1000) × (global_presence ÷ 10)
Return formatted string: "HUB: COMPANY | SECTOR: S | CEO: C | AGE: A | RPE: R.R | MOMENTUM: M.M | IQ: I.I | DOMINANCE: D.D | SIG: SIG | EXCELLENCE: E.E"
Round RPE, momentum, IQ, dominance, and excellence to 1 decimal place
HUB: TECHGLOBAL CORP | SECTOR: Technology | CEO: Sarah Johnson | AGE: 15 | RPE: 150000.0 | MOMENTUM: 504.0 | IQ: 113.6 | DOMINANCE: 420.0 | SIG: TechGl10SJ000202 | EXCELLENCE: 8016.0
HUB: INNOVATE SYSTEMS | SECTOR: Software | CEO: Mike Chen | AGE: 8 | RPE: 200000.0 | MOMENTUM: 378.0 | IQ: 62.4 | DOMINANCE: 315.0 | SIG: Innova8MC500201 | EXCELLENCE: 3014.4
HUB: FUTURE DYNAMICS | SECTOR: AI | CEO: Lisa Wang | AGE: 12 | RPE: 166666.7 | MOMENTUM: 720.0 | IQ: 106.4 | DOMINANCE: 600.0 | SIG: Future2LW200200 | EXCELLENCE: 8500.8 """

#def main 
def main():
    # create storing variable for storing return value of caling func with respective inputs 
    result1 = intelligence_hub("TechGlobal Corp", "Technology", "Sarah Johnson", 5000, 750000000, 12, 18, 7, 8, 25, 2010)
    result2 = intelligence_hub("Innovate Systems", "Software", "Mike Chen", 2500, 500000000, 15, 9, 7, 6, 20, 2017)
    result3 = intelligence_hub("Future Dynamics", "AI", "Lisa Wang", 3000, 500000000, 20, 12, 8, 9, 30, 2013)
    # print the items stored in storing variables 
    print(result1)
    print(result2)
    print(result3)

# def calling funct & assign their temp variables 
def intelligence_hub(company, sector, ceo_name, employees, revenue, growth_rate, market_share, innovation_score, sustainability_rating, global_presence, founding_year):
    # get all imp calculations
    company_age = 2025 - founding_year
    revenue_per_employee = revenue / employees
    growth_momentum = (growth_rate * market_share * innovation_score) / 100
    sustainability_factor = sustainability_rating * global_presence / 10
    intelligence_quotient = (revenue_per_employee + growth_momentum + sustainability_factor) * company_age / 1000
    market_dominance = (market_share * innovation_score * sustainability_rating) / (100 - growth_rate)
    # Create intelligence_signature: first6_company + str(sector_length) + ceo_initials + str(last3_revenue) + str(founding_decade)
    first,last=company.split()
    first6_company=first[:6]
    sector_length=len(sector)
    initial_first,initial_last= ceo_name.split()
    ceo_initials=initial_first[:1]+initial_last[:1]
    str_revenue=str(revenue)
    last3_revenue=str_revenue[-3:]
    str_founding = str(founding_year)
    founding_decade=str_founding[:3]
    intelligence_signature = first6_company + str(sector_length) + ceo_initials + str(last3_revenue) + str(founding_decade)
    # calculate hub excellence 
    hub_excellence = (intelligence_quotient + market_dominance) * (employees / 1000) * (global_presence / 10)
    # return f string 
    return f"HUB: {company.upper()} | SECTOR: {sector} | CEO: {ceo_name} | AGE: {company_age} | RPE: {revenue_per_employee:0.1f} | MOMENTUM: {growth_momentum:0.1f} | IQ: {intelligence_quotient:0.1f} | DOMINANCE: {market_dominance:0.1f} | SIG: {intelligence_signature} | EXCELLENCE: {hub_excellence:0.1f}"
# call main func
main()




