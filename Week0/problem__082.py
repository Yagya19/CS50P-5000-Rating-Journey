#PROBLEM 82 - TEXT PATTERN CLASSIFIER (COMPLETE CHALLENGE FORMAT) 
def main():
    result1 = text_classifier("sentiment", "positive#feedback@good%review", 2, 3, 1)
    result2 = text_classifier("topic", "science@research#data%analysis", 1, 2, 2)
    result3 = text_classifier("language", "english%text@sample#classify", 3, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def text_classifier(classification_type, text_sample, pattern_sensitivity, classification_depth, precision_level):
    #Step 1: Count Text Pattern Elements

    #sample_length: Count total characters in text_sample
    sample_length = len(text_sample)
    #alphabetic_patterns: Count letter characters (a-z, A-Z) in text_sample
    alphabetic_patterns = ( text_sample.count("a") + text_sample.count("b") + text_sample.count("c") +\
                            text_sample.count("d") + text_sample.count("e") + text_sample.count("f") +\
                            text_sample.count("g") + text_sample.count("h") + text_sample.count("i") +\
                            text_sample.count("j") + text_sample.count("k") + text_sample.count("l") +\
                            text_sample.count("m") + text_sample.count("n") + text_sample.count("o") +\
                            text_sample.count("p") + text_sample.count("q") + text_sample.count("r") +\
                            text_sample.count("s") + text_sample.count("t") + text_sample.count("u") +\
                            text_sample.count("v") + text_sample.count("w") + text_sample.count("x") +\
                            text_sample.count("y") + text_sample.count("z") + text_sample.count("A") + \
                            text_sample.count("B") + text_sample.count("C") +\
                            text_sample.count("D") + text_sample.count("E") + text_sample.count("F") +\
                            text_sample.count("G") + text_sample.count("H") + text_sample.count("I") +\
                            text_sample.count("J") + text_sample.count("K") + text_sample.count("L") +\
                            text_sample.count("M") + text_sample.count("N") + text_sample.count("O") +\
                            text_sample.count("P") + text_sample.count("Q") + text_sample.count("R") +\
                            text_sample.count("S") + text_sample.count("T") + text_sample.count("U") +\
                            text_sample.count("V") + text_sample.count("W") + text_sample.count("X") +\
                            text_sample.count("Y") + text_sample.count("Z") )

    #classification_markers: Count classification indicator characters ("#", "@", "%") in text_sample
    classification_markers =  text_sample.count("#") + text_sample.count("@") + text_sample.count("%")

    #MATHEMATICAL FORMULAS (COMPLETE):
    Text_Classification_Complexity_Score =(sample_length * 15) + (alphabetic_patterns * 30) + (classification_markers * 60)
    Classification_Multiplier = 5.4*(classification_type=="sentiment")+ 4.9*(classification_type=="topic")+ 4.3*(classification_type=="language")
    Pattern_Analysis_Projection = Text_Classification_Complexity_Score * Classification_Multiplier  * classification_depth
    Raw_Classification_Accuracy_Index = Pattern_Analysis_Projection - (pattern_sensitivity * 170)
    Classification_Accuracy_Index = Raw_Classification_Accuracy_Index *(Raw_Classification_Accuracy_Index >=340)+340*(Raw_Classification_Accuracy_Index <340)
    Text_Pattern_Density_Ratio = alphabetic_patterns / (sample_length +(sample_length==0)) *( sample_length!=0) + 1.6*(sample_length==0)
    Recognition_Precision = (Text_Pattern_Density_Ratio * 100) + (classification_depth * 85)
    Classification_Type_Complexity = 9*(classification_type=="sentiment")+ 11*(classification_type=="topic")+ 7*(classification_type=="language")
    Accuracy_Categories = "Highly_Accurate"*(Classification_Accuracy_Index>=850) + "Moderately_Accurate"*(620<=Classification_Accuracy_Index<850) + "Low_Accuracy"*(Classification_Accuracy_Index<620) 
    Depth_Categories = "Comprehensive_Classification"*(classification_depth == 3)+"Standard_Classification"*(classification_depth == 2) + "Basic_Classification"*(classification_depth == 1)
    Pattern_Distinctiveness = (classification_markers * 160) / (alphabetic_patterns + (alphabetic_patterns ==0)) * (alphabetic_patterns!=0) + 180*(alphabetic_patterns==0)
    Classification_Signature = classification_type + str(classification_depth) + str(pattern_sensitivity) + Accuracy_Categories 

    return f"CLASSIFIED: {Depth_Categories} | TYPE: {classification_type} | LENGTH: {sample_length} | PATTERNS: {alphabetic_patterns} | MARKERS: {classification_markers} | INDEX: {Classification_Accuracy_Index:.1f} | PRECISION: {Recognition_Precision :.1f}% | DENSITY: {Text_Pattern_Density_Ratio:.3f} | DISTINCTIVENESS: {Pattern_Distinctiveness:.1f}% | CATEGORY: {Accuracy_Categories} | COMPLEXITY: {Classification_Type_Complexity} | SIG: {Classification_Signature }"

main()
