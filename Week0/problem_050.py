""" PROBLEM 50: Master Text Intelligence Processor
Task: Write a function called ultimate_processor that creates the supreme text processing system combining analysis, transformation, cleaning, pattern detection, and intelligent optimization into one master engine.
Requirements:
Function name: ultimate_processor
result1 = ultimate_processor("The   quick123  brown   fox  jumps over the the lazy dog! Programming is fun!!! Advanced algorithms rock.", "comprehensive", 8, "professional", "professional")
result2 = ultimate_processor("Python456  programming  is    fun and and powerful technology!!!", "intelligent", 7, "creative", "creative")
result3 = ultimate_processor("Machine    learning algorithms  process complex data efficiently.", "advanced", 6, "technical", "technical")
Takes 5 parameters: input_text, processing_mode, intelligence_level, optimization_target, output_style
Perform comprehensive_analysis: word count, character analysis, readability metrics, vocabulary richness
Execute smart_transformation: case optimization, punctuation normalization, spacing correction
Apply intelligent_cleaning: remove unwanted elements based on intelligence_level
Conduct pattern_recognition: detect linguistic patterns, repetitions, and structural elements
Generate optimization_score: (analysis_quality × transformation_efficiency × cleaning_effectiveness) ÷ 100
Calculate processing_mastery: (optimization_score × intelligence_level × pattern_density) ÷ 1000
Calculate ultimate_intelligence: (processing_mastery + comprehensive_metrics + pattern_complexity) × output_bonus
Create master_signature: processing_mode + word_count + intelligence_level + optimization_target + mastery_grade
Produce final_output based on output_style with maximum optimization
Return formatted string: "ULTIMATE: [final_output] | ANALYSIS: A.A | TRANSFORMATION: T.T | CLEANING: C.C | PATTERNS: P | OPTIMIZATION: O.O | MASTERY: M.M | INTELLIGENCE: I.I | SIG: SIGNATURE"
Round all metrics to 1 decimal place
Processing Rules:
Comprehensive analysis: All text metrics from previous problems combined
Smart transformation: Intelligent case, punctuation, and formatting optimization
Intelligent cleaning: Adaptive cleaning based on intelligence_level (1-10 scale)
Pattern recognition: Advanced linguistic and structural pattern detection
Output styles: "professional", "creative", "academic", "technical"
Mastery grade: "Expert" (≥80), "Master" (60-79), "Advanced" (40-59), "Standard" (<40)
Expected Output:
ULTIMATE: The Quick Brown Fox Jumps Over Lazy Dog Programming Advanced Algorithms | ANALYSIS: 87.5 | TRANSFORMATION: 92.3 | CLEANING: 89.1 | PATTERNS: 25 | OPTIMIZATION: 736.8 | MASTERY: 2947.2 | INTELLIGENCE: 35366.4 | SIG: comprehensive158professional Expert
ULTIMATE: Python Programming Technology Innovation Systems | ANALYSIS: 78.2 | TRANSFORMATION: 85.6 | CLEANING: 82.4 | PATTERNS: 18 | OPTIMIZATION: 551.2 | MASTERY: 1653.6 | INTELLIGENCE: 16536.0 | SIG: intelligent97creative Master
ULTIMATE: Machine Learning Algorithms Process Complex Data | ANALYSIS: 82.1 | TRANSFORMATION: 88.9 | CLEANING: 85.7 | PATTERNS: 22 | OPTIMIZATION: 625.4 | MASTERY: 2188.9 | INTELLIGENCE: 21889.0 | SIG: advanced86technical Expert """ 

# define main
def main():
    result1 = ultimate_processor("The   quick123  brown   fox  jumps over the the lazy dog! Programming is fun!!! Advanced algorithms rock.", "comprehensive", 8, "professional", "professional")
    result2 = ultimate_processor("Python456  programming  is    fun and and powerful technology!!!", "intelligent", 7, "creative", "creative")
    result3 = ultimate_processor("Machine    learning algorithms  process complex data efficiently.", "advanced", 6, "technical", "technical")

    
    print(result1)
    print(result2)
    print(result3)


