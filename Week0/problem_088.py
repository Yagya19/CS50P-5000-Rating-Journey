#PROBLEM 88 - TIME SERIES PATTERN ANALYZER (COMPLETE CHALLENGE FORMAT)
def main():
    result1 = time_series_analyzer("upward", "rising123↗growth456↗increase→bull", 2, 3, 1)
    result2 = time_series_analyzer("downward", "decline248↘drop567↗correction", 1, 2, 2)
    result3 = time_series_analyzer("sideways", "stable135→flat↘range", 3, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def time_series_analyzer(trend_type, series_data, volatility_threshold, forecast_horizon, precision_level):
    #Step 1: Count Time Series Elements

    #series_length: Count total characters in series_data 
    series_length = len(series_data)
    #temporal_points: Count digit characters (0-9) in series_data
    temporal_points = series_data.count("0")+ series_data.count("1")+ series_data.count("2")+ series_data.count("3")+series_data.count("4")+ series_data.count("5")+ series_data.count("6")+ series_data.count("7")+ series_data.count("8")+ series_data.count("9")
    #trend_indicators: Count trend marker characters ("↗", "↘", "→") in series_data
    trend_indicators = series_data.count("↗")+ series_data.count("↘")+ series_data.count("→")

    Time_Series_Complexity_Score = (series_length * 21) + (temporal_points * 42) + (trend_indicators * 90)
    Trend_Multiplier = 7.2*(trend_type=="upward") +  6.7*(trend_type=="downward") +  6.2*(trend_type=="sideways") 
    Pattern_Forecast_Projection =  Time_Series_Complexity_Score  * Trend_Multiplier  * forecast_horizon
    Raw_Trend_Confidence_Index = Pattern_Forecast_Projection - (volatility_threshold * 230)
    Trend_Confidence_Index =  Raw_Trend_Confidence_Index * ( Raw_Trend_Confidence_Index >=460) + 460*( Raw_Trend_Confidence_Index<460)
    Temporal_Density_Ratio = temporal_points / (series_length + (series_length==0))*(series_length!=0) + 2.2*(series_length==0)
    Forecast_Accuracy = ( Temporal_Density_Ratio * 100) + (forecast_horizon * 115)
    Trend_Type_Complexity =  9*(trend_type=="upward") +  11*(trend_type=="downward") +  13*(trend_type=="sideways") 
    Confidence_Categories = "Strong_Trend"*(Trend_Confidence_Index>=1150) +  "Moderate_Trend"*(860<=Trend_Confidence_Index<1150) +  "Weak_Trend"*(Trend_Confidence_Index<860) 
    Forecast_Categories = "Long_Term_Forecast"*(forecast_horizon == 3) + "Medium_Term_Forecast"*(forecast_horizon == 2) +"Short_Term_Forecast"*(forecast_horizon == 1)
    Pattern_Stability = (trend_indicators * 220) / (temporal_points+(temporal_points==0)) * (temporal_points!=0) + 240*(temporal_points==0)
    Trend_Signature = trend_type + str(forecast_horizon) + str(volatility_threshold) + Confidence_Categories 

    return f"ANALYZED: {Forecast_Categories} | TREND: {trend_type} | LENGTH: {series_length} | POINTS: {temporal_points} | INDICATORS: {trend_indicators} | INDEX: {Trend_Confidence_Index:.1f} | ACCURACY: {Forecast_Accuracy:.1f}% | DENSITY: {Temporal_Density_Ratio:.3f} | STABILITY: {Pattern_Stability:.1f}% | CATEGORY: {Confidence_Categories} | COMPLEXITY: {Trend_Type_Complexity} | SIG: {Trend_Signature}"

main()
