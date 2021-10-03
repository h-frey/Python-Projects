import requests
from tkinter import*
import tkinter as tk
from tkinter import ttk


# Todo - Ask for input from the user (amount and currency)
currency_from = input(
    "Enter the currency you would like to convert from: ").upper()
currency_to = input(
    "Enter the currency you would like to convert to: ").upper()
amount = float(input("Enter the amount you would like to convert: "))
   

def converter(currency_from, currency_to, amount):
    # Todo - Connect to the api
    rates = {}
    url = "https://v6.exchangerate-api.com/v6/fdf7a7843bc0a6d00c03f3c8/latest/USD"
    response = requests.get(url)
    data = response.json()
    rates = data["conversion_rates"]

    # Todo- Check in the database for the  exchange rate
    if currency_from in rates.keys() and currency_to in rates.keys():
        exchange_value = rates[currency_from]
        # Todo - Perform  the conversion
        # first convert the amount into USD if it is not in USD because usd is base currency
        if currency_from != "USD":
            final_amount = round(amount / exchange_value, 2)

        final_amount = round(amount * rates[currency_to], 2)
        # Todo - Output the final conversion
        return final_amount
    else:
        print("not in ")



print(converter(currency_from, currency_to,amount))