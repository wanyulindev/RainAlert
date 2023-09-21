import requests
from twilio.rest import Client

account_sid = 'AC6ce642cdb9e2cf3bd2d3fd03564dcf9a'
auth_token = '51d1b7adecb7bf0ae5c7bb85ed282d6b'

MY_LAT = 34.052235
MY_LNG = -118.243683
exclude_data = "current,minutely,daily"
api_key = "6274c1fdf81d17d702df0440ebd85f4b"
# Let's just write the OWM address here to make it even much clear:
# And down below are all working free:
# OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"  # current weather
OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
# OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": api_key,
    "exclude": exclude_data     # We want to only fetch what we need, exclude else.
}

response = requests.get(OWM_Endpoint,
                        params=parameters)
# Testify if our request is okay:
# print(response.status_code)
response.raise_for_status()
data = response.json()
# print(data)
# print(data["hourly"][:13])
within_12hours = data["hourly"][:12]
will_rain = False
for item in within_12hours:
    # What I wrote:
    # print(item["weather"])
    # for i in item["weather"]:
    #     print(i["id"])
    #     if i["id"] < 700:
    #         print("it will rain")   # This is where need to put "Sending Out SMS" coding.
    #  if item["weather"]["id"] < 700:
    #      print(f"It will rain! {item['weather']['id']}")
    # print(item["weather"]["id"])

    # What dr.Angela wrote:
    # print(item["weather"][0]["id"])
    condition_code = item["weather"][0]["id"]
    if condition_code < 700:
        # print("it will rain")     # instead printing every < 700 would rain:
        will_rain = True    # Let's write it as only once, so we will bring umbrella next 12 hrs.

if will_rain:
    # print("Bring an umbrella")
    # Using Twilio:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+18444821071',
        body='It gonna rain today! Bring an umbrella :) 🙂☔️🌧',
        to='+16268736132'
    )
    print(message.status)
    print(message.sid)




