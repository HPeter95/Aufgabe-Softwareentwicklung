import paho.mqtt.client as mqtt
from random import uniform
import time


client = mqtt.Client("Planungsalgorithmus")
client.connect("localhost", 1883)   # normalerweise hier ip-adresse vom mosquitto Broker



while True:
    client.publish("MaxStartzeitpunkt2")    #"2" da der Planungsalgorithmus den zeitpunkt weitergeben soll nicht das Haushaltsgerät
    print("Just published " + str(randNumber) + " Minuten to topic Dauer")

    time.sleep(5)