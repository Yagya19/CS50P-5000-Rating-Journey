"""
PROBLEM 23: Advanced Financial Analyzer
Task: Write a function called financial_analyzer that processes complex financial data and generates comprehensive investment reports.
Requirements:
Function name: financial_analyzer
  result1 = financial_analyzer("John Smith", 200000, 50000, 45, 7, 5)
  result2 = financial_analyzer("Mary Wilson", 300000, 90000, 35, 8, 10)
  result3 = financial_analyzer("Alex Brown", 250000, 50000, 40, 6, 15)
Takes 6 parameters: investor_name, portfolio_value, annual_income, age, risk_level, investment_years
Calculate investment_ratio: portfolio_value ÷ annual_income
Calculate age_factor: (100 - age) ÷ 10
Calculate risk_score: risk_level × age_factor × investment_ratio
Calculate projected_growth: portfolio_value × (1 + risk_level ÷ 100) × investment_years
Create investor_id: first3_name + age + risk_level + last2_investment_years
Calculate financial_rating: (risk_score + projected_growth ÷ 1000) ÷ 2
Return formatted string: "INVESTOR: NAME | RATIO: X.X | RISK: Y.Y | GROWTH: Z | ID: W | RATING: R.R"
Round ratio, risk, and rating to 1 decimal place
Expected Output:
INVESTOR: JOHN SMITH | RATIO: 4.0 | RISK: 280.0 | GROWTH: 1320000 | ID: Joh45705 | RATING: 800.0
INVESTOR: MARY WILSON | RATIO: 3.3 | RISK: 198.0 | GROWTH: 2160000 | ID: Mar35810 | RATING: 1179.0
INVESTOR: ALEX BROWN | RATIO: 5.0 | RISK: 375.0 | GROWTH: 1800000 | ID: Ale40615 | RATING: 1087.5
"""
def main(): #defined main 
    #  created 3 storing variables for calling function with inputs from 3 profiles ie 1 text & 5 numbers
    profile1 = financial_analyzer("John Smith", 200000, 50000, 45, 7, 5)
    profile2 = financial_analyzer("Mary Wilson", 300000, 90000, 35, 8, 10)
    profile3 = financial_analyzer("Alex Brown", 250000, 50000, 40, 6, 15)
    # print the item stored in each storing variable returned by calling function 
    print(profile1)
    print(profile2)
    print(profile3)
    
# defined calling function with 6 temporary storing variables
def financial_analyzer(investor_name, portfolio_value, annual_income, age, risk_level, investment_years):
    # imporatnt 4 formulas
    investment_ratio = portfolio_value / annual_income
    age_factor= (100 - age) / 10
    risk_score= risk_level * age_factor * investment_ratio
    projected_growth= portfolio_value * (1 + risk_level / 100) * investment_years

    # formula for investor_id: first3_name + age + risk_level + last2_investment_years 
    first,last=investor_name.split()
    first3_name = first[:3]
    investment_years_str=str(investment_years)
    last2_investment_years = investment_years_str[-2:]
    investor_id=first3_name + str(age) + str(risk_level) + last2_investment_years
    
    # calculate financial rating 
    financial_rating = (risk_score + projected_growth / 1000) / 2

    # name in caps
    NAME=investor_name.upper()

    #return the format string 
    return f"INVESTOR: {NAME} | RATIO: {investment_ratio:0.1f} | RISK: {risk_score:0.1f} | GROWTH: {projected_growth} | ID: {investor_id} | RATING: {financial_rating:0.1f}"

main()
