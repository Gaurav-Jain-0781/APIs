import time
from libs.exchange_rate import ClientExchangeRate

app_id = "1d0ba6cbabc74e578fc71fdd4a667af0"
client = ClientExchangeRate(app_id)

start = time.time()
usd_amount = 1000
gbp_converted = client.convert(usd_amount, "USD", "GBP")
end = time.time()

print(end - start)
print(f"{usd_amount} USD  is {gbp_converted} GBP.")
