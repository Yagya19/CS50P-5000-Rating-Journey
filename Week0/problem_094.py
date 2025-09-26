#PROBLEM 94 - LOGICAL DECISION ENGINE (COMPREHENSIVE WEEK 0 TEST)
def main():
    result1 = decision_engine("Test123GO", "high", 8)
    result2 = decision_engine("SAMPLE456data", "medium", 15)
    result3 = decision_engine("low789ABC", "low", 5)
    
    print(result1)
    print(result2)
    print(result3)

def decision_engine(input_sequence, rule_priority, threshold_value):
    #Step 1: Sequence Analysis

    #Count total characters in input_sequence
    sequence_length = len(input_sequence)

    #Count uppercase letters (A-Z) in input_sequence
    uppercase_count =  (
                        input_sequence.count("A") +
                        input_sequence.count("B") +
                        input_sequence.count("C") +
                        input_sequence.count("D") +
                        input_sequence.count("E") +
                        input_sequence.count("F") +
                        input_sequence.count("G") +
                        input_sequence.count("H") +
                        input_sequence.count("I") +
                        input_sequence.count("J") +
                        input_sequence.count("K") +
                        input_sequence.count("L") +
                        input_sequence.count("M") +
                        input_sequence.count("N") +
                        input_sequence.count("O") +
                        input_sequence.count("P") +
                        input_sequence.count("Q") +
                        input_sequence.count("R") +
                        input_sequence.count("S") +
                        input_sequence.count("T") +
                        input_sequence.count("U") +
                        input_sequence.count("V") +
                        input_sequence.count("W") +
                        input_sequence.count("X") +
                        input_sequence.count("Y") +
                        input_sequence.count("Z")
                        )
    #Count numeric digits (0-9) in input_sequence
    digit_count = (
                    input_sequence.count("0") +
                    input_sequence.count("1") +
                    input_sequence.count("2") +
                    input_sequence.count("3") +
                    input_sequence.count("4") +
                    input_sequence.count("5") +
                    input_sequence.count("6") +
                    input_sequence.count("7") +
                    input_sequence.count("8") +
                    input_sequence.count("9") 
                   )

    primary_score = ((uppercase_count*3) + (digit_count * 2))* int( sequence_length%2==0 and rule_priority == "high") + ((uppercase_count + digit_count) * 4)*int(sequence_length%2!=0 and rule_priority == "high")
    action_code = "EXECUTE"*(primary_score > threshold_value)* int( sequence_length%2==0 and rule_priority == "high") + "DELAY"*(primary_score <= threshold_value)* int( sequence_length%2==0 and rule_priority == "high") + "PROCESS"*(primary_score >= threshold_value) *int(sequence_length%2!=0 and rule_priority == "high")+ "REJECT"*(primary_score < threshold_value)*int(sequence_length%2!=0 and rule_priority == "high")



    secondary_score = (uppercase_count - digit_count)*(rule_priority == "medium")
    action_code = "APPROVE"*(rule_priority == "medium")*( secondary_score > 0) + "REVIEW"*(rule_priority == "medium")*(secondary_score <= 0)




    action_code = "NEUTRAL"*(uppercase_count == digit_count)*(rule_priority == "low") + "ADVANCE"*(uppercase_count > digit_count)*(rule_priority == "low") + "RETREAT"*(uppercase_count < digit_count)*(rule_priority == "low")

    action_code = "HALT"*(input_sequence == "STOP") + "RUSH"*(input_sequence == "GO")*(threshold_value<10) + "OVERFLOW"*(sequence_length > 20 )*(rule_priority != "low")



    return f"{action_code}|{sequence_length}|{uppercase_count}|{digit_count}|{rule_priority}|{threshold_value}"

main()
