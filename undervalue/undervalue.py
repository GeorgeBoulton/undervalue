import yfinance as yf
import finnhub as fh
import requests
import json

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

def calculateFinancials(tickerSymbol):
    # Get YFinance ticker
    ticker = yf.Ticker(tickerSymbol)
    info = ticker.info

    eps = info["trailingEps"]
    sharePrice = info["previousClose"]
    bookValue = info["bookValue"]
    
    #PE
    peRatio = round(sharePrice/eps, 2)

    #PEG
    pegRatio = info["pegRatio"]

    #PB   
    pbRatio = round(sharePrice/bookValue, 2)

    #Current Ratio
    currentRatio = 0

    return [tickerSymbol, eps, peRatio, pegRatio, pbRatio, currentRatio]

    # print("EPS on " + tickerSymbol + "=" + str(eps))
    # print("P/E on " + tickerSymbol + "=" + str(peRatio))
    # print("PEG on " + tickerSymbol + "=" + str(pegRatio))



tickersList = []
financialsList = []
tagsList = ["Ticker", "EPS", "P/E Ratio", "PEG Ratio", "P/B Ratio", "Current Ratio"]

tickersList = getTickers(finnhub_client.stock_symbols('US')[0:200])

count = 0
for tickerSymbol in tickersList:
    #print(str(count) + " " + tickerSymbol)
    count+=1

    try:       
        financialsList.append(calculateFinancials(tickerSymbol))

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
