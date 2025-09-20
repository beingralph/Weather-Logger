import gspread
import os

from oauth2client.service_account import ServiceAccountCredentials
import requests, datetime

# Setup Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Open Google Sheet
sheet = client.open("WeatherData").sheet1

# Fetch weather
API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = os.getenv("WEATHER_CITY", "Bengaluru")
url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
data = requests.get(url).json()

if "main" in data:
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    row = [str(datetime.datetime.now()), CITY, temp, desc]
    sheet.append_row(row)
    print("Weather saved to Google Sheets:", row)
else:
    print("Error:", data.get("message", "Unexpected response"))
