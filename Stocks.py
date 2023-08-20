import yfinance as yf

# 指定要获取数据的股票符号
stock_symbol = "AAPL"  # 这里使用苹果公司的股票作为示例

# 使用yfinance库获取股票数据
stock_data = yf.Ticker(stock_symbol)

# 获取历史股价数据
historical_data = stock_data.history(period="1y")  # 获取过去一年的历史数据，你可以根据需要更改时间范围

# 打印历史数据
print(historical_data)
