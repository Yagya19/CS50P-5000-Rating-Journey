"""PROBLEM 53: Complete Geometric Calculator
Task: Write a function called geometric_calculator that calculates areas, perimeters, and geometric properties for different shapes.
Requirements:
result1 = geometric_calculator("rectangle", 10.0, 5.0, 2)
result2 = geometric_calculator("circle", 5.0, 0.0, 3)  
result3 = geometric_calculator("triangle", 6.0, 5.0, 1)
Function name: geometric_calculator
Takes 4 parameters: shape_type, dimension1, dimension2, precision_level
Shape Calculations (COMPLETE FORMULAS):

Rectangle (shape_type = "rectangle"):
area = dimension1 * dimension2
perimeter = 2 * (dimension1 + dimension2)

Circle (shape_type = "circle"):
python# dimension1 = radius, dimension2 = ignored
area = 3.14159 * dimension1 * dimension1
perimeter = 2 * 3.14159 * dimension1

Triangle (shape_type = "triangle"):
python# dimension1 = base, dimension2 = height
area = 0.5 * dimension1 * dimension2
perimeter = dimension1 + dimension2 + ((dimension1**2 + dimension2**2)**0.5)  # Approximate

Additional Calculations:
python# Shape efficiency
shape_efficiency = area / perimeter
# Geometric complexity (fixed values)
geometric_complexity = 2 * (shape_type == "rectangle") + \
    4 * (shape_type == "circle") + \
    3 * (shape_type == "triangle")

    # Complexity rating
    complexity_rating = "Simple" * (geometric_complexity <= 2) + \
    "Medium" * (geometric_complexity == 3) + \
    "Complex" * (geometric_complexity >= 4)

    # Shape analysis
    shape_analysis = "Regular" * (shape_efficiency > 5) + \
    "Balanced" * (2 <= shape_efficiency <= 5) + \
    "Extended" * (shape_efficiency < 2)

    # Geometric signature
    geometric_signature = shape_type + str(precision_level) + complexity_rating

Calculate area and perimeter for the specified shape
Compute shape_efficiency: area ÷ perimeter ratio
Generate geometric_complexity score based on shape type
Create shape_analysis summary 
return f"GEOMETRY: {shape_analysis} | SHAPE: {shape_type} | AREA: {area:.{precision_level}f} | PERIMETER: {perimeter:.{precision_level}f} | EFFICIENCY: {shape_efficiency:.2f} | COMPLEXITY: {geometric_complexity} | SIG: {geometric_signature}"
"""
# define main
def main():
    # set storing variables for calling func with inputs
    result1 = geometric_calculator("rectangle", 10.0, 5.0, 2)
    result2 = geometric_calculator("circle", 5.0, 0.0, 3)  
    result3 = geometric_calculator("triangle", 6.0, 5.0, 1) 

    # set print 
    print(result1)
    print(result2) 
    print(result3)

# define calling func with parameters
def geometric_calculator(shape_type, dimension1, dimension2, precision_level):
    # area and parameter for each shape 
    area_rect = dimension1 * dimension2
    area_circle =  3.14159 * dimension1 **2
    area_traingle =  0.5 * dimension1 * dimension2
    area = (area_rect)*(shape_type=="rectangle") + (area_circle)*(shape_type=="circle") + (area_traingle)*(shape_type=="triangle") 

    # parameter for each shape 
    pmt_rect = 2 * (dimension1 + dimension2)
    pmt_circle = 2 * 3.14159 * dimension1
    pmt_traingle = dimension1 + dimension2 + ((dimension1**2 + dimension2**2)**0.5)

    perimeter = (pmt_rect)*(shape_type=="rectangle") + (pmt_circle)*(shape_type=="circle") + (pmt_traingle)*(shape_type=="triangle") 

    # shape efficency calculations
    shape_efficiency = area / perimeter

    # geometric complexity calculations 
    geometric_complexity = 2 * (shape_type == "rectangle") +  4 * (shape_type == "circle") +  3 * (shape_type == "triangle")

    # Complexity rating
    complexity_rating = "Simple" * (geometric_complexity <= 2) +  "Medium" * (geometric_complexity == 3) + "Complex" * (geometric_complexity >= 4)

    # Shape analysis
    shape_analysis = "Regular" * (shape_efficiency > 5) +  "Balanced" * (2 <= shape_efficiency <= 5) + "Extended" * (shape_efficiency < 2)

    #  Geometric signature
    geometric_signature = shape_type + str(precision_level) + complexity_rating 

    # return f string 
    return f"GEOMETRY: {shape_analysis} | SHAPE: {shape_type} | AREA: {area:0.{precision_level}f} | PERIMETER: {perimeter:0.{precision_level}f} | EFFICIENCY: {shape_efficiency:.2f} | COMPLEXITY: {geometric_complexity} | SIG: {geometric_signature}"

# call main
main()
