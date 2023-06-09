import paho.mqtt.client as mqtt
from random import uniform
import time, random
import json
from datetime import datetime, timedelta


def on_message(client, userdata, message):
    print(f"Received message: {str(message.payload.decode('utf-8'))} on topic: {message.topic}")

    if message.topic == "Startzeitpunkt":
        Startzeitpunkt_Unix = float(message.payload.decode())
        Startzeitpunkt_readable = datetime.fromtimestamp(Startzeitpunkt_Unix)
        print("Der optimale Startzeitpunkt ist", Startzeitpunkt_readable)

# Aktuelle Uhrzeit
Uhrzeit = datetime.now()

# Zufällige Uhrzeit zwischen jetzt und in genau 2 Tagen
random_Uhrzeit = Uhrzeit + timedelta(days=random.randint(0, 2),
                              hours=random.randint(0, 23),
                              minutes=random.randint(0, 59),
                              seconds=random.randint(0, 59))

# Konvertieren von random_Uhrzeit in Unix timestamp Format
random_Uhrzeit_Unix = int(time.mktime(random_Uhrzeit.timetuple()))

client = mqtt.Client("Haushaltsgerät_1")
client.connect("localhost", 1883)   # normalerweise hier ip-adresse vom mosquitto Broker
client.loop_start()
client.subscribe("Startzeitpunkt")
client.on_message = on_message

#   Alternative für anderen Broker wenn 'localhost' nicht funktioniert:
#   mqttBroker ="mqtt.eclipseprojects.io"
#   client.connect(mqttBroker)

while True:
    randNumber1 = uniform(1000, 3000)        # Leistung Spülmaschine / Waschmaschine in Watt
    print("Just published " + str(randNumber1) + " Watt to topic Leistung")

    randNumber2 = uniform(30, 150)        # Dauer Spülmaschine / Waschmaschine in Minuten
    print("Just published " + str(randNumber2) + " Minuten to topic Dauer")

    print("Just published " + str(random_Uhrzeit_Unix) + " in Sekunden to topic MaxStartzeitpunkt")

    Client_Name = "Haushaltsgerät_1"

# Topics zu Json formatieren
    Topics_Client_1 = [Client_Name, randNumber1, randNumber2, random_Uhrzeit_Unix]
    Topics_Client_1_json = json.dumps(Topics_Client_1)
    client.publish("Topics_Client_1", Topics_Client_1_json)

    time.sleep(5)

