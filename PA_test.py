import paho.mqtt.client as mqtt
import time
import json
from datetime import datetime


def on_message(client, userdata, message):
    global var1, var2, var3

    Client_Topics_Array = json.loads(message.payload.decode("utf-8"))

    print(f"Received message: {Client_Topics_Array}")

    var1 = Client_Topics_Array[0]
    var2 = Client_Topics_Array[1]
    var3 = Client_Topics_Array[2]

    print(f"Type of var1: {type(var1)}")
    print(f"Type of var2: {type(var2)}")
    print(f"Type of var3: {type(var3)}")

    var1 = int(var1)
    var2 = int(var2)
    var3 = int(var3)

    print(var1, var2, var3)

    client.publish("MaxStartzeitpunkt2", str(var1))
    print("Just published " + str(var1) + " als spätester Startzeitpunkt")

client = mqtt.Client("Planungsalgorithmus")
client.connect("localhost", 1883)  # normalerweise hier ip-adresse vom mosquitto Broker

client.loop_start()

client.subscribe("Topics_Client_1")
client.subscribe("Wetterdaten")
client.on_message = on_message

time.sleep(30)
client.loop_stop()
