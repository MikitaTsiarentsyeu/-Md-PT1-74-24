def usd_conversion(byn_currency):
    usd_currency = byn_currency * 0.31
    return usd_currency

byn_currency = float(input("Enter the amount in BYN: "))
usd_currency = usd_conversion(byn_currency)
print("The amount in USD is: ", usd_currency)





def usd_conversion(byn_currency, exchange_rate):
    usd_currency = byn_currency * exchange_rate 
    return usd_currency

byn_currency = float(input("Enter the amount in BYN: "))
exchange_rate = float(input("Enter the exchange rate: "))
usd_currency = usd_conversion(byn_currency, exchange_rate)
print("The amount in USD is: ", usd_currency)




def usd_conversion(byn_currency, exchange_rate):
    usd_currency = byn_currency * exchange_rate
    return usd_currency

while True:
    byn_currency_input = input("Enter the amount in BYN:  (or type 'end' to exit): ")
    if byn_currency_input.lower() == 'end':
        break
    byn_currency = float(byn_currency_input)
    exchange_rate = float(input("Enter the exchange rate: "))
    usd_currency = usd_conversion(byn_currency, exchange_rate)
    print("The amount in USD is: ", usd_currency)

   



