import requests
import config
#import RPi.GPIO as GPIO

def send_api_message(parameters):
    r=requests.post(url=config.SIPAS_BACKEND_URL, data=parameters)
    data = r.json()
    return data["data"]

#def setupGPIO(gpio):
#    GPIO.setmode(GPIO.BCM)
#    GPIO.setwarnings(False)
#    GPIO.setup(gpio, GPIO.OUT)