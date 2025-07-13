"""PROBLEM 33: Advanced Trading Algorithm Engine
Task: Write a function called trading_engine that creates a sophisticated financial trading system with advanced market analysis and risk calculations.
Requirements:
Function name: trading_engine
result1 = trading_engine("TECH", 150.0, 5000, 15.0, 6, 5)
result2 = trading_engine("ENERGY", 45.0, 5000, 15.0, 4, 8)
result3 = trading_engine("FINANCE", 220.0, 5000, 8.0, 9, 4)
Takes 6 parameters: stock_symbol, current_price, volume_shares, volatility_percent, market_trend, risk_tolerance
Calculate position_value: current_price × volume_shares
Calculate volatility_factor: (volatility_percent ÷ 100) × position_value
Calculate trend_multiplier: market_trend × risk_tolerance ÷ 10
Calculate risk_adjusted_return: (position_value × trend_multiplier) ÷ (volatility_factor + 1)
Calculate portfolio_weight: position_value ÷ (position_value + volatility_factor + 1000000)
Calculate trading_signal: (risk_adjusted_return × portfolio_weight) - volatility_factor
Create trading_signature: first4_symbol + price_category + volume_class + trend_indicator
Calculate algorithm_score: (trading_signal + risk_adjusted_return) × (100 - volatility_percent) ÷ 100
Return formatted string: "TRADING: SYMBOL | PRICE: $P.P | VALUE: $V | VOLATILITY: F.F | RETURN: R.R | WEIGHT: W.W% | SIGNAL: S.S | SIG: SIGNATURE | SCORE: SC.SC"
Round price, volatility factor, return, weight, signal, and score to 1 decimal place
Classification Logic:
price_category: "L" (≤50), "M" (51-200), "H" (>200)
volume_class: "S" (≤1000), "M" (1001-10000), "L" (>10000)
trend_indicator: "B" (trend ≤ 0), "N" (0 < trend ≤ 5), "U" (trend > 5)
TRADING: TECH | PRICE: $150.0 | VALUE: $750000 | VOLATILITY: 112500.0 | RETURN: 4500.0 | WEIGHT: 86.7% | SIGNAL: 4387.5 | SIG: TECHMMU | SCORE: 6532.5
TRADING: ENERGY | PRICE: $45.0 | VALUE: $225000 | VOLATILITY: 33750.0 | RETURN: 2000.0 | WEIGHT: 86.7% | SIGNAL: 1966.3 | SIG: ENER5MSN | SCORE: 3966.3
TRADING: FINANCE | PRICE: $220.0 | VALUE: $1100000 | VOLATILITY: 88000.0 | RETURN: 7920.0 | WEIGHT: 92.4% | SIGNAL: 7832.0 | SIG: FINAHU | SCORE: 15752.0 """

# def main 
def main():
    # set storing variables for calling function with inputs specific for each profile / "text",numbers
    result1 = trading_engine("TECH", 150.0, 5000, 15.0, 6, 5)
    result2 = trading_engine("ENERGY", 45.0, 5000, 15.0, 4, 8)
    result3 = trading_engine("FINANCE", 220.0, 5000, 8.0, 9, 4)
    # print the items stored in storing variable
    print(result1)
    print(result2)
    print(result3)

# def calling function with parameters 
def trading_engine(stock_symbol, current_price, volume_shares, volatility_percent, market_trend, risk_tolerance):
    # all imp calculations 
    position_value = current_price * volume_shares
    volatility_factor = (volatility_percent / 100) * position_value
    trend_multiplier = market_trend * risk_tolerance / 10
    risk_adjusted_return = (position_value * trend_multiplier) / (volatility_factor + 1)
    portfolio_weight = position_value / (position_value + volatility_factor + 1000000)
    trading_signal = (risk_adjusted_return * portfolio_weight) - volatility_factor
    # getting trading signatire bases
    first4_symbol = stock_symbol[:4]
    price_category = "L"*(current_price<=50) + "M"*(51<current_price<=200) + "H"*(current_price>200)
    volume_class = "S" * (volume_shares<=1000) + "M" * (1001<volume_shares<=10000) + "L"* (volume_shares>10000)
    trend_indicator = "B"*(market_trend <= 0) + "N"*(0 < market_trend <= 5) + "U"*(market_trend > 5)
    # calculate sig and algo score
    trading_signature = first4_symbol + price_category + volume_class + trend_indicator
    algorithm_score = (trading_signal + risk_adjusted_return) * (100 - volatility_percent) / 100

    # return f string 
    return f"TRADING: {stock_symbol.upper()} | PRICE: ${current_price:0.1f} | VALUE: ${position_value} | VOLATILITY: {volatility_factor:0.1f} | RETURN: {risk_adjusted_return:0.1f} | WEIGHT: { portfolio_weight:0.1f}% | SIGNAL: {trading_signal:0.1f} | SIG: { trading_signature.upper()} | SCORE: {algorithm_score:0.1f}"

# calling main
main()
