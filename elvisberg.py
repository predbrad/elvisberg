import yfinance as yf

"""
get_stock_data
prints the dividends, earnings and recent news for a stock
e.g.
get_stock_data("MSFT")
"""
def get_stock_data(requested_ticker):
    stock = yf.Ticker(requested_ticker)

    print(stock.dividends)
    print(stock.earnings)
    
    # TODO stock.news is a large and ugly dictionary, we'll use this soon
    # print(stock.news)

"""
get_stock_history
prints the recent prices of a stock, defaults to 1 month history
e.g.
get_stock_history("AAPL")
or
get_stock_history("AAPL","2mo")
"""
def get_stock_history(requested_ticker, requested_period="1mo"):
    stock = yf.Ticker(requested_ticker)

    print(stock.history(period=requested_period))


if __name__=="__main__":
    print("please use this tool via interactive mode")
    print("e.g.")
    print("python3 -i elvisberg.py")
