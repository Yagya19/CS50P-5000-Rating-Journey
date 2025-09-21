# PROBLEM 67 - QUALITY ASSESSMENT ENGINE (COMPLETE CHALLENGE FORMAT)
def main():
    result1 = quality_assessor("product", "GOOD Quality Test!", 2, 3, 1)
    result2 = quality_assessor("service", "Excellent SERVICE provided", 1, 2, 2)
    result3 = quality_assessor("process", "Standard PROCESS workflow", 3, 1, 1)

    print(result1)
    print(result2)
    print(result3)

def quality_assessor(assessment_type, input_sample, quality_standard, inspection_level, precision_level):
    #Step 1: Count Quality Elements
    #sample_size: Count total characters in input_sample
    no_space_inputs = input_sample.replace(" ","")
    sample_size = len(no_space_inputs) 

    #quality_indicators: Count uppercase letters (A-Z) in input_sample
    quality_indicators = input_sample.count("A") + input_sample.count("B") + input_sample.count("C") + \
                        input_sample.count("D") + input_sample.count("E") + input_sample.count("F") + \
                        input_sample.count("G") + input_sample.count("H") + input_sample.count("I") + \
                        input_sample.count("J") + input_sample.count("K") + input_sample.count("L") + \
                        input_sample.count("M") + input_sample.count("N") + input_sample.count("O") + \
                        input_sample.count("P") + input_sample.count("Q") + input_sample.count("R") + \
                        input_sample.count("S") + input_sample.count("T") + input_sample.count("U") + \
                        input_sample.count("V") + input_sample.count("W") + input_sample.count("X") + \
                        input_sample.count("Y") + input_sample.count("Z")

    #defect_markers: Count special characters (!@#$%^&*) in input_sample
    defect_markers = input_sample.count("!") + input_sample.count("@") + input_sample.count("#") + \
                    input_sample.count("$") + input_sample.count("%") + input_sample.count("^") + \
                    input_sample.count("&") + input_sample.count("*") + input_sample.count(")") 
    
    # Formulas 
    Quality_Base_Score= (sample_size * 3) + (quality_indicators * 7) + (defect_markers * (-2))
    Quality_Multiplier = 1.5*(assessment_type=="product") + 1.3*(assessment_type=="service") + 1.7*(assessment_type=="process") 
    Assessment_Rating = Quality_Base_Score * Quality_Multiplier * inspection_level
    Raw_Quality_Index = Assessment_Rating - (quality_standard * 40)
    Quality_Index = Raw_Quality_Index*(Raw_Quality_Index>80) + 80*(Raw_Quality_Index<80)
    Defect_Ratio = (defect_markers / sample_size)*(sample_size!=0) + 0.25*(sample_size==0)
    Quality_Reliability = (quality_indicators / sample_size) * 100 * (sample_size != 0) + (inspection_level * 18)*(sample_size == 0)
    Assessment_Type_Complexity =  6*(assessment_type=="product") + 4*(assessment_type=="service") + 8*(assessment_type=="process") 
    Quality_Categories = "Premium" * (Quality_Index >= 200) + "Standard" * (130<Quality_Index<200) + "Poor" * (Quality_Index<130) 
    Inspection_Categories = "Rigorous_Inspection"*(inspection_level == 3) + "Normal_Inspection"*(inspection_level == 2) + "Basic_Inspection"*(inspection_level == 1)
    Quality_Performance =  (quality_indicators*30)/(defect_markers + (defect_markers==0))*(defect_markers!=0) + 90*(defect_markers == 0)
    Assessment_Signature = assessment_type + str(inspection_level) + str(quality_standard) +  Quality_Categories

    return f"ASSESSED: {Inspection_Categories} | TYPE: {assessment_type} | SIZE: {sample_size} | INDICATORS: {quality_indicators} | DEFECTS: {defect_markers} | INDEX: { Quality_Index:.1f} | RELIABILITY: {Quality_Reliability:.1f}% | RATIO: {Defect_Ratio:.3f} | PERFORMANCE: {Quality_Performance:.1f}% | CATEGORY: {Quality_Categories} | COMPLEXITY: {Assessment_Type_Complexity} | SIG: {Assessment_Signature}"

main()
