# Import necessary modules
import requests  # Module for sending HTTP requests
import json      # Module for working with JSON data

# Welcome message with an emoji
print("\n🌦️ Welcome to the Weather Information App! 🌈\n\n")

# Prompt the user to input the name of the city
city = input("Enter the name of the city: ")

# Create the URL for the WeatherAPI request
# Replace 'YOUR_API_KEY' with your actual API key
URL = f"http://api.weatherapi.com/v1/current.json?key=4c8fc4835fcd42e594d231853232208&q={city}"

# Send a GET request to the WeatherAPI and store the response
response = requests.get(URL)  # Send GET request to the specified URL
data = json.loads(response.text)  # Parse the JSON response into a Python dictionary

# Extracting and printing specific weather information

# Extract location details from the response
location = data['location']
# Extract current weather details from the response
current = data['current']

# Print location details including city name, region, and country
print(f"Location: {location['name']}, {location['region']}, {location['country']}")
# Print the local time of the city
print(f"Local Time: {location['localtime']}")
# Print temperature in both Celsius and Fahrenheit
print(f"Temperature: {current['temp_c']}°C ({current['temp_f']}°F)")
# Print the weather condition description
print(f"Condition: {current['condition']['text']}")

# Thank you message with emojis
print("\n🌞 Thank you for using our weather service! Have a great day! ☔️")
