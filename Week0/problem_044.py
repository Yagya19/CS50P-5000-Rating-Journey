"""PROBLEM 44: Advanced Text Data Parser
Task: Write a function called advanced_parser that creates an intelligent text parsing system capable of extracting structured data and meaningful information from unformatted text.
Requirements:
Function name: advanced_parser
result1 = advanced_parser("The company earned 123 million in 2024! Programming and testing are important. Data processing costs 456.", "standard", 6)
result2 = advanced_parser("AI systems processed 2000 records efficiently. Technology innovation in 25 companies@", "detailed", 7)
result3 = advanced_parser("Machine learning algorithms rapidly processing information effectively. Innovation costs 100 million.", "comprehensive", 8)
Takes 3 parameters: raw_data, parse_mode, extraction_depth
Extract all numbers from text and calculate their sum
Extract all capitalized words (potential proper nouns/names)
Extract all words ending with specific suffixes: "ing", "ed", "ly", "tion"
Count special characters: !@#$%^&*()
Calculate parsing_efficiency: (extracted_elements ÷ total_words) × 100
Calculate data_richness: (unique_extractions ÷ total_extractions) × 100 if extractions > 0, else 0
Calculate intelligence_score: (parsing_efficiency + data_richness) × extraction_depth ÷ 10
Create parser_signature: parse_mode + total_words + extracted_count + intelligence_rating
Return formatted string: "PARSED | Numbers: N (Sum: S) | Capitals: C | Suffixes: Sf | Special: Sp | Efficiency: E.E% | Richness: R.R% | Intelligence: I.I | SIG: SIGNATURE"
Round efficiency, richness, and intelligence to 1 decimal place
Parsing Rules:
Numbers: Extract digits and calculate sum
Capitals: Words starting with uppercase letter
Suffixes: Words ending with "ing", "ed", "ly", "tion"
Special chars: Count !@#$%^&*()
Intelligence rating: "Basic" (≤30), "Advanced" (31-60), "Expert" (>60)
Expected Output:
PARSED | Numbers: 3 (Sum: 579) | Capitals: 4 | Suffixes: 2 | Special: 2 | Efficiency: 61.1% | Richness: 90.0% | Intelligence: 90.7 | SIG: standard18610Expert
PARSED | Numbers: 2 (Sum: 2025) | Capitals: 3 | Suffixes: 1 | Special: 1 | Efficiency: 53.8% | Richness: 85.7% | Intelligence: 83.6 | SIG: detailed13712Expert
PARSED | Numbers: 1 (Sum: 100) | Capitals: 2 | Suffixes: 3 | Special: 0 | Efficiency: 75.0% | Richness: 100.0% | Intelligence: 131.3 | SIG: comprehensive816Expert """
#define main
def main():
    # set storing variables to store returned items from calling func provided with inputs reated to each profile
    result1 = advanced_parser("The company earned 123 million in 2024! Programming and testing are important. Data processing costs 456.", "standard", 6)
    result2 = advanced_parser("AI systems processed 2000 records efficiently. Technology innovation in 25 companies@", "detailed", 7)
    result3 = advanced_parser("Machine learning algorithms rapidly processing information effectively. Innovation costs 100 million.", "comprehensive", 8)
    # print each item stored in storing variable
    print(result1)
    print(result2)
    print(result3)

