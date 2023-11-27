import requests

url = "https://covid-193.p.rapidapi.com/history"

querystring = {}

headers = {
	"X-RapidAPI-Key": "7c97880d88msh385904ea8bbf2efp1265a2jsn984f1daf83a4",
	"X-RapidAPI-Host": "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)