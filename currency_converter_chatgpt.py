import requests

# API URL and headers
url = "https://api.apilayer.com/fixer/convert"
headers= {"apikey": "mdrCUDc3EZeE4NLyZemERaT5PMedpoYQ"}

# Get user input
from_currency = input("Enter the source currency (EGP, AED...) : ").upper()
to_currency = input("Enter the target currency (EGP, AED...): ").upper()
amount = float(input("Enter the amount to convert: "))

# Construct payload
payload = {"to": to_currency, "from": from_currency, "amount": amount}

# Make API request
response = requests.get(url, headers=headers, params=payload)

# Check response status code
status_code = response.status_code

# Get result
result = response.text

# Print result
if response.status_code == 200:
    result = response.json()
    print(f"{amount} {from_currency} is equivalent to {result['result']} {to_currency}")
else:
    print(f"Error: HTTP Status Code {response.status_code}")
