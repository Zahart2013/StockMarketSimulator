import requests
import time


def training_data(company, key):
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
    for time in output['Time Series (Daily)']:
        if count == 0:
            result_10 = float(output['Time Series (Daily)'][time]['4. close'])
        elif count >= 10:
            prices.append(float(output['Time Series (Daily)'][time]['4. close']))
        count += 1
        if len(prices) == 30:
            break
    prices.reverse()
    return prices, result_10


def generate():
    companies = ['AAPL', 'AMD', 'AMZN', "INTC", "MSFT", "CSCO", "GPRO", "NVDA"]
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
    return prices, results
