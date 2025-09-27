#PROBLEM 99 - MATRIX CALCULATION ENGINE (COMPREHENSIVE WEEK 0 TEST) 
def main():
    result1 = matrix_calculator("a1b2c3d4e", "sum", 4)
    result2 = matrix_calculator("x5y6z7w8q", "product", 1)
    result3 = matrix_calculator("m9n0p1q2r", "cross", 7)
    
    print(result1)
    print(result2)
    print(result3)

def matrix_calculator(grid_data, operation_mode, target_position):
   
    grid_list = list(grid_data) 
    Row1_list = [grid_list[0],grid_list[1],grid_list[2]]
    Row2_list = [grid_list[3],grid_list[4],grid_list[5]]
    Row3_list = [grid_list[6],grid_list[7],grid_list[8]]

    #Extract Values:

    #Count numeric digits (0-9) at each position: pos0_digits, pos1_digits, etc.

    #Calculate total_digits = sum of all position digit counts
    total_digits = grid_data.count("0") + grid_data.count("1") + grid_data.count("2") + grid_data.count("3") + grid_data.count("4")+grid_data.count("5") + grid_data.count("6") + grid_data.count("7") + grid_data.count("8")+grid_data.count("9")
    
    pos0_digits = int(grid_list[0]) * (grid_list[0].isdigit() == True) 
    pos1_digits = int(grid_list[1]) * (grid_list[1].isdigit() == True)
    pos2_digits = int(grid_list[2]) * (grid_list[2].isdigit() == True)
    pos3_digits = int(grid_list[3]) * (grid_list[3].isdigit() == True)
    pos4_digits = int(grid_list[4]) * (grid_list[4].isdigit() == True)
    pos5_digits = int(grid_list[5]) * (grid_list[5].isdigit() == True)
    pos6_digits = int(grid_list[6]) * (grid_list[6].isdigit() == True)
    pos7_digits = int(grid_list[7]) * (grid_list[7].isdigit() == True)
    pos8_digits = int(grid_list[8]) * (grid_list[8].isdigit() == True)

    grid_checksum = pos0_digits*1 + pos1_digits*2 + pos2_digits*3 + pos3_digits*4 + pos4_digits*5 + pos5_digits*6 + pos6_digits*7 + pos7_digits*8 + pos8_digits*9


    result_value =  (
                        ((pos0_digits + pos4_digits + pos8_digits) + (pos2_digits + pos4_digits + pos6_digits)) * (operation_mode == "sum")
                        + ((pos0_digits + 1) * (pos4_digits + 1) * (pos8_digits + 1)) * (operation_mode == "product")
                        + ((pos1_digits + pos3_digits + pos5_digits + pos7_digits) * 2) * (operation_mode == "cross")
                    )


    adjustment_factor = 1.0*(target_position == 0) + 1.25*(target_position == 1) + 1.5*(target_position == 2) + (2.0 - (target_position * 0.1))*(3<=target_position<=8)

    adjusted_result = result_value * adjustment_factor
    matrix_score = adjusted_result + grid_checksum
    efficiency_ratio = matrix_score / (total_digits + 1)

    category = "OPTIMAL"*(matrix_score >= 100) + "EFFICIENT"*(50 <= matrix_score < 100) +  "BASIC"*(matrix_score < 50) 


    Performance_Level =  "HIGH"*(efficiency_ratio >= 20) + "MEDIUM"*(10 <= efficiency_ratio < 20) + "LOW"*(efficiency_ratio < 10)

    return f"{category}:{Performance_Level}:{matrix_score:.1f}:{efficiency_ratio:.2f}:{adjusted_result:.1f}:{grid_checksum}:{total_digits}"

main()

