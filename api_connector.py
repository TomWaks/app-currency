import datetime
import json
import vars
import requests

currencies = ['USD', 'EUR', 'JPY', 'GBP', 'AUD', 'CAD', 'CHF', 'CNH', 'HKD', 'PLN']
currencies_name = ['US DOLLAR', 'EURO', 'JAPANESE YEN', 'POUND STERLING', 'AUSTRALIAN DOLLAR', 'CANADIAN DOLLAR',
                   'SWISS FRANC', 'CHINESE RENMINBI', 'HONK KONG DOLLAR', 'POLISH ZLOTY']

crypto_currencies = ['BTC', 'ETH', 'XRP', 'LTC', 'USDT', 'BCH', 'LIBRA', 'XMR', 'EOS', 'BSV']
crypto_currencies_name = ['BITCOIN', 'ETHEREUM', 'RIPPLE', 'LITECOIN', 'TETHER', 'BITCOIN CASH', 'LIBRA', 'MONERO',
                          'EOS', 'Bitcoin SV']


class APIConnector:
    def __init__(self, __base_currency='EUR', __currencies={}):
        self.API_KEY = 'accde8baac00161ecf395f24a5408fcd'
        self.API_KEY = '0b0b16071e2db15a155ceefed86d808c'
        self.API_KEY = 'ca5c0ad8becdd6ce422fd35e704be0cf'
        self.resource = 'http://data.fixer.io/api/'
        self.base_currency = __base_currency
        self.currencies = __currencies

    def get_rate_foreign_exchanges(self, __time):
        __url = self.resource + __time + "?access_key=" + self.API_KEY + "&format=1"
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
                self.currencies[key].date.append(__date)
                try:
                    self.currencies[key].rate.append(__rates[key])
                except KeyError:
                    self.currencies[key].rate.append("-")
        else:
            print(vars.CRED, "STATUS: ", __response.status_code, vars.CEND)

    def save_data(self):
        with open("data.json", "r") as f:
            __data = json.load(f)

        __data['DATE'] = self.currencies['EUR'].date

        for key, value in self.currencies.items():
            __data[key] = value.rate



        with open('data.json', 'w') as outfile:
            outfile.write(json.dumps(__data, indent=4, sort_keys=True))

    def load_data(self):
        with open("data.json", "r") as f:
            __data = json.load(f)

        for key, value in self.currencies.items():
            self.currencies[key].date = __data['_DATE']
            self.currencies[key].rate = __data[key]

    def check_data(self):
        with open("data.json", "r") as f:
            __data = json.load(f)
        __the_last_date = datetime.datetime.strptime(__data['_DATE'][-1], "%Y-%m-%d")
        __current_date = datetime.datetime.now()

        return [str(d) for d in self.dates_bwn_twodates(__the_last_date, __current_date)]

    @staticmethod
    def dates_bwn_twodates(start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield (start_date + datetime.timedelta(n)).strftime("%Y-%m-%d")

    def update_data(self):
        __dates = self.check_data()
        print(__dates)
        for date in __dates:
            self.get_rate_foreign_exchanges(date)

        for key, value in self.currencies.items():
            value.get_rate()
        self.save_data()

