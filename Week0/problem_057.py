# define main func
def main():
    result1 = optimization_engine("minimize", 100.0, 50.0, 80, 2)
    result2 = optimization_engine("maximize", 200.0, 500.0, 120, 3)
    result3 = optimization_engine("balance", 150.0, 300.0, 60, 2)
    
    print(result1)
    print(result2)
    print(result3)

# define calling func with paramters 
def optimization_engine(optimization_type, target_value, constraint_limit, iteration_count, precision_level):
    # > Calculate optimal solutions based on optimization_type
    # > Compute optimization metrics and performance analysis
    # > Generate comprehensive optimization summary

    # Minimize (optimization_type = "minimize") All values calculation :
    initial_guess = target_value
    step_reduction = target_value / iteration_count

    # Maximize (optimization_type = "maximize") All values calculation :
    initial_value = target_value * 0.8
    growth_factor = constraint_limit / iteration_count

    # Balance (optimization_type = "balance"): All values calculation : 
    balance_point = (target_value + constraint_limit) / 2
    adjustment_factor = abs(target_value - constraint_limit) / iteration_count

    # get net optmz value & convergence_rate as per conditions 
    optimized_value = ((initial_guess) - (step_reduction * iteration_count * 0.5))*(optimization_type == "minimize") +  (initial_value + (growth_factor * iteration_count * 0.6))*(optimization_type == "maximize") + (balance_point + (adjustment_factor * 0.3))*(optimization_type == "balance")
    convergence_rate = abs(target_value - optimized_value) / target_value * (optimization_type == "minimize") + abs(optimized_value - constraint_limit) / constraint_limit * (optimization_type == "maximize") + abs(optimized_value - balance_point) / balance_point*(optimization_type == "balance")

    optimization_efficiency = (1 - convergence_rate) * 100

    performance_complexity = 3*(optimization_type == "minimize") + 5*(optimization_type == "maximize") + 4*(optimization_type == "balance")

    algorithm_quality = "Excellent"*(iteration_count>=100) + "Good"*(50<=iteration_count<=99) + "Basic"*(iteration_count<50) 

    performance_analysis = "Optimal"* (optimization_efficiency >= 90) + "Efficient" * (70<= optimization_efficiency <=89 )+ "Moderate" *(optimization_efficiency<70)

    optimization_signature = optimization_type + str(iteration_count) + str(precision_level) + algorithm_quality 

    improvement_percentage = abs((optimized_value - target_value) / target_value * 100) 

    primary_result = optimized_value 

    # return f string 
    return f"OPTIMIZED: {performance_analysis} | TYPE: {optimization_type} | TARGET: {target_value:.1f} | CONSTRAINT: {constraint_limit:.1f} | ITERATIONS: {iteration_count} | RESULT: {primary_result:.{precision_level}f} | EFFICIENCY: {optimization_efficiency:.1f}% | CONVERGENCE: {convergence_rate:.3f} | IMPROVEMENT: {improvement_percentage:.1f}% | COMPLEXITY: {performance_complexity} | SIG: {optimization_signature}"

# call main
main()