# define caling func with parameters
def ultimate_processor(input_text, processing_mode, intelligence_level, optimization_target, output_style):
    # Perform comprehensive_analysis: word count - done,  , readability metrics :  
    # word count
    words = input_text.split()
    unique_words = len(set(words))
    word_count = len(words) 
    # character_analysis_score = (letters_only / total_characters) * 100
    no_spaces_text = input_text.replace(" ","")
    letters_only = len(no_spaces_text)
    uniques_chars = set(no_spaces_text)
    total_characters = len(uniques_chars)
    character_analysis_score = (letters_only / total_characters) * 100

    # readability_score = (avg_word_length * 10) + (word_count / sentence_count) 
    pad_words=  (words + [""]*10)[:10]

    w0_len = len(pad_words[0])
    word_t0 = "Short"*(1<w0_len<3) + "Medium"*(4<w0_len<6) + "Long"*(7<w0_len<10) + "Extended"*(w0_len>=11)
    w1_len = len(pad_words[1])
    word_t1 = "Short"*(1 < w1_len < 3) + "Medium"*(4 < w1_len < 6) + "Long"*(7 < w1_len < 10) + "Extended"*(w1_len >= 11)
    w2_len = len(pad_words[2])
    word_t2 = "Short"*(1 < w2_len < 3) + "Medium"*(4 < w2_len < 6) + "Long"*(7 < w2_len < 10) + "Extended"*(w2_len >= 11)
    w3_len = len(pad_words[3])
    word_t3 = "Short"*(1 < w3_len < 3) + "Medium"*(4 < w3_len < 6) + "Long"*(7 < w3_len < 10) + "Extended"*(w3_len >= 11)
    w4_len = len(pad_words[4])
    word_t4 = "Short"*(1 < w4_len < 3) + "Medium"*(4 < w4_len < 6) + "Long"*(7 < w4_len < 10) + "Extended"*(w4_len >= 11)
    w5_len = len(pad_words[5])
    word_t5 = "Short"*(1 < w5_len < 3) + "Medium"*(4 < w5_len < 6) + "Long"*(7 < w5_len < 10) + "Extended"*(w5_len >= 11)
    w6_len = len(pad_words[6])
    word_t6 = "Short"*(1 < w6_len < 3) + "Medium"*(4 < w6_len < 6) + "Long"*(7 < w6_len < 10) + "Extended"*(w6_len >= 11)
    w7_len = len(pad_words[7])
    word_t7 = "Short"*(1 < w7_len < 3) + "Medium"*(4 < w7_len < 6) + "Long"*(7 < w7_len < 10) + "Extended"*(w7_len >= 11)
    w8_len = len(pad_words[8])
    word_t8 = "Short"*(1 < w8_len < 3) + "Medium"*(4 < w8_len < 6) + "Long"*(7 < w8_len < 10) + "Extended"*(w8_len >= 11)
    w9_len = len(pad_words[9])
    word_t9 = "Short"*(1 < w9_len < 3) + "Medium"*(4 < w9_len < 6) + "Long"*(7 < w9_len < 10) + "Extended"*(w9_len >= 11)

    avg_word_length =  (w0_len + w1_len + w2_len + w3_len + w4_len + w5_len + w6_len + w7_len + w8_len + w9_len) / word_count

    sentence_breaker_text = input_text.replace(".",".|").replace("?","?|").replace("!","!|")
    sentence_list = sentence_breaker_text.split("|")
    sentence_count = len(sentence_list)

    readability_score = (avg_word_length * 10) + (word_count / sentence_count) 

    vocabulary_richness = (unique_words / word_count) * 100

    analysis_quality = character_analysis_score  + readability_score + vocabulary_richness

    comprehensive_metrics =  analysis_quality

    # Execute smart_transformation: case optimization, punctuation normalization, spacing correction

    # case optimisation 
    # Capitalize first word of each sentence + proper nouns
    capitalise_text = input_text.lower().capitalize() 

    case_optimisation = len(capitalise_text)

    # add space after each sentence breaker 
    spaced_start_text = capitalise_text. replace(".",". ").replace("?","? ").replace("!","! ")

    # normalise excessive punctuation 
    punctuation_text = spaced_start_text.replace("!!!","! ").replace("???","? ").replace("...",". ")

    punctuation_normalization = len(punctuation_text)

    # space correction 
    elements = punctuation_text.split()

    perfect_text = " ".join(elements)
    spacing_correction = len(perfect_text)


    # Apply intelligent_cleaning: remove unwanted elements based on intelligence_level
    # c1// if intelligence_level <= 3:  # Remove extra spaces only
    fix_space_text = " ".join(words)
    



    #c2 // if 4 <= intelligence_level <= 6: # ... remove all digits & # Space normalization

    digits_removed_text = input_text.replace("0","").replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","")
    words_without_digits = len(digits_removed_text)
    nodigits_fix_space = " ".join(digits_removed_text)
    # c3 //if 7 <= intelligence_level <= 8: # Remove everything unwanted
    digits_removed_text = input_text.replace("0","").replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","")
    symbol_digit_removed_text = digits_removed_text.replace("@","").replace("#","").replace("$","").replace("%","").replace("^","").replace("&","").replace("*","")
    symbol_digit_removed_words = symbol_digit_removed_text.split()
    symbol_digit_fix_space_removed_text = " ".join(symbol_digit_removed_words)
    
    #c4 // if intelligence_level >= 9: # Remove digits, special chars, short words  # Maybe remove common words like "the", "and", "is"
    symbol_digit_phrase_removed_text = symbol_digit_removed_text.replace("the","").replace("and","").replace("is","")
    symbol_digit_phrase_removed_elemnts = symbol_digit_phrase_removed_text.split()
    symbol_digit_phrase_fixspace_text = " ".join(symbol_digit_phrase_removed_elemnts)

    intelligent_clean = perfect_text*(intelligence_level <= 3) + nodigits_fix_space*(4 <= intelligence_level <= 6) +  symbol_digit_fix_space_removed_text*(7 <= intelligence_level <= 8) + symbol_digit_phrase_fixspace_text*(intelligence_level >= 9)

    intelligent_cleaning = len(intelligent_clean)

    transformation_efficiency =  case_optimisation + punctuation_normalization + spacing_correction

    optimization_score = analysis_quality + transformation_efficiency + intelligent_cleaning 

    # Conduct pattern_recognition: detect linguistic patterns, repetitions, and structural elements
    #1. Linguistic Patterns:
    #Word length categories: Count short (1-3), medium (4-6), long (7-10), extended (11+) words

    word_type = [ word_t0 , word_t1 , word_t2 , word_t3 , word_t4,  word_t5, word_t6, word_t7, word_t8, word_t9]

    count_Short =  word_type.count("Short")
    count_Medium =  word_type.count("Medium")
    count_Long =  word_type.count("Long")
    count_Extended =  word_type.count("Extended")
   
    count_pattern = count_Short + count_Medium + count_Long + count_Extended 

    #2. Repetitions: Repeated words: Words that appear multiple times / Repeated letters: Letters that appear frequently / Repeated phrases: Common word combinations that repeat

    pad_words = (words+[""]*10)[:10]
    unique_words = list(set(pad_words))
    Number_of_unique_words = len(unique_words)
    
    pad_unique_words = (unique_words + [""]*5)[:5]
    first_repeated_count = pad_words.count(pad_unique_words[0])
    sec_repeated_count = pad_words.count(pad_unique_words[1])
    trd_repeated_count = pad_words.count(pad_unique_words[2])
    four_repeated_count = pad_words.count(pad_unique_words[3])
    five_repeated_count = pad_words.count(pad_unique_words[4])

    count_repeated_patterns = first_repeated_count + sec_repeated_count + trd_repeated_count + four_repeated_count + five_repeated_count 

    #count repeated letters, 
    onlylets_text = input_text.lower().replace(" ","")
    a = onlylets_text.count("a")
    b = onlylets_text.count("b")
    c = onlylets_text.count("c")
    d = onlylets_text.count("d")
    e = onlylets_text.count("e")
    f = onlylets_text.count("f")
    g = onlylets_text.count("g")
    h = onlylets_text.count("h")
    i = onlylets_text.count("i")
    j = onlylets_text.count("j")
    k = onlylets_text.count("k")
    l = onlylets_text.count("l")
    m = onlylets_text.count("m")
    n = onlylets_text.count("n")
    o = onlylets_text.count("o")
    p = onlylets_text.count("p")
    q = onlylets_text.count("q")
    r = onlylets_text.count("r")
    s = onlylets_text.count("s")
    t = onlylets_text.count("t")
    u = onlylets_text.count("u")
    v = onlylets_text.count("v")
    w = onlylets_text.count("w")
    x = onlylets_text.count("x")
    y = onlylets_text.count("y")
    z = onlylets_text.count("z")

    count_letters_pattern = a + b + c + d + e + f + g + h + i + j + k + l + m + n + o + p + q + r + s + t + u + v + w + x + y + z


    # repeated phrases
    first_repeated_phrase = pad_words.count(pad_unique_words[0])* (pad_words.count(pad_unique_words[0]) > 1 )
    sec_repeated_phrase = pad_words.count(pad_unique_words[1])*(pad_words.count(pad_unique_words[1]) > 1 )
    trd_repeated_phrase = pad_words.count(pad_unique_words[2])*(pad_words.count(pad_unique_words[2]) > 1 )
    four_repeated_phrase = pad_words.count(pad_unique_words[3])*(pad_words.count(pad_unique_words[3]) > 1 )
    five_repeated_phrase = pad_words.count(pad_unique_words[4])*(pad_words.count(pad_unique_words[4]) > 1 )

    total_repeated_phrase = first_repeated_phrase + sec_repeated_phrase + trd_repeated_phrase + four_repeated_phrase + five_repeated_phrase 


    # 3. Structural Elements:  Punctuation patterns: Count periods, commas, exclamations, questions  #Analyze punctuation_patterns: frequency of different punctuation marks  exclamations, questions
    frequency_periods = input_text.count(".")
    frequency_commas = input_text.count(",")
    frequency_exclamations = input_text.count("!")
    frequency_questions = input_text.count("?")

    count_punctuation_pattern =  frequency_periods + frequency_commas + frequency_exclamations + frequency_questions

    total_patterns = count_pattern + count_repeated_patterns + count_letters_pattern +  total_repeated_phrase + count_punctuation_pattern 
    pattern_complexity = total_patterns 

    pattern_density = (total_patterns / word_count) * 100

    processing_mastery = (optimization_score * intelligence_level * pattern_density) / 1000

    # Based on output_style parameter
    output_bonus = 5 * (output_style == "professional") +  8 * (output_style == "creative") + 10 * (output_style == "academic") + 12 * (output_style == "technical")

    ultimate_intelligence = (processing_mastery + comprehensive_metrics + pattern_complexity) * output_bonus

    #Create master_signature: processing_mode + word_count + intelligence_level + optimization_target + mastery_grade

    mastery_grade =  "Expert" * ( processing_mastery>=80) + "Master"* (60< processing_mastery<79) + "Advanced"* (40< processing_mastery<59)+ "Standard" *( processing_mastery<40)

    master_signature = processing_mode + str(word_count) + str(intelligence_level) + str(optimization_target) + mastery_grade

    # return f string 
    return f"ULTIMATE: {intelligent_cleaning} | ANALYSIS: {analysis_quality:0.1f} | TRANSFORMATION: { transformation_efficiency:0.1f} | CLEANING: {intelligent_cleaning:0.1f} | PATTERNS: {total_patterns} | OPTIMIZATION: {optimization_score:0.1f} | MASTERY: { processing_mastery:0.1f} | INTELLIGENCE: {ultimate_intelligence:0.1f} | SIG: {master_signature}"

# call main
main()
