import requests
import json
from datetime import datetime
import sys

currencies = ['USD', 'ALL', 'DZD', 'ARS', 'AMD', 'AUD', 'AZN', 'BHD', 'BDT',
'BYN', 'BMD', 'BOB', 'BAM', 'BRL', 'BGN', 'KHR', 'CAD', 'CLP', 'CNY', 'COP',
'CRC', 'HRK', 'CUP', 'CZK', 'DKK', 'DOP', 'EGP', 'EUR', 'GEL', 'GHS', 'GTQ',
'HNL', 'HKD', 'HUF', 'ISK', 'INR', 'IDR', 'IRR', 'IQD', 'ILS', 'JMD', 'JPY',
'JOD', 'KZT', 'KES', 'KWD', 'LBP', 'MKD', 'MYR', 'MUR', 'MXN', 'MDL', 'MNT',
'MAD', 'MMK', 'NAD', 'NPR', 'TWD', 'NZD', 'NIO', 'NGN', 'NOK', 'OMR', 'PKR',
'PAB', 'PEN', 'PHP', 'PLN', 'GBP', 'QAR', 'RON', 'RUB', 'SAR', 'RSD', 'SGD',
'ZAR', 'KRW', 'SSP', 'VES', 'LKR', 'SEK', 'CHF', 'THB', 'TTD', 'TND', 'TRY',
'UGX', 'UAH', 'AED', 'UYU', 'UZS', 'VND']

def convert_fiat(top, fiat):
	if fiat:
		if fiat in currencies:
			url = f"https://api.coinmarketcap.com/v1/ticker/?convert={fiat}&limit={top}"
		else:
			print("Error: Not a valid currency pair")
			sys.exit(1)
	else:
		url = f"https://api.coinmarketcap.com/v1/ticker/?limit={top}"

	date = datetime.now().time()
	print(f"Fetched data from coinmarketcap.com at {date}")

	return requests.get(url)