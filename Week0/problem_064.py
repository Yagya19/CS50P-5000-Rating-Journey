def main():
    
    result1 = content_scorer("blog", "Writing great content takes time. Practice makes perfect.", 3, 2, 1)
    result2 = content_scorer("news", "Breaking news today! Major event occurred. Details follow.", 2, 1, 2)
    result3 = content_scorer("review", "This product works well. Quality is good. Would recommend it.", 4, 3, 1)
    
    print(result1)
    print(result2)
    print(result3)


def content_scorer(content_type, text_content, quality_threshold, scoring_weight, precision_level):
    #Step 1: Count Content Elements

    #total_words: Count words in text_content (separated by spaces)
    words = text_content.split() # made a list of words 
    count_words = len(words) # gives number of words in a list

    #unique_words: Count distinct words in text_content
    unique_words = set(words) # gives a list of non repeating words 
    count_unique_words = len(unique_words)

    #sentence_count: Count sentences ending with ".", "!", or "?"
    sentence_count = text_content.count(".")+text_content.count("!")+text_content.count("?") 

    #Step 2 is just applying the Quality Multiplier formula:
    Quality_Multiplier = 1.2*(content_type=="blog")+1.5*(content_type=="news")+ 1.1*(content_type=="review") 
                                                                                   
    Content_Complexity_Score = (count_words*1.5) + (count_unique_words*3) + (sentence_count* 8)

    Base_Content_Score = Content_Complexity_Score * Quality_Multiplier * scoring_weight

    Unchecked_Quality_Adjustment = Base_Content_Score - (quality_threshold * 20) 
    Quality_Adjustment = Unchecked_Quality_Adjustment*(Unchecked_Quality_Adjustment>=25) + 25
    Content_Diversity_Ratio =  (count_unique_words / count_words)*(count_words!=0) + 0.5*(count_words==0)
    Readability_Index =  (Content_Diversity_Ratio * 100) + (sentence_count*5)
    Content_Type_Complexity = 4*(content_type=="blog")+6*(content_type=="news")+ 5*(content_type=="review") 
    Quality_Categories = "Excellent"*(Quality_Adjustment>=200) + "Good"*(100<Quality_Adjustment<200) + "Average"*(Quality_Adjustment<100) 
    Scoring_Categories = "Advanced_Scoring"*(scoring_weight == 3) + "Standard_Scoring"*(scoring_weight == 2) + "Basic_Scoring"*(scoring_weight == 1)
    Content_Efficiency = (count_unique_words / sentence_count) * 10*(sentence_count != 0) + 15*(sentence_count == 0)
    Content_Signature = content_type + str(scoring_weight) + str(quality_threshold) +  Quality_Categories

    return f"SCORED: {Scoring_Categories} | TYPE: {content_type} | WORDS: {count_words} | UNIQUE: {count_unique_words} | SENTENCES: {sentence_count} | SCORE: {Quality_Adjustment:.1f} | DIVERSITY: {Content_Diversity_Ratio:.3f} | READABILITY: {Readability_Index:.1f} | EFFICIENCY: {Content_Efficiency:.1f} | CATEGORY: {Quality_Categories} | COMPLEXITY: {Content_Type_Complexity} | SIG: {Content_Signature}"

main()
   


                                                                                   

        
