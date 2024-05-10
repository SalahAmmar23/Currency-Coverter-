"""
we want to create 4 functions for our Currency Exchanger 
1. get currency rates from API source 
2. get user inputs like : amount to convery from what to what currency
3. convery currency function will have 4 paramaters : amount, curreny source, curreceny target, rates
4. Display the result  after converting 
"""


import requests
source_currency = ""
target_currency = ""
amount = float

# Base URL for currency API (replace with your preferred API)
API_URL = "https://api.apilayer.com/fixer/convert?to={}&from={}&amount={}".format(target_currency, source_currency, str(amount))

def get_currency_rates(base_currency="USD"):
  """
  Fetches exchange rates for various currencies from an API.

  Args:
      base_currency (str, optional): The base currency for the rates. Defaults to "USD".

  Returns:
      dict: Dictionary where keys are currency codes and values are exchange rates relative to the base currency.
  """
  try:
    response = requests.get(f"{API_URL}/{base_currency}")
    response.raise_for_status()  # Raise exception for non-200 status codes
    data = response.json()
    return data["rates"]
  except requests.exceptions.RequestException as e:
    print(f"Error fetching rates: {e}")
    return {}

def get_user_input(amount, source_currency, target_currency):
  """
  Prompts the user for amount, source currency, and target currency.

  Returns:
      dict: Dictionary containing user input for conversion.
  """
  while True:
    try:
      amount = float(input("Enter amount to convert: "))
      if amount < 0:
        raise ValueError("Amount cannot be negative")
      source_currency = input("Enter source currency (e.g., USD, EUR): ").upper()
      target_currency = input("Enter target currency (e.g., USD, EUR): ").upper()
      return {"amount": amount, "source": source_currency, "target": target_currency}
    except ValueError as e:
      print(f"Invalid input: {e}")

def convert_currency(amount, source_currency, target_currency, rates):
  """
  Calculates the converted amount based on exchange rates.

  Args:
      amount (float): Amount to convert.
      source_currency (str): Source currency code.
      target_currency (str): Target currency code.
      rates (dict): Dictionary of exchange rates.

  Returns:
      float: Converted amount in the target currency.
  """
  if source_currency not in rates or target_currency not in rates:
    print(f"Invalid currency code: {source_currency} or {target_currency}")
    return 0
  # Convert to base currency first (if not already)
  if source_currency != "USD":
    amount /= rates[source_currency]
  # Convert to target currency
  return amount * rates[target_currency]

def display_results(converted_amount, source_currency, target_currency):
  """
  Formats and displays the conversion results.

  Args:
      converted_amount (float): Converted amount.
      source_currency (str): Source currency code.
      target_currency (str): Target currency code.
  """
  print(f"{source_currency} {amount:.2f} is equivalent to {target_currency} {converted_amount:.2f}")

# Main program loop
while True:
  # Get exchange rates
  rates = get_currency_rates()
  if not rates:
    print("Failed to retrieve exchange rates. Exiting...")
    break

  # Get user input
  user_input = get_user_input(amount, source_currency, target_currency)
  amount = user_input["amount"]
  source_currency = user_input["source"]
  target_currency = user_input["target"]

  # Convert currency
  converted_amount = convert_currency(amount, source_currency, target_currency, rates)
  if converted_amount > 0:
    display_results(converted_amount, source_currency, target_currency)

  # Loop for another conversion
  choice = input("Do another conversion? (y/n): ").lower()
  if choice != "y":
    break

print("Thank you for using the currency converter!")