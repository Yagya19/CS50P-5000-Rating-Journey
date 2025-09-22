#PROBLEM 72 - ECONOMIC SIMULATION ENGINE (COMPLETE CHALLENGE FORMAT)
def main():
    result1 = economic_simulator("stock", "price$125.50%growth#tech", 2, 3, 1)
    result2 = economic_simulator("currency", "usd$1.25%eur#exchange", 1, 2, 2)
    result3 = economic_simulator("commodity", "gold$1950%oil#barrel", 3, 1, 1)
    
    print(result1)
    print(result2)
    print(result3)

def economic_simulator(market_type, economic_data, volatility_factor, forecast_periods, precision_level):

    #Step 1: Count Economic Elements
    #market_size: Count total characters in economic_data
    market_size = len(economic_data)
    #financial_indicators: Count digit characters (0-9) in economic_data
    financial_indicators =  economic_data.count("0") + economic_data.count("1")+  economic_data.count("2") +  economic_data.count("3")+  economic_data.count("4")+ economic_data.count("5")+ economic_data.count("6")+  economic_data.count("7")+  economic_data.count("8")+  economic_data.count("9")  
    #trend_markers: Count trend indicator characters ("%", "$", "#") in economic_data
    trend_markers = economic_data.count("%") + economic_data.count("$")+  economic_data.count("#")

    Economic_Base_Score = (market_size * 5.5) + (financial_indicators * 10) + (trend_markers * 15)
    Market_Multiplier = 2.4 * (market_type=="stock") + 2.0 * (market_type=="currency") + 1.8 * (market_type=="commodity")
    Market_Projection = Economic_Base_Score * Market_Multiplier  * forecast_periods
    Raw_Economic_Stability_Index = Market_Projection  - (volatility_factor * 70)
    Economic_Stability_Index = Raw_Economic_Stability_Index * (Raw_Economic_Stability_Index>=140)+140*(Raw_Economic_Stability_Index<140) 
    Market_Liquidity_Ratio = financial_indicators / (market_size + (market_size==0)) * (market_size!=0) + 0.6*(market_size==0)
    Forecast_Reliability = ( Market_Liquidity_Ratio  * 100) + (forecast_periods * 35)
    Market_Type_Complexity = 8*(market_type=="stock") + 10 * (market_type=="currency") + 7 * (market_type=="commodity")
    Economic_Categories = "Bullish" * ( Economic_Stability_Index >= 350) + "Neutral" * ( 230<Economic_Stability_Index < 350) + "Bearish" * ( Economic_Stability_Index <230) 
    Forecast_Categories = "Long_Range_Forecast"*(forecast_periods == 3) + "Medium_Range_Forecast"*(forecast_periods == 2) +"Short_Range_Forecast"*(forecast_periods == 1) 
    Market_Volatility = trend_markers *60/ (financial_indicators + (financial_indicators==0)) * (financial_indicators!=0) + 85*(financial_indicators==0)
    Economic_Signature = market_type + str(forecast_periods) + str(volatility_factor) +  Economic_Categories 

    return f"FORECASTED: {Forecast_Categories } | TYPE: {market_type} | SIZE: {market_size} | INDICATORS: {financial_indicators} | TRENDS: {trend_markers} | INDEX: {Economic_Stability_Index:.1f} | RELIABILITY: {Forecast_Reliability :.1f}% | LIQUIDITY: {Market_Liquidity_Ratio :.3f} | VOLATILITY: {Market_Volatility:.1f}% | CATEGORY: {Economic_Categories} | COMPLEXITY: {Market_Type_Complexity} | SIG: {Economic_Signature }"

main()