# define calling function with parameters 
def advanced_parser(raw_data, parse_mode, extraction_depth):
    # Extract all numbers from text and calculate their sum
    words=raw_data.split() # make a list of all words 
    total_words=len(words) # total words in raw text 

    w0 = words[0] * words[0].isnumeric()
    w1 = words[1] * words[1].isnumeric()
    w2 = words[2] * words[2].isnumeric()
    w3 = words[3] * words[3].isnumeric()
    w4 = words[4] * words[4].isnumeric()
    w5 = words[5] * words[5].isnumeric()
    w6 = words[6] * words[6].isnumeric()
    w7 = words[7] * words[7].isnumeric()
    w8 = words[8] * words[8].isnumeric()
    w9 = words[9] * words[9].isnumeric()
    w10 = words[10] * words[10].isnumeric()  # checked all words are number and stored in variable and told they are int 

    sum = w0+w1+w2+w3+w4+w5+w6+w7+w8+w9+w10 # got their sum

    # list of all nos words exctracted 
    nums_count = [w0,w1,w2,w3,w4,w5,w6,w7,w8,w9,w10]
    only_nums_list=list(filter(None,nums_count))

    unique_nums_list = set(only_nums_list)
    count_unq_nums_list=len(unique_nums_list) # count of unique nos extracted

    sum_num_word_extracted=len(only_nums_list)   # total number of words with numbers extracted

    # Extract all capitalized words (potential proper nouns/names) # 1 = if titled . 0 if not titled.
    c0 = words[0]* (words[0].istitle()) # get each list element checked and updated 
    c1 = words[1]* (words[1].istitle())
    c2 = words[2]*(words[2].istitle())
    c3 = words[3]*(words[3].istitle())
    c4 = words[4]*(words[4].istitle())
    c5 = words[5]*(words[5].istitle())
    c6 = words[6]*(words[6].istitle())
    c7 = words[7]*(words[7].istitle())
    c8 = words[8]*(words[8].istitle())
    c9 = words[9]*(words[9].istitle())
    c10 = words[10]*(words[10].istitle()) 

    capitalize_words =  [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]  # created the list omiiting the non capital elemets 
    ref_cap_list= list(filter(None,capitalize_words)) # filtered out void element from the capiatl filtered list

    unique_caps_list=set(ref_cap_list)
    
    count_unq_caps_list=len(unique_nums_list) # count of unique caps extracted 

    sum_cap_word_extracted=len(ref_cap_list) # total number of words with capitals extracted


    #Extract all words ending with specific suffixes: "ing", "ed", "ly", "tion"
    e0 = words[0]* words[0].endswith(("ing", "ed", "ly", "tion")) # get each list element checked and updated
    e0 = words[0] * words[0].endswith(("ing", "ed", "ly", "tion"))
    e1 = words[1] * words[1].endswith(("ing", "ed", "ly", "tion"))
    e2 = words[2] * words[2].endswith(("ing", "ed", "ly", "tion"))
    e3 = words[3] * words[3].endswith(("ing", "ed", "ly", "tion"))
    e4 = words[4] * words[4].endswith(("ing", "ed", "ly", "tion"))
    e5 = words[5] * words[5].endswith(("ing", "ed", "ly", "tion"))
    e6 = words[6] * words[6].endswith(("ing", "ed", "ly", "tion"))
    e7 = words[7] * words[7].endswith(("ing", "ed", "ly", "tion"))
    e8 = words[8] * words[8].endswith(("ing", "ed", "ly", "tion"))
    e9 = words[9] * words[9].endswith(("ing", "ed", "ly", "tion"))
    e10 = words[10] * words[10].endswith(("ing", "ed", "ly", "tion"))

    spec_nos_list = [e0,e1,e2,e3,e4,e5,e6,e7,e8,e9,e10]
    upg_spec_lst= list(filter(None, spec_nos_list))

    unique_suffix_list=set(upg_spec_lst)
    sum_suffix_word_extracted = len(unique_suffix_list)

    count_suffix_word_extracted=len(upg_spec_lst)  # total number of words with suffix extracted 

    #Count special characters: !@#$%^&*()
    a1=raw_data.count("!")
    a2=raw_data.count("@")
    a3=raw_data.count("#")
    a4=raw_data.count("$")
    a5=raw_data.count("%")
    a6=raw_data.count("^")
    a7=raw_data.count("&")
    a8=raw_data.count("*")
    a9=raw_data.count("(")
    a10 = raw_data.count(")")

    sum = int(a1) + int(a2)+int(a3) + int(a4)+int(a5) + int(a6)+int(a7) + int(a8)+int(a9)+int(a10)

    list_special = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
    filt_lst_special = list(filter(None,list_special))

    sum_special_word_extracted = len(filt_lst_special)  # total number of words with suffix extracted 
    upg_sum_special_word_extracted  = set(filt_lst_special)
    count_suffix_word_extracted = len(upg_sum_special_word_extracted)


    # imp calculations
    # extracted_elements : TOTAL count of all extracted items.
    # This should be the count of unique/distinct items found, not total count.
    extracted_elements = int(sum_num_word_extracted) + int(sum_cap_word_extracted) + int(sum_suffix_word_extracted) + int(sum_special_word_extracted)
    unique_extractions = count_unq_nums_list + count_unq_caps_list + count_suffix_word_extracted + count_suffix_word_extracted  
    total_extractions = extracted_elements + unique_extractions 
    parsing_efficiency = (extracted_elements / total_words) * 100
    data_richness = (unique_extractions / total_extractions) * 100 
    intelligence_score = (parsing_efficiency + data_richness) * extraction_depth / 10 

    # create sig 
    # set logic for inteligence rating 
    Intelligence_rating = "Basic" * (intelligence_score <=30) + "Advanced" * (31<intelligence_score <60) + "Expert"* (intelligence_score >60)
    parser_signature = parse_mode + str(total_words) +  str(total_extractions) + Intelligence_rating 

    # return f string 
    return f"PARSED | Numbers: {sum_cap_word_extracted} Sum: {sum} | Capitals: {sum_cap_word_extracted} | Suffixes: {count_suffix_word_extracted} | Special: { sum_special_word_extracted} | Efficiency: {parsing_efficiency:0.1f}% | Richness: {data_richness:0.1f}% | Intelligence: {intelligence_score :0.1f} | SIG: { parser_signature}"
    
# call main
main()
