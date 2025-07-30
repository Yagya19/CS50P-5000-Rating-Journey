# define main 

def main():
    result1 = numerical_methods("newton", 25.0, 10.0, 0.001, 2)
    result2 = numerical_methods("bisection", 16.0, 8.0, 0.010, 3)
    result3 = numerical_methods("secant", 30.0, 15.0, 0.100, 2)
    
    print(result1)
    print(result2)
    print(result3)


# define calling func with parameters 
def numerical_methods(method_type, target_function, initial_value, tolerance_level, precision_level):
    # Calculate numerical approximations based on method_type
    #Compute convergence metrics and accuracy analysis
    #Generate numerical analysis summary
    # if Newton (method_type = "newton"): 
    iteration_1 = initial_value - (target_function / (2 * initial_value))
    iteration_2 = iteration_1 - (target_function / (2 * iteration_1))
    
    # if Bisection (method_type = "bisection"): 
    left_bound = initial_value * 0.5
    right_bound = initial_value * 1.5
    midpoint_1 = (left_bound + right_bound) / 2
    midpoint_2 = (left_bound + midpoint_1) / 2

    # if Secant (method_type = "secant"): 
    x0 = initial_value
    x1 = initial_value * 1.1
    x2 = x1 - (target_function * (x1 - x0)) / (target_function * 1.1 - target_function)

    # net values with conditional on types 
    final_approximation = (iteration_2 - (target_function / (2 * iteration_2)))*(method_type == "newton") + ((midpoint_1 + midpoint_2) / 2)*(method_type == "bisection")+(x2 - (target_function * (x2 - x1)) / (target_function * 1.1 - target_function))*(method_type == "secant")
    approximation_error = (abs(final_approximation - iteration_2))*(method_type == "newton") + (abs(right_bound - left_bound) / 4)*(method_type == "bisection")+(abs(final_approximation - x2))*(method_type == "secant")
    
    Convergence_Rate = approximation_error / tolerance_level

    Numerical_Accuracy = (1 -(approximation_error / abs(final_approximation))) * 100 * (final_approximation!=0) + 95*(final_approximation==0)

    Method_Complexity = 4*(method_type=="newton") + 2*(method_type == "bisection") + 3*(method_type == "secant")

    Convergence_Quality = "Excellent"*(Convergence_Rate<= 0.1) + "Good"*(0.1<Convergence_Rate<=0.5)+"Poor"*(Convergence_Rate>0.5) 

    Numerical_Analysis = "Highly_Accurate"*(Numerical_Accuracy>=95) + "Accurate"*(85<=Numerical_Accuracy<95) + "Approximate"*(Numerical_Accuracy<85) 

    Methods_Signature =  method_type + str(int(tolerance_level)) + str(precision_level) +  Convergence_Quality

    Improvement_Factor= abs(final_approximation - initial_value) / initial_value * 100 

    Primary_result = final_approximation 

    # return f string 
    return f"NUMERICAL: {Numerical_Analysis} | METHOD: {method_type} | INITIAL: {initial_value:.1f} | TARGET: {target_function:.1f} | TOLERANCE: {tolerance_level:.3f} | RESULT: {Primary_result:.{precision_level}f} | ACCURACY: {Numerical_Accuracy:.1f}% | CONVERGENCE: {Convergence_Rate:.3f} | ERROR: {approximation_error:.4f} | IMPROVEMENT: {Improvement_Factor:.1f}% | COMPLEXITY: {Method_Complexity} | SIG: {Methods_Signature}"

# Call main
main()
