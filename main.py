import requests

MY_LAT = 34.052235
MY_LNG = -118.243683

api_key = "6274c1fdf81d17d702df0440ebd85f4b"
# Let's just write the OWM address here to make it even much clear:
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": api_key
}

response = requests.get(OWM_Endpoint,
                        params=parameters)
# Testify if our request is okay:
# print(response.status_code)
response.raise_for_status()
data = response.json()
print(data)


