import paho.mqtt.client as mqtt
from random import uniform
import time, random
import json
from datetime import datetime, timedelta




def on_message(client, userdata, message):
    print(f"received message: {str(message.payload.decode('utf-8'))} on topic: {message.topic}")

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
random_Uhrzeit_Unix = 300

client = mqtt.Client("Haushaltsgerät")
client.connect("localhost", 1883)   # normalerweise hier ip-adresse vom mosquitto Broker
client.loop_start()
client.subscribe("Startzeitpunkt")
client.on_message = on_message

#   Alternative für anderen Broker wenn 'localhost' nicht funktioniert:
#   mqttBroker ="mqtt.eclipseprojects.io"
#   client.connect(mqttBroker)

while True:
    randNumber1 = 50      # Leistung Spülmaschine / Waschmaschine in Watt
   # client.publish("Leistung", randNumber1)
    print("Just published " + str(randNumber1) + " Watt to topic Leistung")

    randNumber2 = 100      # Dauer Spülmaschine / Waschmaschine in Minuten
   # client.publish("Dauer", randNumber2)
    print("Just published " + str(randNumber2) + " Minuten to topic Dauer")

    #client.publish("MaxStartzeitpunkt", random_Uhrzeit_Unix)
    print("Just published " + str(random_Uhrzeit_Unix) + " in Sekunden to topic MaxStartzeitpunkt")

# Topics zu Json formatieren
    Topics_Client_1 = [randNumber1, randNumber2, random_Uhrzeit_Unix]
    Topics_Client_1_json = json.dumps(Topics_Client_1)
    client.publish("Topics_Client_1", Topics_Client_1_json)

    time.sleep(5)

