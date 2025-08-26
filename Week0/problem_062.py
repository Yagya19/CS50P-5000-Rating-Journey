def main():
    result1 = text_analyzer("email", "john@example.com meeting tomorrow", 2, 1, 1)
    result2 = text_analyzer("social", "Great day! #sunshine #happy @friends", 3, 2, 2)
    result3 = text_analyzer("article", "The quick brown fox jumps. It was amazing.", 1, 3, 1)
    
    print(result1)
    print(result2)
    print(result3)

def text_analyzer(text_type, content_string, analysis_depth, filter_level, precision_level): # created a func with 5 parameters for storing input values
    #Step 1: Count Basic Elements character_count: Count total characters in content_string (including spaces) & word_count: Count total words in content_string (words separated by spaces)
    character_count = len(content_string)
    words = content_string.split() 
    word_count = len(words) 

    #Step 2: Count Special Elements Based on Text Type
    """If text_type = "email": Count "@" symbols in content_string
    If text_type = "social": Count "#" symbols + "@" symbols in content_string
    If text_type = "article": Count sentence endings (".", "!", "?") in content_string"""

    Count_Special_Elements =  content_string.count("@")*(text_type=="email") + (content_string.count("#")+content_string.count("@"))*(text_type=="social") + (content_string.count(".")+content_string.count("!")+content_string.count("?"))*(text_type=="article")

    # Step 3 : All maths formulas 
    Content_Complexity_Score = (character_count / 10) + (word_count * 2) + (Count_Special_Elements * 5)
    unchecked_Text_Quality_Rating = ((Content_Complexity_Score * analysis_depth) - (filter_level * 15))
    Text_Quality_Rating = unchecked_Text_Quality_Rating * (unchecked_Text_Quality_Rating>=30) + 30*(unchecked_Text_Quality_Rating<30)

    # Processing Efficiency= meaningful_content_ratio × 100) + analysis_bonus
    Meaningful_content_ratio = Count_Special_Elements  / character_count
    Analysis_bonus = analysis_depth * 10
    Processing_Efficiency=  (Meaningful_content_ratio * 100) + Analysis_bonus

    Text_Type_Complexity = 3*(text_type=="email")+ 5*(text_type=="social")+4*(text_type=="article")

    Quality_Categories = "Premium"*(Text_Quality_Rating>=100)+ "Standard"*(70<=Text_Quality_Rating<=99)+"Basic"*(Text_Quality_Rating<70)
    Analysis_Categories = "Deep_Analysis"*(analysis_depth==3)+"Standard_Analysis"*(analysis_depth==2)+"Quick_Analysis"*(analysis_depth==1)

    Content_Density =(word_count / character_count) * 100 * (character_count!=0) + 20*(character_count==0) 

    Text_Signature = text_type + str(analysis_depth) + str(filter_level) + (Quality_Categories)

    return f"ANALYZED: {Analysis_Categories} | TYPE: {text_type} | CHARS: {character_count} | WORDS: {word_count} | ELEMENTS: {Count_Special_Elements} | QUALITY: {Text_Quality_Rating:.1f} | EFFICIENCY: {Processing_Efficiency:.1f}% | DENSITY: {Content_Density:.1f}% | CATEGORY: {Quality_Categories} | COMPLEXITY: {Text_Type_Complexity} | SIG: {Text_Signature}"

main()
