import requests, json, sys
from requests import Request, Session
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

from secret import key

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

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




def fetchAPIData(currency):
	url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
	parameters = {
		'start':'1',
		'limit':'1',
		'convert':currency
	}
	headers = {
		'Accepts': 'application/json',
	
		'X-CMC_PRO_API_KEY': key
	}

	session = Session()
	session.headers.update(headers)
	res = session.get(url, params = parameters)
	data = json.loads(res.text)
	a = data['data']
	return a

@app.route('/')
def homepage():
	selectedCurrency = 'USD'
	a = fetchAPIData(currency = selectedCurrency)
	
	for i in a:
		crypto_name = i['name']
		last_updated = i['last_updated']
		market_cap = i['quote'][selectedCurrency]['market_cap']
		price = i['quote'][selectedCurrency]['price']
		volume_24h = i['quote'][selectedCurrency]['volume_24h']

	return render_template(
		'index.html', 
		currencies = currencies, 
		selectedCurrency = selectedCurrency,
		last_updated = last_updated,
		market_cap = market_cap,
		price = price,
		volume_24h = volume_24h,
		crypto_name = crypto_name
	)

@app.route('/search', methods=['POST'])
def search():
	if request.method == 'POST':
		selectedCurrency = request.form['currency']
		a = fetchAPIData(currency = selectedCurrency)

		for i in a:
			crypto_name = i['name']
			last_updated = i['last_updated']
			market_cap = i['quote'][selectedCurrency]['market_cap']
			price = i['quote'][selectedCurrency]['price']
			volume_24h = i['quote'][selectedCurrency]['volume_24h']

		return render_template(
			'index.html', 
			currencies = currencies, 
			selectedCurrency = selectedCurrency,
			last_updated = last_updated,
			market_cap = market_cap,
			price = price,
			volume_24h = volume_24h,
			crypto_name = crypto_name
		)