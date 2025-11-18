import requests
import os
from twilio.rest import Client

endpint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OPENWEATHER_API_KEY")
account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

weather_params = {
    "lat": 21.028511,
    "lon": 105.804817,
    "appid": api_key,
    "cnt": 4,
}

weather_response = requests.get(endpint, params=weather_params)
weather_response.raise_for_status()
weather_data = weather_response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+1234567890",
        to="Your verified phone number"
    )
    print(message.status)