from api_connector import APIConnector
from foreign_exchange import ForeignExchange


if __name__ == "__main__":

    with open("currencies.txt", "r") as file:
        data = file.read()
    data = data.split(',\n')

    __currency = {}
    for currency in data:
        __currency[currency.split(':')[0]] = ForeignExchange(currency.split(':')[0], currency.split(':')[1])
    api_connector = APIConnector('USD', __currency)
    api_connector.get_rate_foreign_exchanges("2020-04-01")
    api_connector.get_rate_foreign_exchanges("2020-04-02")
    api_connector.get_rate_foreign_exchanges("2020-04-03")
    api_connector.get_rate_foreign_exchanges("2020-04-04")
    api_connector.get_rate_foreign_exchanges("2020-04-05")

    for key, value in __currency.items():
        value.get_rate()
