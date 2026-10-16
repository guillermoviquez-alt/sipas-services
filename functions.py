import requests
import config
#import RPi.GPIO as GPIO

def send_api_message(parameters):
    headers = {}
    r=requests.post(url=config.SIPAS_BACKEND_URL+"/v4/api_private/", json=parameters, headers=headers)
    data = r.json()
    return data["data"]
