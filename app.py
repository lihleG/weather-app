import requests 

#API KEY for OpenWeatherMap
API_KEY = "1668430b8a5a4d72608b30feaf9b6172"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

#Ask the user for a city
city = input("Enter a city: ")

# Build the API request URL
url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

#send the request
response = requests.get(url)

#convert the response into JSON (python dictionary)
data = response.json()

#check if the city exists
if data["cod"] == 200:
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]
    print(f"Temperature in {city}: {temperature}°C")
    print(f"Weather: {description}")

else:
    print("city not found, try again")