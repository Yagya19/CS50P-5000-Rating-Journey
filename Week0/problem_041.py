""" PROBLEM 41: Advanced Text Intelligence Analyzer
Task: Write a function called text_analyzer that creates a comprehensive text analysis system providing detailed linguistic insights and readability metrics.
Requirements:
Function name: text_analyzer
result1 = text_analyzer("The quick brown fox jumps over lazy dog. Python programming is fun! Advanced algorithms rock.", "standard")
result2 = text_analyzer("Artificial intelligence revolutionizes technology. Modern systems enable breakthrough innovations.", "detailed")
result3 = text_analyzer("Machine learning algorithms process complex data efficiently.", "comprehensive")
Takes 2 parameters: text_content, analysis_mode
Calculate word_count: total number of words
Calculate average_word_length: total characters ÷ word count
Calculate sentence_count: count periods, exclamation marks, question marks
Calculate readability_score: (average_word_length × 10) + (word_count ÷ sentence_count)
Calculate vocabulary_richness: unique_words ÷ total_words × 100
Calculate text_complexity: readability_score × vocabulary_richness ÷ 100
Create analysis_report: first_word + last_word + word_count + complexity_rating
Return formatted string: "TEXT ANALYSIS | Words: W | Avg Length: A.A | Sentences: S | Readability: R.R | Richness: Ri.Ri% | Complexity: C.C | Report: REPORT"
Round all decimal values to 1 decimal place
Expected Output:
TEXT ANALYSIS | Words: 15 | Avg Length: 5.2 | Sentences: 3 | Readability: 57.0 | Richness: 80.0% | Complexity: 45.6 | Report: ThePython15Advanced
TEXT ANALYSIS | Words: 12 | Avg Length: 6.1 | Sentences: 2 | Readability: 91.0 | Richness: 75.0% | Complexity: 68.3 | Report: ArtificialSystems12Expert  
TEXT ANALYSIS | Words: 8 | Avg Length: 4.8 | Sentences: 1 | Readability: 128.0 | Richness: 100.0% | Complexity: 128.0 | Report: MachineLearning8Master """

# define main
def main():
    # set storing variables for calling func with inputs from each profile
    result1 = text_analyzer("The quick brown fox jumps over lazy dog. Python programming is fun! Advanced algorithms rock.", "standard")
    result2 = text_analyzer("Artificial intelligence revolutionizes technology. Modern systems enable breakthrough innovations.", "detailed")
    result3 = text_analyzer("Machine learning algorithms process complex data efficiently.", "comprehensive") 
    # print each item from storing variable
    print(result1)
    print(result2)
    print(result3)

#define calling function with parameters
def text_analyzer(text_content, analysis_mode):
    # all imp formulas
    words=text_content.split() # make list of all words
    total_number_of_words = len( words) # take count of all words
    word_count = total_number_of_words # get word count value
    total_characters=len(text_content) # get all characters 
    average_word_length = total_characters / word_count # get avg word length 
    # as sentence eithrr ends with a dot, ? or ! we use it as way to get number of sentences
    sentence_count = text_content.count(".") + text_content.count("?") + text_content.count("!") 
    readability_score = (average_word_length * 10) + (word_count / sentence_count)
    unique_words=set(text_content)
    count_unique_words=len( unique_words)
    vocabulary_richness = count_unique_words /  total_number_of_words * 100
    text_complexity = readability_score * vocabulary_richness / 100
    last_filter=words[-1]
    last=last_filter.replace(".","")
    analysis_report = words[0] +  last + str(word_count) + str(int(text_complexity)) 

    # return f string 
    return f"TEXT ANALYSIS | Words: {word_count} | Avg Length: {average_word_length:0.1f} | Sentences: {sentence_count} | Readability: {readability_score:0.1f} | Richness: {vocabulary_richness :0.2f}% | Complexity: {text_complexity:0.1f} | Report: {analysis_report}"

# call main
main()
