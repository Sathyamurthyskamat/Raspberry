import sys
import Adafruit_DHT
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("file.json")
firebase_admin.initialize_app(cred,{'https://rasp-f69dc-default-rtdb.firebaseio.com/'},None)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    users_ref = ref.child('Data')
    users_ref.set({"data": {
        'Temperature': 'Temp: {0:0.1f} C'.format(temperature),
        'Humidity': 'Humidity: {1:0.1f} %'.format(humidity)} })
    #print 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
    time.sleep(1)
