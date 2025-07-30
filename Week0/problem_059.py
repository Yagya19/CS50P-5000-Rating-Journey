# define main 
def main():
    result1 = series_analyzer("arithmetic", 5.0, 3.0, 10, 2)
    result2 = series_analyzer("geometric", 2.0, 1.5, 8, 3)
    result3 = series_analyzer("harmonic", 1.0, 0.5, 5, 2)
    
    print(result1)
    print(result2)
    print(result3)

# define calling func with parameters 
def  series_analyzer(series_type, first_term, common_ratio, term_count, precision_level):
    # Calculate series properties based on series_type
    # Compute convergence analysis and summation metrics
    # Generate comprehensive series analysis summary 


    # If Arithmetic (series_type = "arithmetic"): 
    # Arithmetic series: a, a+d, a+2d, a+3d, ...
    common_difference = common_ratio  # Using common_ratio as difference for arithmetic
    

    # Geometric series: a, ar, ar^2, ar^3, ...


    # Harmonic Series 
    # Harmonic series: 1/a, 1/(a+d), 1/(a+2d), ...
    # Harmonic series manual calculation (first 5 terms max for Week 0)
    harmonic_difference = common_ratio
    term1 = 1 / first_term
    term2 = 1 / (first_term + harmonic_difference)
    term3 = 1 / (first_term + 2 * harmonic_difference)
    term4 = 1 / (first_term + 3 * harmonic_difference)
    term5 = 1 / (first_term + 4 * harmonic_difference)

    # net series sum and series average and n term with conditions 

    nth_term = (first_term + (term_count - 1) * common_difference)*(series_type == "arithmetic") + (first_term * (common_ratio ** (term_count - 1)))* (series_type == "geometric")+ (1 / (first_term + (term_count - 1) * harmonic_difference))*(series_type=="harmonic") 
    series_sum = ((term_count * (first_term + nth_term)) / 2)*(series_type == "arithmetic") + (first_term * (1 - (common_ratio ** term_count)) / (1 - common_ratio))*(series_type =="geometric")*(common_ratio != 1)+(first_term * term_count)*(series_type =="geometric")*(common_ratio == 1)+(term1 + term2 + term3 + term4 + term5)*(series_type=="harmonic")
    series_average = (series_sum / term_count)*(series_type == "arithmetic") + (series_sum / term_count)*(series_type =="geometric") +  (series_sum / 5 )*(series_type=="harmonic")
    

    Convergence_Rate = abs(nth_term - series_average) / series_average

    Series_Efficiency = (series_sum / (term_count * abs(first_term))) * 100 * (first_term!=0) + 50*(first_term==0) 

    Series_Complexity= 2*(series_type == "arithmetic") + 4*(series_type =="geometric") + 5*((series_type=="harmonic")) 

    Convergence_Quality = "Excellent"*(Convergence_Rate <= 0.2) + "Good"*(0.2<Convergence_Rate <= 0.8) + "Poor"*(Convergence_Rate > 0.8) 

    Series_Analysis = "Rapid_Growth"*(Series_Efficiency >= 200) + "Steady_Growth"*(100<=Series_Efficiency <=199) + "Slow_Growth"*(Series_Efficiency <100) 

    Series_Signature = series_type + str(term_count) + str(precision_level) + Convergence_Quality 

    Growth_Factor =  abs(nth_term - first_term) / abs(first_term) * 100 

    Primary_result = series_sum 

    # return f string 
    return f"SERIES: {Series_Analysis} | TYPE: {series_type} | FIRST: {first_term:.1f} | RATIO: {common_ratio:.1f} | TERMS: {term_count} | SUM: {Primary_result:.{precision_level}f} | AVERAGE: {series_average:.{precision_level}f} | NTH_TERM: {nth_term:.{precision_level}f} | EFFICIENCY: {Series_Efficiency:.1f}% | CONVERGENCE: {Convergence_Rate:.3f} | GROWTH: {Growth_Factor:.1f}% | COMPLEXITY: {Series_Complexity} | SIG: {Series_Signature}"

# Call main
main()
