# define main 
def main():
    # set storing variables for calling func 
    result1 = financial_calculator("investment", 10000.0, 8.5, 5, 2)
    result2 = financial_calculator("loan", 25000.0, 6.0, 10, 2)
    result3 = financial_calculator("savings", 5000.0, 3.0, 4, 2)
    
    # print item kept in storing varibales
    print(result1)
    print(result2)
    print(result3)

# define calling func with parameters 
def  financial_calculator(calculation_type, principal, rate, time_period, precision_level):
    # Investment (calculation_type = "investment"):# Investment growth calculations
    simple_interest = principal * (rate / 100) * time_period
    compound_interest = principal * ((1 + rate/100) ** time_period) - principal
    final_amount = principal + compound_interest 

    # Loan payment calculations
    monthly_rate = (rate / 100) / 12
    total_months = time_period * 12
    monthly_payment = (principal * monthly_rate * ((1 + monthly_rate) ** total_months)) / (((1 + monthly_rate) ** total_months) - 1)
    total_payment = monthly_payment * total_months
    total_interest = total_payment - principal 

    # Savings growth calculations
    annual_growth = principal * (rate / 100)
    total_growth = annual_growth * time_period
    savings_balance = principal + total_growth

    # Investment efficiency (return on investment percentage)
    investment_efficiency = (compound_interest / principal) * 100 * (calculation_type == "investment") + (total_interest / principal) * 100 * (calculation_type == "loan") + (total_growth / principal) * 100 * (calculation_type == "savings")

    # Financial complexity rating
    financial_complexity = 3 * (calculation_type == "investment") + 5 * (calculation_type == "loan") + 2 * (calculation_type == "savings")

    # Complexity grade
    complexity_grade = "Simple" * (financial_complexity <= 2) + "Moderate" * (financial_complexity == 3) + "Complex" * (financial_complexity >= 5)

    # Financial analysis
    financial_analysis = "High_Return" * (investment_efficiency > 50) + "Good_Return" * (20 <= investment_efficiency <= 50) + "Low_Return" * (investment_efficiency < 20)

    # Financial signature
    financial_signature = calculation_type + str(int(principal/1000)) + str(precision_level) + complexity_grade 

    # Primary result depends on calculation type
    primary_result = final_amount * (calculation_type == "investment") +  monthly_payment * (calculation_type == "loan") + savings_balance * (calculation_type == "savings")

    # return f string 
    return f"FINANCIAL: {financial_analysis} | TYPE: {calculation_type} | PRINCIPAL: ${principal:.0f} | RATE: {rate:.1f}% | YEARS: {time_period} | PRIMARY: ${primary_result:.{precision_level}f} | EFFICIENCY: {investment_efficiency:.1f}% | COMPLEXITY: {financial_complexity} | SIG: {financial_signature}"
    
# call main
main()
