#PROBLEM 85 - IMAGE PATTERN RECOGNITION ENGINE (COMPLETE CHALLENGE FORMAT)
def main():
    result1 = image_pattern_recognizer("edge", "pixels123│border456─corner┼detect", 2, 3, 1)
    result2 = image_pattern_recognizer("shape", "contour248│outline567─boundary", 1, 2, 2)
    result3 = image_pattern_recognizer("texture", "surface135─pattern┼fabric", 3, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def image_pattern_recognizer(recognition_mode, image_data, feature_threshold, processing_layers, precision_level):

    #Step 1: Count Image Pattern Elements
    #pixel_matrix: Count total characters in image_data
    pixel_matrix = len(image_data)
    #feature_points: Count digit characters (0-9) in image_data
    feature_points = image_data.count("0")+image_data.count("1")+image_data.count("2")+image_data.count("3")+image_data.count("4")+image_data.count("5")+image_data.count("6")+image_data.count("7")+image_data.count("8")+image_data.count("9")
    #edge_markers: Count edge detection characters ("│", "─", "┼") in image_data
    edge_markers = image_data.count("│")+image_data.count("─")+image_data.count("┼")
    Image_Processing_Complexity_Score = (pixel_matrix * 18) + (feature_points * 36) + (edge_markers * 75)
    Recognition_Multiplier = 6.3*(recognition_mode=="edge") + 5.8*(recognition_mode=="shape") + 5.4*(recognition_mode=="texture")  
    Pattern_Analysis_Projection =  Image_Processing_Complexity_Score * Recognition_Multiplier * processing_layers
    Raw_Visual_Recognition_Index = Pattern_Analysis_Projection- (feature_threshold * 200)
    Visual_Recognition_Index = Raw_Visual_Recognition_Index*(Raw_Visual_Recognition_Index>=400) + 400*(Raw_Visual_Recognition_Index<400)
    Feature_Density_Ratio = feature_points / (pixel_matrix + (pixel_matrix == 0)) * (pixel_matrix != 0) + 1.9*(pixel_matrix == 0)
    Processing_Accuracy = (Feature_Density_Ratio  * 100) + (processing_layers * 100)
    Recognition_Mode_Complexity = 8*(recognition_mode=="edge") + 10*(recognition_mode=="shape") + 12*(recognition_mode=="texture")
    Recognition_Categories = "Sharp_Recognition"*(Visual_Recognition_Index>=1000) + "Clear_Recognition"*(740<=Visual_Recognition_Index<1000) + "Blurry_Recognition"*(Visual_Recognition_Index<740)
    Processing_Categories = "Multi_Layer_Processing"*(processing_layers == 3) +  "Dual_Layer_Processing"*(processing_layers == 2) +  "Single_Layer_Processing"*(processing_layers == 1) 
    Edge_Definition_Quality = (edge_markers * 190) / (feature_points+(feature_points==0)) * (feature_points!=0) + 210*(feature_points==0)
    Recognition_Signature = recognition_mode + str(processing_layers) + str(feature_threshold) + Recognition_Categories

    return f"RECOGNIZED: {Processing_Categories} | MODE: {recognition_mode} | MATRIX: {pixel_matrix} | FEATURES: {feature_points} | EDGES: {edge_markers} | INDEX: {Visual_Recognition_Index:.1f} | ACCURACY: {Processing_Accuracy:.1f}% | DENSITY: {Feature_Density_Ratio:.3f} | DEFINITION: {Edge_Definition_Quality:.1f}% | CATEGORY: {Recognition_Categories} | COMPLEXITY: {Recognition_Mode_Complexity} | SIG: {Recognition_Signature}"

main()
