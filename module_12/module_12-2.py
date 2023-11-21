import requests

city = input('Please enter the city you want to check the weather.\n')
key = '2c7e3f1b843faeae23a7cc3596808dc8'
request = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'
response = requests.get(request).json()
condition = response['weather'][0]['description']
temperature = round(response['main']['temp'] - 273.15, 2)
print(f'The weather in {city} is {condition}. Current temperature is {temperature}℃.')