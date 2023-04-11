import paho.mqtt.client as mqtt
import random
import time
import json
from datetime import datetime, timedelta

current_time = datetime.now()
def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))
    client.publish("Wetterdaten", Wetterdaten_json)
    print("Just published " + str(Wetterdaten_json) + " to topic Wetterdaten")

# Wetterdaten vom heutigen Tag bis maximal dem folgenden Tag als Unix Timestamp ausgeben:
Wetterdaten = [
    ["aktuelle Zeit", 0],
    ["aktuelle Zeit + 6 Stunden", 0],
    ["aktuelle Zeit + 12 Stunden", 0],
    ["aktuelle Zeit + 18 Stunden", 0],
    ["aktuelle Zeit + 24 Stunden", 0],
    ["aktuelle Zeit + 1 Tag 6 Stunden", 0],
    ["aktuelle Zeit + 1 Tag 12 Stunden", 0],
    ["aktuelle Zeit + 1 Tag 18 Stunden", 0],
    ["aktuelle Zeit + 1 Tag 24 Stunden", 0],
]
# Spalte 0 wird in Reihe 0 die aktuelle Zeit zugewiesen, alle nachfolgenden Zeilen haben 6 Stunden mehr
# Spalte 1 des Arrays Wetterdaten wird ein Sonnenintensitätsfaktor von 0 bis 10 zugewiesen:
for sub_array in Wetterdaten:
    sub_array[0] = int(current_time.timestamp())
    current_time += timedelta(hours=6)
    sub_array[1] = random.random() * 10

# Array in JSON string konvertieren
Wetterdaten_json = json.dumps(Wetterdaten)

client = mqtt.Client("Wetterserver")
client.connect("localhost", 1883)

client.loop_start()
client.subscribe("MaxStartzeitpunkt2")
client.on_message = on_message

time.sleep(30)
client.loop_stop()
