
# Standard library imports
import requests
import json

# Third party imports
import finnhub as fh

# Local imports
import finanicals as fi

nasdaq = "XNGS"
nyse = "XNYS"


# Setup client
finnhub_client = fh.Client(api_key="c0jt0n748v6qqehfm94g")

# Extract tickers from relevant markets
def getTickers(tickers):
    tickersList = []

    for ticker in tickers:
        symbol = ticker["displaySymbol"]
        market = ticker["mic"]

        if market == nasdaq or market == nyse:
            tickersList.append(symbol)
    
    return tickersList





tickersList = []
financialsList = []
tagsList = ["Ticker", "Trailing EPS", "P/E Ratio", "PEG Ratio", "P/B Ratio", "Current Ratio"]

tickersList = getTickers(finnhub_client.stock_symbols('US')[0:200])

count = 0
for tickerSymbol in tickersList:
    #print(str(count) + " " + tickerSymbol)
    count+=1

    try:       
        financialsList.append(fi.calculateFinancials(tickerSymbol))

    except:
        print("Not enough info on " + tickerSymbol)
        continue

row_format = "{:>15}" * (len(tagsList) + 1)
print(row_format.format("", *tagsList))
for stock in financialsList:
    try:
        print (row_format.format("",*stock))
    except:
        continue
