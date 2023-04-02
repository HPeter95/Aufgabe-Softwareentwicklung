import paho.mqtt.client as mqtt
from random import uniform
import time


client = mqtt.Client("Planungsalgorithmus")
client.connect("localhost", 1883)   # normalerweise hier ip-adresse vom mosquitto Broker

#   Alternative für anderen Broker wenn 'localhost' nicht funktioniert:
#   mqttBroker ="mqtt.eclipseprojects.io"
#   client.connect(mqttBroker)

while True:
    randNumber = uniform(1000.0, 3000.0)        # Leistung Spülmaschine / Waschmaschine in Watt
    client.publish("Leistung", randNumber)
    print("Just published " + str(randNumber) + " Watt to topic Leistung")

    randNumber = uniform(30.0, 150.0)        # Dauer Spülmaschine / Waschmaschine in Minuten
    client.publish("Dauer", randNumber)
    print("Just published " + str(randNumber) + " Minuten to topic Dauer")

    time.sleep(5)