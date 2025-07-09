"""
PROBLEM 22: Enterprise Data Processor
Task: Write a function called process_enterprise_data that analyzes complex business data and generates comprehensive reports.
Requirements:
Function name: process_enterprise_data
result1 = process_enterprise_data("TechCorp", 7500000, 50, 2010, "New York")
result2 = process_enterprise_data("Innovate Inc", 8000000, 40, 2017, "California")
result3 = process_enterprise_data("Global Solutions", 10000000, 80, 2000, "Texas")
Takes 5 parameters: company_name, revenue, employees, founded_year, location
Calculate company_age: 2025 - founded_year---Done
Calculate revenue_per_employee: revenue ÷ employees---Done
Calculate growth_factor: (revenue ÷ 1000000) × (employees ÷ 100) × company_age-----Done
Extract location_code: first2_letters + last2_letters of location---------------------Done
Create enterprise_id: first3_company + employees + founded_year + location_code---------Done
Calculate efficiency_score: (revenue_per_employee × growth_factor) ÷ 1000
Return formatted string: "ENTERPRISE: COMPANY | AGE: X | RPE: Y.Y | GROWTH: Z.Z | ID: W | SCORE: S.S"
Round RPE, growth, and score to 1 decimal place
ENTERPRISE: TECHCORP | AGE: 15 | RPE: 150000.0 | GROWTH: 75.0 | ID: TEC50020010NY | SCORE: 11250.0
ENTERPRISE: INNOVATE INC | AGE: 8 | RPE: 200000.0 | GROWTH: 32.0 | ID: INN40201717CA | SCORE: 6400.0
ENTERPRISE: GLOBAL SOLUTIONS | AGE: 25 | RPE: 125000.0 | GROWTH: 187.5 | ID: GLO80020000TX | SCORE: 23437.5
"""
def main(): #defined main 
    # assign storing value to calling func./ 5inputs : "Text",Nos
    result1 = process_enterprise_data("TechCorp", 7500000, 50, 2010, "New York")
    result2 = process_enterprise_data("Innovate Inc", 8000000, 40, 2017, "California")
    result3 = process_enterprise_data("Global Solutions", 10000000, 80, 2000, "Texas")
    # print the item stored in storing variable / item is returned by calling function 
    print(result1)
    print(result2)
    print(result3)

# def calling function & assign temp variable / 5 temp variables - v1,v2..v5
def process_enterprise_data(company_name, revenue, employees, founded_year, location): 
    # get company age 
    company_age = 2025 - founded_year
    # get  revenue_per_employee
    revenue_per_employee = revenue / employees
    # get growth_factor
    growth_factor = (revenue / 1000000) * (employees / 100) * company_age
    # get location code
    first2_letters = location[:2] # get first 2 letters
    last2_letters= location[-2:] # get last 2 letters
    location_code = (first2_letters + last2_letters).upper()
    #get enterprise_id = first3_company + employees + founded_year + location_code
    first3_company = company_name[:3] #get first 3 letteres of company name
    enterprise_id = first3_company + str(employees) + str(founded_year) + str(location_code)
    #get efficiency_score
    efficiency_score = (revenue_per_employee * growth_factor) / 1000
    # company in caps
    caps_company=company_name.upper()

    #return format string 
    return f"ENTERPRISE: {caps_company} | AGE: {company_age} | RPE: {revenue_per_employee:0.1f} | GROWTH: {growth_factor:0.1f} | ID: {enterprise_id} | SCORE: {efficiency_score:0.1f}"

main()





