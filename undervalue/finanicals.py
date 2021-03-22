# Standard library imports
import requests
import json

# Third party imports
import yfinance as yf
import finnhub as fh

finnhub_client = fh.Client(api_key="c0jt0n748v6qqehfm94g")

def calculateFinancials(tickerSymbol):
    # Get YFinance ticker
    ticker = yf.Ticker(tickerSymbol)
    info = ticker.info
      

    eps = info["trailingEps"]
    sharePrice = info["previousClose"]
    bookValue = info["bookValue"]
    totalAssets = info["totalAssets"]
    

    #PE
    peRatio = round(sharePrice/eps, 2)

    #PEG
    pegRatio = info["pegRatio"]

    #PB   
    pbRatio = round(sharePrice/bookValue, 2)

    #Current Ratio
    currentRatio = getCurrentRatio(tickerSymbol)

    return [tickerSymbol, eps, peRatio, pegRatio, pbRatio, currentRatio]

    # print("EPS on " + tickerSymbol + "=" + str(eps))
    # print("P/E on " + tickerSymbol + "=" + str(peRatio))
    # print("PEG on " + tickerSymbol + "=" + str(pegRatio))


def getCurrentRatio(tickerSymbol):
    basicFinancials = finnhub_client.company_basic_financials(tickerSymbol, 'all')

    return basicFinancials["series"]["annual"]["currentRatio"][0]["v"]
    