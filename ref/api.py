import requests, json 

from datetime import datetime

today =  datetime.today().strftime('%d-%m-%Y')

print(today)


url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=834002&date=16-07-2021"

# https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=834002&date=16-07-2021 


response = requests.get(url).json() 

print(response["sessions"][5]["available_capacity"])