#PROBLEM 98 - SEQUENCE PATTERN GENERATOR (COMPREHENSIVE WEEK 0 TEST)
def main():
    result1 = sequence_generator(123, "arithmetic", 5)
    result2 = sequence_generator(24, "geometric", 4)
    result3 = sequence_generator(789, "fibonacci", 6)
    
    print(result1)
    print(result2)
    print(result3)

def sequence_generator(seed_value, pattern_type, sequence_length):
    #Step 1: Seed Analysis

    #Calculate digit_sum = sum of all digits in seed_value
    list_seed = list(str(seed_value)) 
    pad_seed = ((list_seed) + ["0"]*5)[:5]
    digit_sum = int(pad_seed[0]) + int(pad_seed[1]) + int(pad_seed[2]) + int(pad_seed[3]) + int(pad_seed[4])

    #Calculate digit_product = product of all digits in seed_value (if seed_value has 0, treat as 1)
    digit_product = (int(pad_seed[0]) * int(pad_seed[1]) * int(pad_seed[2]) * int(pad_seed[3]) * int(pad_seed[4]))

    #Calculate seed_magnitude = number of digits in seed_value
    seed_magnitude = len(str(seed_value))

    #Step 2: Pattern-Specific Calculations
    #Arithmetic Pattern:

    step_value = (digit_sum + 3)*(pattern_type == "arithmetic")
    first_term = seed_value
    multiplier = ((digit_product % 5) + 2)*(pattern_type == "geometric")
    modifier = (digit_sum % 10)*(pattern_type == "fibonacci")
    next_term = (seed_value + step_value)*(pattern_type == "arithmetic") + (seed_value * multiplier)*((pattern_type == "geometric"))+(seed_value + modifier)*((pattern_type == "fibonacci"))

    sequence_sum =  next_term
    average_term = sequence_sum / seed_magnitude
    growth_factor = int(list_seed[-1]) / (int(list_seed[0]) + int((list_seed[0]==0))) * ( list_seed[0] !=0)  + 1*( list_seed[0]==0)   

    Sequence_Classification = "EXPLOSIVE"*(sequence_sum >= 10000) + "RAPID"*(1000 <= sequence_sum < 10000) + "MODERATE"*(100 <= sequence_sum < 1000) + "SLOW"*(sequence_sum < 100)


    Pattern_Strength = "STRONG"*(growth_factor >= 100) + "MEDIUM"*(10 <= growth_factor < 100) + "WEAK"*(growth_factor < 10)


    return f"{Sequence_Classification}:{Pattern_Strength}:{sequence_sum}:{average_term:.1f}:{growth_factor:.2f}:{digit_sum}:{pattern_type}"

main()
