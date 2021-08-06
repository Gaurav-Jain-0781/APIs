import requests
from cachetools import cached, TTLCache


class ClientExchangeRate:
    base_url = "https://openexchangerates.org/api"

    def __init__(self, app_id):
        self.app_id = app_id

    @property
    @cached(cache=TTLCache(maxsize=2, ttl=900 ))
    def latest(self):
        return requests.get(f"{self.base_url}/latest.json?app_id={self.app_id}").json()

    def convert(self, initial_amount, from_currency, to_currency):
        rates = self.latest['rates']
        to_rate = rates[to_currency]

        if from_currency == 'USD':
            return initial_amount * to_rate
        else:
            to_usd = initial_amount / rates[from_currency]
            return to_usd * to_rate
