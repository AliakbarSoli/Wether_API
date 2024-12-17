import requests

def API(): 
    Your_Token = input('Enter Tokne whit https://weatherstack.com: ')
    city_name = input('Entar of City Name: ') 
    url = f"http://api.weatherstack.com/current?access_key={Your_Token}&query={city_name}"
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
