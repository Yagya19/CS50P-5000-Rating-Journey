"""
PROBLEM 25: Ultimate Performance Engine
Task: Write a function called performance_engine that creates the ultimate performance analysis system combining all advanced computational concepts.
Requirements:
Function name: performance_engine
result1 = performance_engine("Sarah Wilson", "Engineering", 8, 32, 80, 90000, 6, "New York")
result2 = performance_engine("Mike Davis", "Marketing", 5, 22, 75, 70000, 5, "Seattle")
result3 = performance_engine("Lisa Brown", "Finance", 12, 45, 90, 110000, 7, "Chicago")
Takes 8 parameters: employee_name, department, years_experience, projects_completed, success_rate, salary, team_size, location
Calculate experience_factor: years_experience × (projects_completed ÷ 10) × (success_rate ÷ 100)
Calculate productivity_index: (projects_completed × success_rate) ÷ years_experience
Calculate team_efficiency: (salary ÷ team_size) × (success_rate ÷ 100)
Calculate location_bonus: len(location) × 100 + years_experience × 50
Calculate performance_score: (experience_factor + productivity_index + team_efficiency + location_bonus) ÷ 4
Create ultimate_id: first3_employee + dept_length + years + last2_salary + first2_location
Calculate mastery_level: performance_score × (projects_completed ÷ 100) × (team_size ÷ 10)
Return formatted string: "PERFORMANCE: NAME | DEPT: D | EXP: X.X | PROD: Y.Y | TEAM: Z.Z | SCORE: S.S | ID: I | MASTERY: M.M"
Round all decimal values to 1 decimal place
PERFORMANCE: SARAH WILSON | DEPT: ENGINEERING | EXP: 64.0 | PROD: 30.0 | TEAM: 1350.0 | SCORE: 941.0 | ID: Sar1180090Ne | MASTERY: 1223.3
PERFORMANCE: MIKE DAVIS | DEPT: MARKETING | EXP: 38.4 | PROD: 27.5 | TEAM: 1050.0 | ID: Mik900085Se | MASTERY: 798.0
PERFORMANCE: LISA BROWN | DEPT: FINANCE | EXP: 108.0 | PROD: 37.5 | TEAM: 1575.0 | ID: Lis70011000Ch | MASTERY: 1620.0 """

#define main 
def main():
    # create storing variable for calling input with inputs for each profile 
    profile1 = performance_engine("Sarah Wilson", "Engineering", 8, 32, 80, 90000, 6, "New York")
    profile2 = performance_engine("Mike Davis", "Marketing", 5, 22, 75, 70000, 5, "Seattle")
    profile3 = performance_engine("Lisa Brown", "Finance", 12, 45, 90, 110000, 7, "Chicago")
    # print item stored in storing variable ie returned by calling func
    print(profile1)
    print(profile2)
    print(profile3)
#defined calling function and set temp storing variables
def  performance_engine(employee_name, department, years_experience, projects_completed, success_rate, salary, team_size, location):
    # all calculations
    experience_factor = years_experience * (projects_completed / 10) * (success_rate / 100)
    productivity_index = (projects_completed * success_rate) / years_experience
    team_efficiency = (salary / team_size) * (success_rate / 100)
    location_bonus = len(location) * 100 + years_experience * 50
    performance_score= (experience_factor + productivity_index + team_efficiency + location_bonus) / 4
    # ultimate_id: first3_employee + str(dept_length) + str(years_experience) + str(last2_salary) + first2_location
    first,last=employee_name.split()
    first3_employee=first[:3]
    dept_length = len(department)
    salary_str=str(salary)
    last2_salary=salary_str[-2:]
    first2_location=location[:2]
    ultimate_id = first3_employee + str(dept_length) + str(years_experience) + str(last2_salary) + first2_location
    #mastery_level: performance_score × (projects_completed ÷ 100) × (team_size ÷ 10)
    mastery_level = performance_score * (projects_completed / 100) * (team_size / 10)
    # name in caps
    NAME=employee_name.upper()
    # return f string 
    return f"PERFORMANCE: {NAME} | DEPT: {department} | EXP: {experience_factor:0.1f} | PROD: {productivity_index:0.1f} | TEAM: {team_efficiency:0.1f} | SCORE: {performance_score:0.1f} | ID: {ultimate_id} | MASTERY: {mastery_level:0.1f}"

#calling main
main()
