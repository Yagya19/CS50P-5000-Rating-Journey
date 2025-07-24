""" PROBLEM 51: Advanced Scientific Calculator Engine
Task: Write a function called scientific_calculator that creates an intelligent mathematical computation system capable of performing complex calculations with multiple operations and precision analysis.
Requirements:
Function name: scientific_calculator
result1 = scientific_calculator(12.5, 3.25, "basic", 4)
result2 = scientific_calculator(4.0, 3.0, "advanced", 3) 
result3 = scientific_calculator(8.0, 6.0, "scientific", 5)
Takes 4 parameters: num1, num2, operation_type, precision_level
Support operations: "basic" (add, subtract, multiply, divide), "advanced" (power, root, percentage), "scientific" (trigonometric approximations)
Calculate operation_result based on operation_type
Apply precision_rounding based on precision_level (1-5 decimal places)
Calculate computation_accuracy: measure how precise the result is
# Different operation types have different inherent accuracy
base_accuracy = 95.0 * (operation_type == "basic") + \
85.0 * (operation_type == "advanced") + \
75.0 * (operation_type == "scientific")
# Adjust slightly based on precision level
computation_accuracy = base_accuracy + (precision_level * 2)
Calculate efficiency_score: operation complexity × precision level
Generate error_tolerance: acceptable margin of error for the operation
tolerance_rate = 0.001 * (operation_type == "basic") + \
0.01 * (operation_type == "advanced") + \
0.01 * (operation_type == "scientific")
error_tolerance = operation_result * tolerance_rate
Create calculation_signature: operation_type + precision_level + accuracy_grade
Return formatted string: "CALCULATED: R.RRRR | OPERATION: [operation_type] | PRECISION: P decimals | ACCURACY: A.A% | EFFICIENCY: E.E | TOLERANCE: T.TTTTT | SIG: SIGNATURE"
Round all metrics according to precision_level
# Different operation types have different inherent accuracy
base_accuracy = 95.0 * (operation_type == "basic") + \
85.0 * (operation_type == "advanced") + \
75.0 * (operation_type == "scientific")
Operation Rules:
# Simple complexity scoring
operation_complexity = 
3 * (operation_type == "basic") + \
5 * (operation_type == "advanced") + \
7 * (operation_type == "scientific")
Basic: +, -, ×, ÷ (use num1 + num2, num1 - num2, num1 × num2, num1 ÷ num2)
Advanced: Power (num1^num2), Root (num1^(1/num2)), Percentage (num1% of num2)
Scientific: Simple approximations (sine ≈ num1/100, cosine ≈ num2/100)
Accuracy grade: "High" (≥95%), "Good" (80-94%), "Fair" (<80%)
CALCULATED: 15.7500 | OPERATION: basic | PRECISION: 4 decimals | ACCURACY: 98.5% | EFFICIENCY: 16.2 | TOLERANCE: 0.0157 | SIG: basic4High
CALCULATED: 64.000 | OPERATION: advanced | PRECISION: 3 decimals | ACCURACY: 92.1% | EFFICIENCY: 23.8 | TOLERANCE: 0.640 | SIG: advanced3Good
CALCULATED: 0.08000 | OPERATION: scientific | PRECISION: 5 decimals | ACCURACY: 85.7% | EFFICIENCY: 34.3 | TOLERANCE: 0.00080 | SIG: scientific5Good """

# def main
def main():
    # seet storing variables for calling func 
    result1 = scientific_calculator(12.5, 3.25, "basic", 4)
    result2 = scientific_calculator(4.0, 3.0, "advanced", 3) 
    result3 = scientific_calculator(8.0, 6.0, "scientific", 5)

    # print items stored in stroing variables 
    print(result1)
    print(result2)
    print(result3)

# calling def with parameters 
def scientific_calculator(num1, num2, operation_type, precision_level):
    # get operation result based on ops type 
    # if op type is basic
    add = num1 + num2
    subtract = num1 - num2
    multiply = num1 * num2
    divide = num1 / num2
   
    # if op type is advanced
    power = num1**num2
    root = num1**(1/num2)
    percentage = (num1 / num2)*100
   
    # if op type is scientific
    sine = num1/100
    cosine = num2/100
    operation_result = (add + subtract + multiply + divide)*(operation_type=="basic") + (power + root + percentage)*(operation_type=="advanced") + (sine + cosine)*(operation_type=="scientific")
    # imp calcylations 
    base_accuracy = (95.0) * (operation_type == "basic") + (85.0) * (operation_type == "advanced") + (75.0) * (operation_type == "scientific")
    # Adjust slightly based on precision level
    computation_accuracy = base_accuracy + (precision_level * 2)
    operation_complexity = 3 * (operation_type == "basic") + 5 * (operation_type == "advanced") + 7 * (operation_type == "scientific")
    efficiency_score = operation_complexity * precision_level
    # generate error tolerence : 
    tolerance_rate = 0.001 * (operation_type == "basic") + 0.01 * (operation_type == "advanced") + 0.01 * (operation_type == "scientific")
    error_tolerance = operation_result * tolerance_rate
    # Create calculation_signature: operation_type + precision_level + accuracy_grade
    accuracy_grade = "High" * (computation_accuracy>=95) + "Good" * (80<computation_accuracy<94) + "Fair"*(computation_accuracy<80)
    calculation_signature = operation_type + str(precision_level) + accuracy_grade

    # return f string 
    return f"CALCULATED: {operation_result :0.{precision_level}f} | OPERATION: {operation_type} | PRECISION: {precision_level} decimals | ACCURACY: {computation_accuracy:0.1f}% | EFFICIENCY: {efficiency_score:0.1f} | TOLERANCE: {error_tolerance:0.5f} | SIG: {calculation_signature}"

# call main
main()
