"""PROBLEM 49: Advanced Language Pattern Recognition Engine
Task: Write a function called pattern_detector that creates an intelligent linguistic analysis system capable of detecting sophisticated language patterns and text characteristics.
Requirements:
Function name: pattern_detector
result1 = pattern_detector("The quick brown fox jumps over the lazy dog. Programming is fun! Amazing algorithms work.", "linguistic", 7, 5)
result2 = pattern_detector("Python programming and coding is interesting technology.", "advanced", 6, 4)
result3 = pattern_detector("Machine learning algorithms efficiently process data.", "deep", 5, 3)
Takes 4 parameters: text_sample, detection_mode, sensitivity_level, analysis_depth
Detect word_length_patterns: count words of different lengths (1-3, 4-6, 7-10, 11+ chars)
Identify repetition_patterns: count repeated words, repeated letters, repeated phrases= common repeated words like the the , and and
Analyze punctuation_patterns: frequency of different punctuation marks
Calculate linguistic_complexity: average word length × unique word ratio × sentence variety
Calculate pattern_density: (total_patterns_found ÷ total_words) × 100
Calculate recognition_accuracy: (detected_patterns × sensitivity_level × analysis_depth) ÷ 100
Create detection_signature: detection_mode + word_count + pattern_count + accuracy_grade
Generate pattern_report with most frequent patterns identified
Return formatted string: "DETECTED: [pattern_report] | COMPLEXITY: C.C | DENSITY: D.D% | ACCURACY: A.A | PATTERNS: P | SIG: SIGNATURE"
Round complexity, density, and accuracy to 1 decimal place
Pattern Detection Rules:
Word lengths: Short (1-3), Medium (4-6), Long (7-10), Extended (11+)
Repetition types: Word repetition, letter repetition, pattern repetition
Punctuation analysis: Count periods, commas, exclamations, questions
Linguistic complexity: Based on vocabulary richness and structure variety
Accuracy grade: "Basic" (≤40), "Good" (41-70), "Excellent" (>70)
Expected Output:
DETECTED: Short:3 Medium:5 Long:2 Extended:1 Repeats:2 Punct:3 | COMPLEXITY: 45.8 | DENSITY: 73.3% | ACCURACY: 86.2 | PATTERNS: 16 | SIG: linguistic115Good
DETECTED: Short:2 Medium:4 Long:1 Extended:0 Repeats:1 Punct:1 | COMPLEXITY: 38.2 | DENSITY: 62.5% | ACCURACY: 67.5 | PATTERNS: 9 | SIG: advanced74Good
DETECTED: Short:1 Medium:2 Long:2 Extended:0 Repeats:0 Punct:1 | COMPLEXITY: 52.1 | DENSITY: 83.3% | ACCURACY: 75.0 | PATTERNS: 6 | SIG: deep53Excellent """
# define main
def main():
    result1 = pattern_detector("The quick brown fox jumps over the lazy dog. Programming is fun! Amazing algorithms work.", "linguistic", 7, 5)
    result2 = pattern_detector("Python programming and coding is interesting technology.", "advanced", 6, 4)
    result3 = pattern_detector("Machine learning algorithms efficiently process data.", "deep", 5, 3)
    
    print(result1)
    print(result2)
    print(result3)

# define calling func with parameters
def pattern_detector(text_sample, detection_mode, sensitivity_level, analysis_depth):
    #Detect word_length_patterns: count words of different lengths (1-3, 4-6, 7-10, 11+ chars).Word lengths: Short (1-3), Medium (4-6), Long (7-10), Extended (11+).
    words=text_sample.split()
    real_count_words = len(words)
    pad_words = (words+[""]*10)[:10]
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

    average_word_length = (w0_len + w1_len + w2_len + w3_len + w4_len + w5_len + w6_len + w7_len + w8_len + w9_len)/real_count_words 
    
    word_type = [ word_t0 , word_t1 , word_t2 , word_t3 , word_t4,  word_t5, word_t6, word_t7, word_t8, word_t9]

    count_Short =  word_type.count("Short")
    count_Medium =  word_type.count("Medium")
    count_Long =  word_type.count("Long")
    count_Extended =  word_type.count("Extended")

    count_pattern = count_Short + count_Medium + count_Long + count_Extended 

    # Identify repetition_patterns: 
    # count repeated words, 
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
    onlylets_text = text_sample.replace(" ","")
    onlylets_text = text_sample.replace(" ", "").lower()
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

    #Analyze punctuation_patterns: frequency of different punctuation marks  exclamations, questions
    frequency_periods = text_sample.count(".")
    frequency_commas = text_sample.count(",")
    frequency_exclamations = text_sample.count("!")
    frequency_questions = text_sample.count("?")

    sentence_variety =  frequency_periods + frequency_commas + frequency_exclamations + frequency_questions

    count_punctuation_pattern = sentence_variety

    # imp calculations
    Unique_word_ratio = (Number_of_unique_words / real_count_words ) * 100
    linguistic_complexity =  average_word_length * Unique_word_ratio * sentence_variety
    total_patterns = count_pattern + count_repeated_patterns + count_letters_pattern +  total_repeated_phrase + count_punctuation_pattern 
    pattern_density = (total_patterns / real_count_words) * 100
    recognition_accuracy =  (total_patterns * sensitivity_level * analysis_depth) / 100
    accuracy_grade = "Basic" * ( recognition_accuracy<=40) + "Good"* (41<recognition_accuracy<70)+"Excellent"* (recognition_accuracy>70)
    #Create detection_signature: detection_mode + word_count + pattern_count + accuracy_grade
    detection_signature = detection_mode + str(real_count_words)  + str(total_patterns) + accuracy_grade

    # return f string 
    return f"DETECTED: Short:{count_Short} Medium:{count_Medium } Long:{ count_Long} Extended:{count_Extended} Repeats:{total_repeated_phrase} Punct:{count_punctuation_pattern}| COMPLEXITY:{linguistic_complexity:0.1f} | DENSITY: {pattern_density:0.1f}% | ACCURACY: { recognition_accuracy} | PATTERNS: {total_patterns}| SIG: {detection_signature}"

# call main
main()
