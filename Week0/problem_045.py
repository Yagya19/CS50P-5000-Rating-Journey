""" PROBLEM 45: Advanced Text Similarity Engine
Task: Write a function called similarity_calculator that creates an intelligent text comparison system capable of measuring similarity between two texts using multiple sophisticated algorithms.
Requirements:
Function name: similarity_calculator 
result1 = similarity_calculator("The quick brown fox jumps", "The fast brown dog runs quickly", "standard", 7)
result2 = similarity_calculator("Python programming is fun", "Java coding is interesting", "detailed", 9)
result3 = similarity_calculator("Machine learning algorithms", "Deep learning neural networks", "precise", 9)
Takes 4 parameters: text1, text2, comparison_mode, precision_level
Done - Calculate word_overlap: count of words that appear in both texts
Done - Calculate character_similarity: matching characters ÷ total unique characters × 100
Done Calculate length_similarity: 100 - (abs(len1 - len2) ÷ max(len1, len2) × 100)
Done Calculate vocabulary_match: shared_unique_words ÷ total_unique_words × 100
Done Calculate position_similarity: words in same positions ÷ min(word_count1, word_count2) × 100
Done Calculate overall_similarity: (character_similarity + length_similarity + vocabulary_match + position_similarity) ÷ 4
Done Create similarity_signature: comparison_mode + text1_word_count + text2_word_count + similarity_grade
Done Calculate confidence_score: overall_similarity × precision_level ÷ 10
Return formatted string: "SIMILARITY | Overlap: O words | Character: C.C% | Length: L.L% | Vocabulary: V.V% | Position: P.P% | Overall: Ov.Ov% | Confidence: Co.Co | SIG: SIGNATURE"
Round all percentages and confidence to 1 decimal place
Similarity Rules:
Word overlap: Count words present in both texts
Character similarity: Compare character sets
Length similarity: How close the lengths are
Vocabulary match: Shared unique words vs total unique words
Position similarity: Words in same positions
Similarity grade: "Low" (≤40%), "Medium" (41-70%), "High" (>70%)
Expected Output: 
SIMILARITY | Overlap: 4 words | Character: 65.2% | Length: 85.7% | Vocabulary: 44.4% | Position: 25.0% | Overall: 55.1% | Confidence: 38.6 | SIG: standard85Medium
SIMILARITY | Overlap: 2 words | Character: 58.3% | Length: 90.0% | Vocabulary: 28.6% | Position: 16.7% | Overall: 48.4% | Confidence: 43.6 | SIG: detailed76Medium
SIMILARITY | Overlap: 3 words | Character: 71.4% | Length: 75.0% | Vocabulary: 50.0% | Position: 33.3% | Overall: 57.4% | Confidence: 51.9 | SIG: precise69Medium """ 

# define main
def main():
    # set storing variables for calling func with inputs 
    result1 = similarity_calculator("The quick brown fox jumps", "The fast brown dog runs quickly", "standard", 7)
    result2 = similarity_calculator("Python programming is fun", "Java coding is interesting", "detailed", 9)
    result3 = similarity_calculator("Machine learning algorithms", "Deep learning neural networks", "precise", 9) 
    # print items stored in each variables
    print(result1)
    print(result2)
    print(result3)

# define calling func and set parameters to it 
def similarity_calculator(text1, text2, comparison_mode, precision_level):
    #1) Calculate word_overlap: count of words that appear in both texts
    words1 = text1.split() # create list for text1
    words2= text2.split() # create list for text2
    # take only unique words from each list
    onlyunq1 = set(words1)
    onlyunq2 = set(words2)
    # find comoon words by using intersection methods
    list_common_word = onlyunq1.intersection(onlyunq2)
    # Number of Common words
    count_common_word = len(list_common_word)

    # all unique words 
    list_all_unq_words=onlyunq1.union(onlyunq2)
    total_unique_words=len(list_all_unq_words)


    #2) - Calculate character_similarity: matching characters ÷ total unique characters × 100 
    # find matching character 
    all_chars_text1 = set(text1)  # all chars in a set made
    all_chars_text2 = set(text2)  
    # get matching chars in both 
    matching_characters = all_chars_text1.intersection(all_chars_text2) 
    # get matching char count 
    count_matching_chars= len(matching_characters)
    # get unique char in both 
    all_chars_text1 = set(text1)  # all chars in a set made
    unique_characters= all_chars_text1 .union(all_chars_text2) # all chars unique from both texts - non repeating 
    # get unique character count 
    count_unique_characters=len(unique_characters) 
    # charcter similarity calculations 
    character_similarity = count_matching_chars / count_unique_characters * 100 

    #3) Calculate length_similarity: 100 - (abs(len1 - len2) ÷ max(len1, len2) × 100)
    len1 = len(text1)
    len2 = len(text2)
    length_similarity = 100 - (abs(len1 - len2) / max(len1, len2) * 100)

    #4) Calculate vocabulary_match: count_common_word  / total_unique_words × 100 
    vocabulary_match = count_common_word  / total_unique_words * 100 

    #5) Calculate position_similarity: words in same positions ÷ min(word_count1, word_count2) × 100
    word_count1 = len(words1)
    word_count2 = len(words2)

    words_1 = (words1 + [""] * 10 )[:10]
    words_2 = (words2 + [""] * 10 )[:10]

    # position similarity checked for each position for word1 and word2 list # if yes match = 1 / if no match = zero
    match0 = words_1[0] == words_2 [0]
    match1 = words_1[1] == words_2 [1]
    match2 = words_1[2] == words_2 [2]
    match3 = words_1[3] == words_2 [3]
    match4 = words_1[4] == words_2 [4]
    match5 = words_1[5] == words_2 [5]
    match6 = words_1[6] == words_2 [6]
    match7 = words_1[7] == words_2 [7]
    match8 = words_1[8] == words_2 [8]
    match9 = words_1[9] == words_2 [9]

    match_count =  (match0 + match1 + match2 + match3 + match4 + match5 + match6 + match7 + match8 + match9) 

    # main calculations 
    position_similarity = match_count / min(word_count1, word_count2) * 100

    #6) Calculate overall_similarity: (character_similarity + length_similarity + vocabulary_match + position_similarity) ÷ 4
    overall_similarity = (character_similarity + length_similarity + vocabulary_match + position_similarity) / 4

    #7) Create similarity_signature: comparison_mode + text1_word_count + text2_word_count + similarity_grade 
    similarity_grade = "Low" * (overall_similarity<=40) + "Medium" * (41<overall_similarity<70)+ "High"* (overall_similarity>70) 
    # main formula 
    similarity_signature = str(comparison_mode) + str(word_count1)  + str(word_count2) + similarity_grade 

    #8) Calculate confidence_score: overall_similarity × precision_level ÷ 10
    confidence_score = overall_similarity * precision_level / 10

    # return f string 
    return f"SIMILARITY | Overlap: {count_common_word} words | Character: {character_similarity:0.1f} % | Length: {length_similarity:0.1f} % | Vocabulary: {vocabulary_match:0.1f} % | Position: {position_similarity:0.1f}% | Overall: {overall_similarity:0.2f} % | Confidence: {confidence_score:0.2f} | SIG: {similarity_signature}"

# call main()
main()
