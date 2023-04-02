import paho.mqtt.client as mqtt
from random import uniform
import time
import json

Wetterdaten = [
    ["0:00 Uhr", 0],
    ["6:00 Uhr", 1],
    ["12:00 Uhr", 7],
    ["18:00 Uhr", 5.2],
]
# Convert the array to a JSON string
Wetterdaten_json = json.dumps(Wetterdaten)

client = mqtt.Client("Wetterserver")
client.connect("localhost", 1883)



while True:
    randNumber = uniform(1000.0, 3000.0)        # evtl random Nummern von 1-10 als Sonnenscheinindex
    client.publish("Wetterdaten", Wetterdaten_json)
    print("Just published " + str(Wetterdaten_json) + " to topic Wetterdaten")

    time.sleep(5)