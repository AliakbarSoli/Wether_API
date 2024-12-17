import requests

def API(): 
    city_name = input('Entar of City Name: ') 
    url = f"http://api.weatherstack.com/current?access_key=99bc7e18f9c186aa1dc445532461f0c0&query={city_name}"
    return url

def response():
    response = requests.get(API())
    json = response.json()
    if 'success' in json:
        print("Name City is Not True")
    else:
        name_city = json['request']['query']
        whether = json['current']['temperature']
        print(name_city , ': ' , whether)

response()