import json, requests, sys

APPID = "c8cee080b3b7581ad1937ade7a6c2b76"

if len(sys.argv) < 2:
    print("Usage: get_weather.py city_name, 2-letter_country_code")
    sys.exit()

location = ' '.join(sys.argv[1:])
print(f"Location is: {location}")

# TODO: Download thje JSON data from OpenWeatherMap.org's API
longitude = 121.0561356357405
latitude = 14.646850195990021
url = f"https://api.openweathermap.org/data/2.5/forecast?lat={latitude}&lon={longitude}&appid={APPID}&units=metric"
response = requests.get(url)
response.raise_for_status

json_data = response.json()

print(response.text)

with open ("weather_data.json", "w") as jsonfile:
    jsonfile.write(json.dumps(json_data))


# TODO: Load JSON data into a Python Variable
print(f'{json_data["list"][0]["weather"][0]["main"]}) - {json_data["list"][0]["weather"][0]["description"]}')

print("weather tomorrow: ")
print(f'{json_data["list"][1]["weather"][0]["main"]} - {json_data["list"][1]["weather"][0]["description"]}')

print("weather day after tomorrow: ")
print(f'{json_data["list"][2]["weather"][0]["main"]} - {json_data["list"][2]["weather"][0]["description"]}')