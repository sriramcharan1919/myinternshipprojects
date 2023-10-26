import requests
def currency_converter():
    amount = float(input("Enter the amount to convert: "))
    source_currency = input("Enter the source currency: ").upper()
    target_currency = input("Enter the target currency: ").upper()
    api_key = "YOUR_API_KEY" 
    url = f"https://api.exchangerate-api.com/v4/latest/{source_currency}"
    response = requests.get(url)
    data = response.json()
    if response.status_code != 200 or 'error' in data:
        print("Failed to fetch exchange rates. Please try again later.")
        return
    exchange_rate = data['rates'].get(target_currency)
    if not exchange_rate:
        print(f"Unsupported target currency: {target_currency}. Please choose a different currency.")
        return
    converted_amount = amount * exchange_rate
    print(f"{amount:.2f} {source_currency} is equal to {converted_amount:.2f} {target_currency}.")
    print(f"Exchange rate: 1 {source_currency} = {exchange_rate:.4f} {target_currency}.")
currency_converter()
