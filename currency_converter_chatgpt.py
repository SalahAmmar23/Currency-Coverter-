import requests

# API URL and headers
url = "https://api.apilayer.com/fixer/convert"
headers = {"apikey": "mdrCUDc3EZeE4NLyZemERaT5PMedpoYQ"}

while True:
    # Get user input
    from_currency = input("Enter the source currency code: ").upper()
    to_currency = input("Enter the target currency code: ").upper()
    amount = float(input("Enter the amount to convert: "))

    # Construct payload
    payload = {"to": to_currency, "from": from_currency, "amount": amount}

    # Make API request
    response = requests.get(url, headers=headers, params=payload)

    # Check response status code and print result for the user
    if response.status_code == 200:
        result = response.json()
        print(f"{amount} {from_currency} is equivalent to {result['result']} {to_currency}")
    else:
        print(f"Error: HTTP Status Code {response.status_code}")

    # Ask user if they want to perform another conversion
    choice = input("Do you want to perform another conversion? (yes/no): ").lower()
    if choice != "yes":
        break

print("Thank you for using the currency converter!")
