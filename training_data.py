import requests
import time


def training_data(company, key):
    """
    Creates training data for one company
    :param company: str - company's name
    :param key: str - API key
    :return: training data
    """
    global result_10
    data = {"function": 'TIME_SERIES_DAILY',
            "symbol": company,
            "outputsize": 'compact',
            "datatype": "json",
            "apikey": key}
    prices = []
    output = requests.get("https://www.alphavantage.co/query",
                          data).json()
    count = 0
    for date in output['Time Series (Daily)']:
        if count == 0:
            result_10 = float(output['Time Series (Daily)'][date]['4. close'])
        elif count >= 10:
            prices.append(float(output['Time Series (Daily)'][date]['4. close']))
        count += 1
        if len(prices) == 30:
            break
    prices.reverse()
    return prices, result_10


def generate():
    """
    Generates full set of data for AI training
    """
    companies = ['AAPL', 'AMD', 'AMZN', "INTC", "MSFT", "CSCO", "GPRO", "NVDA",
                 "FB", "COKE", "WIX", "TSLA", "NTES", "MU", "ROKU", "YAHOY",
                 "UBSFF", "NDAQ", "NICE", "WMT", "BABA", "GOOG", "IBM", 'QCOM',
                 'CMCSA', 'SPLK', "ADSK", "NFLX", "AVGO", "INTU"]
    prices = []
    results = []
    for each in companies:
        try:
            price, result = training_data(each, "PCT8XEO3EICMQ5T2")
        except:
            time1 = time.time()
            while time.time() - time1 < 60:
                continue
            price, result = training_data(each, "PCT8XEO3EICMQ5T2")
        prices.append(price)
        results.append(result)
        print("Training data downloaded")
    return prices, results
