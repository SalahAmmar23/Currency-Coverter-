import requests

# API endpoint for currency conversion
API_ENDPOINT = "https://api.apilayer.com/fixer/convert"
API_KEY = "mdrCUDc3EZeE4NLyZemERaT5PMedpoYQ"  # Replace with your API key

def get_currency_rates(amount, source_currency, target_currency):
  """
  Fetches the conversion rate for a specific conversion using fixer.io API.

  Args:
      amount (float): Amount to convert.
      source_currency (str): Source currency code.
      target_currency (str): Target currency code.

  Returns:
      float: Conversion rate (target currency per unit of source currency), or None on error.
  """
  url = f"{API_ENDPOINT}?to={target_currency}&from={source_currency}&amount={amount}&apikey={API_KEY}"
  try:
    response = requests.get(url)
    response.raise_for_status()  # Raise exception for non-200 status codes
    data = response.json()
    if "success" in data and data["success"]:
      return data["info"]["rate"]
    else:
      print(f"API error: {data['error']['info']}")
      return None
  except requests.exceptions.RequestException as e:
    print(f"Error fetching rates: {e}")
    return None

def get_user_input():
  """
  Prompts the user for amount, source currency, and target currency.

  Returns:
      dict: Dictionary containing user input for conversion.
  """
  while True:
    try:
      source_currency = input("Enter source currency (e.g., USD, EUR): ").upper()
      target_currency = input("Enter target currency (e.g., USD, EUR): ").upper()
      amount = float(input("Enter amount to convert: "))
      if amount < 0:
        raise ValueError("Amount cannot be negative")
      return {"amount": amount, "source": source_currency, "target": target_currency}
    except ValueError as e:
      print(f"Invalid input: {e}")

def convert_currency(amount, source_currency, target_currency):
  """
  Calculates the converted amount based on the retrieved conversion rate.

  Args:
      amount (float): Amount to convert.
      source_currency (str): Source currency code.
      target_currency (str): Target currency code.

  Returns:
      float: Converted amount in the target currency, or None on error.
  """
  rate = get_currency_rates(amount, source_currency, target_currency)
  if rate is not None:
    return amount * rate
  else:
    return None

def display_results(converted_amount, source_currency, target_currency):
  """
  Formats and displays the conversion results.

  Args:
      converted_amount (float): Converted amount.
      source_currency (str): Source currency code.
      target_currency (str): Target currency code.
  """
  if converted_amount is not None:
    print(f"{source_currency} {amount:.2f} is equivalent to {target_currency} {converted_amount:.2f}")
  else:
    print("Conversion failed. Please try again.")

# Main program loop
while True:
  # Get user input
  user_input = get_user_input()
  amount = user_input["amount"]
  source_currency = user_input["source"]
  target_currency = user_input["target"]

  # Convert currency
  converted_amount = convert_currency(amount, source_currency, target_currency)
  display_results(converted_amount, source_currency, target_currency)

  # Loop for another conversion
  choice = input("Do another conversion? (y/n): ").lower()
  if choice != "y":
    break

print("Thank you for using the currency converter!")
