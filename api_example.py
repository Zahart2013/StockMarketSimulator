from alpha_vantage.timeseries import TimeSeries
import ssl
import json


def data_creator(companies):
    data = {}

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    ts = TimeSeries(key='PCT8XEO3EICMQ5T2', output_format='json')
    for each in companies:
        raw_data = ts.get_daily(symbol=each, outputsize="full")
        company_data = []
        for key in raw_data[0].keys():
            company_data.append({key: raw_data[0][key]})
            if len(company_data) == 10:
                break
        data[each] = company_data
    with open("data.json", "w") as json_file:
        json.dump(data, json_file)


if __name__ == '__main__':
    data_creator(["MSFT", "CSCO", "AAPL", "INTC"])
