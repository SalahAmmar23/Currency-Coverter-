"""
we want to create 4 functions for our Currency Exchanger 
1. get currency rates from API source 
2. get user inputs like : amount to convery from what to what currency
3. convery currency function will have 4 paramaters : amount, curreny source, curreceny target, rates
4. Display the result  after converting 
"""
import requests 


source_currency = input("Enter the Source Currency (EGP, AED...) : ")
target_currency = input("Enter the target Currency (EGP, AED...) : ")

while True:
    try:
        amount = float(input("Enter the amount: "))    
    except ValueError as er:
        print("Invalid input {}".format(er))
        continue
    
    if amount == 0:
        print("The Amount must be greater than Zero")
    else:
        break



url = "https://api.apilayer.com/fixer/convert?to={}&from={}&amount={}".format(target_currency, source_currency, str(amount))

payload = {}
headers= {
  "apikey": "mdrCUDc3EZeE4NLyZemERaT5PMedpoYQ"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
if(status_code != 200):
    print("Sorry, There was a problem. Please try again later.")
    quit()
result = response.json()
converted_amount = result['result']
print("{} {} = {} {} ".format(amount, source_currency,converted_amount, target_currency ))
