import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))

#   Alternative für anderen Broker wenn 'localhost' nicht funktioniert:
#   mqttBroker ="mqtt.eclipseprojects.io"
#   client.connect(mqttBroker)

client = mqtt.Client("Haushaltsgerät")
client.connect("localhost", 1883)       #normalerweise hier ip-adresse vom mosquitto Broker

client.loop_start()

client.subscribe("Startzeitpunkt")
client.on_message = on_message

time.sleep(30)
client.loop_stop()