import paho.mqtt.client as mqtt
from random import uniform
import time, random
from datetime import datetime, timedelta

def on_message(client, userdata, message):
    print(f"received message: {str(message.payload.decode('utf-8'))} on topic: {message.topic}")

# Aktuelle Uhrzeit
Uhrzeit = datetime.now()

# Zufällige Uhrzeit zwischen jetzt und in genau 2 Tagen
random_Uhrzeit = Uhrzeit + timedelta(days=random.randint(0, 2),
                              hours=random.randint(0, 23),
                              minutes=random.randint(0, 59),
                              seconds=random.randint(0, 59))

# Konvertieren von random_Uhrzeit in Unix timestamp Format
random_Uhrzeit_Unix = int(time.mktime(random_Uhrzeit.timetuple()))

client = mqtt.Client("Haushaltsgerät")
client.connect("localhost", 1883)   # normalerweise hier ip-adresse vom mosquitto Broker
client.loop_start()
client.subscribe("Startzeitpunkt")
client.on_message = on_message

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

    client.publish("MaxStartzeitpunkt", random_Uhrzeit_Unix)
    print("Just published " + str(random_Uhrzeit_Unix) + " in Sekunden to topic MaxStartzeitpunkt")

    time.sleep(5)

