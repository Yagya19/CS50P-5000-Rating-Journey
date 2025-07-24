""" PROBLEM 52: Statistical Data Analysis Engine
Task: Write a function called statistical_analyzer that processes numerical datasets and computes essential statistical metrics for data analysis.
Requirements:
Function name: statistical_analyzer
result = statistical_analyzer("10,15,20,25,30,35,40", "comprehensive", 3, "detailed")
# Should process the data and return statistical analysis
Takes 4 parameters: data_values, analysis_type, computation_depth, output_format
Process data_values (comma-separated string of numbers) into individual numbers
Calculate basic statistics: mean, median approximation, range, standard deviation approximation
Perform distribution analysis: min, max, data spread analysis
Generate data_quality_score based on data consistency and range
Create statistical_summary with key findings
Return formatted results based on output_format 
Statistical Operations:
Mean: Sum of all values ÷ count
Range: Maximum - minimum
Data spread: How evenly distributed the values are
Basic standard deviation: Measure of data variation (simplified calculation)
# Mean: Sum of all values ÷ count
mean = (num1 + num2 + num3 + num4 + num5) / count
# Range: Maximum - minimum  
range_value = max_value - min_value
# Data spread: How spread out the data is
data_spread = range_value / mean * 100  # As percentage of mean
median_approx = middle_value  # You'll need to find this
 """
# define main()
def main():
    # set storing values for calling func 
    result1 = statistical_analyzer("10,15,20,25,30", "basic", 2, "summary")
    result2 = statistical_analyzer("5,10,15,20,25,30,35", "comprehensive", 3, "detailed")
    result3 = statistical_analyzer("100,200,150,175,225", "advanced", 4, "report")

    # print each item in storing value
    print(result1)
    print(result2) 
    print(result3)

# define calling func with parameters 
def statistical_analyzer(data_values, analysis_type, computation_depth, output_format):
    # Process data_values (comma-separated string of numbers) into individual numbers
    nums = list(map(int,data_values.split(","))) # converting string of numbers into actual nos list 
    #Calculate basic statistics: mean, median approximation, range, standard deviation approximation

    # Calculate basic statistics: mean, median approximation, range, standard deviation approximation
    count=len(nums) # total count of numbers 
    pad_nums = (nums + [0]*10)[:10] # padding a numerical list

    Sum_of_all_values = pad_nums[0]+pad_nums[1]+pad_nums[2]+pad_nums[3]+pad_nums[4]+pad_nums[5]+pad_nums[6]+pad_nums[7]+pad_nums[8]+pad_nums[9]

    mean = Sum_of_all_values / count    # got mean 

    maximum = max(nums) 
    minimum = min(nums)

    range_value =  maximum -  minimum  # got range value

    # median_approx = middle_value  # You'll ned to find this
    
    sorted_nums = sorted(nums) 
    p = (count)//2   # first index value 
    q = p-1   # second index value for even cases 
    
    median_approx = ((sorted_nums[p]+sorted_nums[q])/2)*(count%2==0) + sorted_nums[p]*(count%2!=0) # formula for median for both even and odd list count 

    # # Standard deviation approximation (simplified) : Calculate differences from mean, then average 


    diff0 = abs(pad_nums[0]-mean)
    diff1 = abs(pad_nums[1]-mean)
    diff2 = abs(pad_nums[2]-mean)
    diff3 = abs(pad_nums[3]-mean)
    diff4 = abs(pad_nums[4]-mean)*(pad_nums[4]!=0) + 0*(pad_nums[4]==0)
    diff5 = abs(pad_nums[5]-mean)*(pad_nums[5]!=0) + 0*(pad_nums[5]==0)
    diff6 = abs(pad_nums[6]-mean)*(pad_nums[6]!=0) + 0*(pad_nums[6]==0)
    diff7 = abs(pad_nums[7]-mean)*(pad_nums[7]!=0) + 0*(pad_nums[7]==0)
    diff8 = abs(pad_nums[8]-mean)*(pad_nums[8]!=0) + 0*(pad_nums[8]==0)
    diff9 = abs(pad_nums[9]-mean)*(pad_nums[9]!=0) + 0*(pad_nums[9]==0)
                
    std_deviation_approx = (diff0 + diff1 + diff2 +diff3 + diff4 + diff5 + diff6 + diff7 +diff8 + diff9)/count # standard deviation calculated 

    #3. Data Quality Score:
   
    consistency_factor = 100 - (std_deviation_approx / mean * 100)
    range_factor = 100 - (range_value / mean * 100)
    data_quality_score = (consistency_factor + range_factor) / 2



    # Data spread analysis
    spread_percentage = (range_value / mean) * 100

    quality_grade = "Excellent" * (data_quality_score >= 80) + "Good" * (60 <= data_quality_score < 80) + "Fair" * (data_quality_score < 60)

    analysis_signature = analysis_type + str(count) + str(computation_depth) + quality_grade

    # Create statistical summary 
    statistical_summary = "Normal_Distribution" * (std_deviation_approx < mean/3) + "Wide_Spread" * (std_deviation_approx >= mean/3)

    # return f string 
    return f"ANALYZED: {statistical_summary} | MEAN: {mean:0.1f} | MEDIAN: {median_approx:.1f} | RANGE: {range_value} | STD_DEV: {std_deviation_approx:0.2f} | SPREAD: {spread_percentage:0.1f}% | QUALITY: {data_quality_score:0.1f} | MIN: {minimum} | MAX: {maximum} | SIG: {analysis_signature}"

# call main
main()
