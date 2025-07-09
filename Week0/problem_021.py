"""
PROBLEM 21: Master Algorithm Synthesizer
Task: Write a function called master_synthesizer that creates the ultimate data processing system combining all advanced Week 0 concepts.
Requirements:
Function name: master_synthesizer
result1 = master_synthesizer("John Smith", "john@gmail.com", 2000, 75000, "TECH", 1199)
result2 = master_synthesizer("Mary Wilson", "mary@yahoo.com", 1995, 90000, "MARKETING", 1288)
result3 = master_synthesizer("Alex Brown", "alex@tech.org", 1997, 80000, "ENGINEERING", 1377)
Takes 6 parameters: full_name, email, birth_year, salary, department, employee_id
Extract and analyze: first_name, last_name, email_domain, age (2025 - birth_year)
Calculate name_score: (first_name_length × last_name_length) + vowel_count_in_full_name ----- Done
Calculate email_score: email_length × 2 + domain_length × 3------Done
Calculate career_score: (salary ÷ age) + (age × 10) + employee_id -----------Done
Create master_code: first2_name + last2_email + age + first3_department + last2_employee_id ----Done
Calculate ultimate_rating: (name_score + email_score + career_score) ÷ 10
Return formatted string: "MASTER: NAME | EMAIL: E | CODE: C | SCORES: N/E/C | ULTIMATE: U.U"
Round ultimate rating to 1 decimal place
MASTER: JOHN SMITH | EMAIL: john@gmail.com | CODE: joam25TEC99 | SCORES: 32/38/3015 | ULTIMATE: 308.5
MASTER: MARY WILSON | EMAIL: mary@yahoo.com | CODE: maom30MAR88 | SCORES: 42/40/3300 | ULTIMATE: 338.2
MASTER: ALEX BROWN | EMAIL: alex@tech.org | CODE: alrg28ENG77 | SCORES: 38/35/2857 | ULTIMATE: 293.0
"""
def main(): #defined main 
    result1 = master_synthesizer("John Smith", "john@gmail.com", 2000, 75000, "TECH", 1199) #asgn storing variable to calling func/6inputs - 3 texts +3 nos
    result2 = master_synthesizer("Mary Wilson", "mary@yahoo.com", 1995, 90000, "MARKETING", 1288)
    result3 = master_synthesizer("Alex Brown", "alex@tech.org", 1997, 80000, "ENGINEERING", 1377)

    print(result1) #print the item stored in storing variable / item is returned by the calling func
    print(result2)
    print(result3)

def master_synthesizer(full_name, email, birth_year, salary, department, employee_id): #def calling func/ 6 temp storing variables assigned 
    # get name score
    firstname,lastname=full_name.lower().split()
    firstnamelen=len(firstname)
    lastnamelen=len(lastname)
    fullname_chars=full_name.replace(" ","")
    vowel_count = fullname_chars.count("a")+fullname_chars.count("e")+fullname_chars.count("i")+fullname_chars.count("o")+fullname_chars.count("u")
    name_score= firstnamelen + lastnamelen + vowel_count

    # get email score and career score 
    age = 2025-birth_year
    email_length=len(email)
    subdomain,domain = email.split("@")
    domain_length=len(domain)
    email_score= email_length*2 + domain_length*3 
    career_score = int((salary / age) + (age * 10) + employee_id)

    #get master id 
    
    first2_name = firstname[:2]
    last2_email= email[-2:]
    first3_department= department[:3]
    employ_str=str(employee_id) # convert int to str to make it possible for slicing 
    last2_employee_id = employ_str[-2:] #slicing
    master_code = first2_name + last2_email + str(age) + first3_department + str(last2_employee_id)

    #get ultimate rating 
    ultimate_rating = (name_score + email_score + career_score) / 10
    caps_fullname=full_name.upper()

    return f"MASTER: {caps_fullname} | EMAIL: {email} | CODE: {master_code} | SCORES: {name_score}/{email_score}/{career_score} | ULTIMATE: {ultimate_rating:0.1f}"

main() #call main

