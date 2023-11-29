import requests
from pprint import pprint

#url = "https://api.chucknorris.io/jokes/random"
#response = requests.request(method="GET", url=url)

#pprint(response.json())

#print()
#print(25*"*")
#print()
#print(response.json()['value'])


#Pobrać dane z https://restcountries.com/v3.1/name/Poland?fullText=true; Wyświetlić podstawowe informacje (np. il. mieszkańców, waluta itp.)
#- Stworzyć skrypt który z linii poleceń przyjmie nazwę kraju i dal niego wyświetli w/w dane.







import requests
url = "https://restcountries.com/v3.1/name/Slovakia?fullText=true"
response = requests.request(method="GET", url=url)
print()
print(25*"*")
print()
print(response.json()[0]['capital'])


# 2 wersja programu


url = "https://restcountries.com/v3.1/name/Poland?fullText=true"
response = requests.request(method="GET", url=url)
print()
print(25*"*")
print()
print(response.json()[0]['currencies'])


