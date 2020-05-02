import json
import vars
import requests

currencies = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNH', 'HKD', 'PLN']
currencies_name = ['US DOLLAR', 'EURO', 'JAPANESE YEN', 'POUND STERLING', 'AUSTRALIAN DOLLAR', 'CANADIAN DOLLAR',
                   'SWISS FRANC', 'CHINESE RENMINBI', 'HONK KONG DOLLAR', 'POLISH ZLOTY']

crypto_currencies = ['BTC', 'ETH', 'XRP', 'LTC', 'USDT', 'BCH', 'LIBRA', 'XMR', 'EOS', 'BSV']
crypto_currencies_name = ['BITCOIN', 'ETHEREUM', 'RIPPLE', 'LITECOIN', 'TETHER', 'BITCOIN CASH', 'LIBRA', 'MONERO', 'EOS', 'Bitcoin SV']


class APIConnector:
    def __init__(self, __base_currency='EUR', __currencies={}):
        self.API_KEY = 'accde8baac00161ecf395f24a5408fcd'
        self.resource = 'http://data.fixer.io/api/'
        self.base_currency = __base_currency
        self.currencies = __currencies

    def get_rate_foreign_exchanges(self, __time):
        __url = self.resource + __time + "?access_key=" + self.API_KEY
        print("Request: ", __url)
        __response = requests.get(__url)
        if __response.status_code == 200:
            print(vars.CGREEN, "STATUS: ", __response.status_code, vars.CEND)
            __data = json.loads(__response.text)
            __date = __data['date']
            __rates = __data['rates']
            print(__date)
            print(__rates)
            for key, value in self.currencies.items():
                if __date not in self.currencies[key].date:
                    self.currencies[key].date.append(__date)
                    self.currencies[key].rate.append(__rates[key])


        else:
            print(vars.CRED, "STATUS: ", __response.status_code, vars.CEND)

        # for __currency in self.currencies:
        #     __url = self.resource + 'exchangerate/' + self.base_currency + '/' + __currency.short_name + '?time=' + __time
        #     __headers = {'X-CoinAPI-Key': self.API_KEY}
        #     __response = requests.get(__url, headers=__headers)
        #
        #     if __response.status_code == 200:
        #         print(__response.headers)
        #         __data = json.loads(__response.text)
        #         print(__data)
        #     else:
        #         print("ERROR: ", __response.status_code)

    def get_current_exchanges_rate(self):
        __url = self.resource + 'exchangerate/' + self.base_currency
        __headers = {'X-CoinAPI-Key': self.API_KEY}
        __response = requests.get(__url, headers=__headers)

        if __response.status_code == 200:
            __data = json.loads(__response.text)
            for index in range(len(__data['rates'])):
                if __data['rates'][index]['asset_id_quote'] in currencies:
                    __index = currencies.index(__data['rates'][index]['asset_id_quote'])
                    __currency = __data['rates'][index]['asset_id_quote']
                    self.currencies[__index].rate = __data['rates'][index]['rate']
                    print(__data['rates'][index])
                    print()

                # if __data['rates'][index]['asset_id_quote'] in crypto_currencies:
                #     print(__data['rates'][index])
                #     print()
            # with open("data.txt", "w") as f:
            #     f.write(__response.text)
            # print("STATUS: OK")
        else:
            print("ERROR: ", __response.status_code)
