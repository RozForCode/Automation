import requests
#your api key
API_KEY = 'xyz'
url = 'http://api.openweathermap.org/data/2.5/weather'

city = input("Enter a city name: ")
request_url = f"{url}?appid={API_KEY}&q={city}"

"""
?appid={API_KEY}&q={city}: This is a query string 
that will be appended to the base URL. It contains two placeholders 
{API_KEY} and {city} which will be replaced with the values of the corresponding variables.
? appends query parameters. Q_P are key value pairs
"""
response = requests.get(request_url)
#before proceeding we'll check the response
#if status ==200, then it's successful
if response.status_code == 200:
    data = response.json()
    print('\n',data)
    print("\n\tWeather condition:"+ data['weather'][0]['description'])
    print("\n\tTemperature condition:"+str(round(data['main']['temp']-273.15,2)))
else:
    print("Error")