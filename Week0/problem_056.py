# define main
def main():
    # set storing variables for calling func carrying inputs
    result1 = function_analyzer("polynomial", 2.0, 3.0, 4.0, 2)
    result2 = function_analyzer("exponential", 3.0, 2.0, 5.0, 3)
    result3 = function_analyzer("logarithmic", 4.0, 1.5, 6.0, 2)
    
    # print item in storing variables 
    print(result1)
    print(result2)
    print(result3)

# define calling func with parameters 
def function_analyzer(function_type, coefficient, exponent, input_value, precision_level):
    #Calculate function values and mathematical properties based on function_type ; Compute function_complexity score ; Generate mathematical_analysis summary
    
    log_value = (exponent * input_value) / 10
    
    # all value conditionals 
    function_value = coefficient * (2.718 ** (exponent * input_value))*(function_type == "exponential") + coefficient * (input_value ** exponent)*(function_type == "polynomial") + coefficient * log_value *(function_type == "logarithmic")
    derivative_value = coefficient * exponent * (input_value ** (exponent - 1))*(function_type == "polynomial") + coefficient * exponent * (2.718 ** (exponent * input_value))*(function_type == "exponential") + coefficient / input_value *(function_type == "logarithmic")
    integral_approximation = (coefficient / (exponent + 1)) * (input_value ** (exponent + 1))*(function_type == "polynomial") +(coefficient / exponent) * (2.718 ** (exponent * input_value))*(function_type == "exponential") + (exponent * input_value) / 10 *(function_type == "logarithmic")+coefficient * (input_value * log_value - input_value)*(function_type == "logarithmic")


    #Additional Required Calculations: 
    # Function complexity rating
    function_complexity = 2 * (function_type == "polynomial") + 4 * (function_type == "exponential") + 3 * (function_type == "logarithmic")

    # Complexity grade
    complexity_grade = "Basic" * (function_complexity <= 2) + "Intermediate" * (function_complexity == 3) + "Advanced" * (function_complexity >= 4)

    # Function behavior analysis
    function_behavior = "Increasing" * (derivative_value > 0) + "Decreasing" * (derivative_value < 0) + "Constant" * (derivative_value == 0)

    # Mathematical analysis
    mathematical_analysis = "Rapid_Growth" * (abs(function_value) > 100) + "Moderate_Growth" * (10 <= abs(function_value) <= 100) + "Slow_Growth" * (abs(function_value) < 10)

    # Function signature
    function_signature = function_type + str(int(abs(coefficient))) + str(precision_level) + complexity_grade

    # Rate of change (absolute value of derivative)
    rate_of_change = abs(derivative_value)

    primary_result = function_value

    # return f string 
    return f"FUNCTION: {mathematical_analysis} | TYPE: {function_type} | COEFF: {coefficient:.1f} | EXP: {exponent:.1f} | INPUT: {input_value:.1f} | VALUE: {primary_result:.{precision_level}f} | DERIVATIVE: {derivative_value:.{precision_level}f} | INTEGRAL: {integral_approximation:.{precision_level}f} | BEHAVIOR: {function_behavior} | RATE: {rate_of_change:.2f} | COMPLEXITY: {function_complexity} | SIG: {function_signature}"


# call main
main()
