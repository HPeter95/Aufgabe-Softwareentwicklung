import paho.mqtt.client as mqtt
import time
import json

value1 = 0
value2 = 0

now = time.time()

def on_message(client, userdata, message):
    global value1, value2, wetterdaten, MaxStartzeitpunkt,wetterdaten_MaxStartzeitpunkt  # damit die Werte der topics separat angesteuert werden können

    print(f"received message: {str(message.payload.decode('utf-8'))} on topic: {message.topic}")

    if message.topic == "Leistung":
        value1 = float(message.payload.decode())
    elif message.topic == "Dauer":
        value2 = float(message.payload.decode())

    elif message.topic == "Wetterdaten":
        wetterdaten = json.loads(message.payload.decode("utf-8"))
        wetterdaten_MaxStartzeitpunkt = [sub_array for sub_array in wetterdaten if now <= sub_array[0] <= MaxStartzeitpunkt]
        max_second_split = max(x[1] for x in wetterdaten_MaxStartzeitpunkt)
        for sub_array in wetterdaten_MaxStartzeitpunkt:
            if sub_array[1] == max_second_split:
                print("Der Zeitpunkt des meisten Photovoltaikstroms im Netz bis spätestens", MaxStartzeitpunkt, " ist ", sub_array[0])
                client.publish("Startzeitpunkt", sub_array[0])

    # Publishen des spätesten Startzeitpunktes "2" an den Wetterserver, da der Planungsalgorithmus
    # den Zeitpunkt weitergeben soll, nicht das Haushaltsgerät
    elif message.topic == "MaxStartzeitpunkt":
        MaxStartzeitpunkt = float(message.payload.decode())
        client.publish("MaxStartzeitpunkt2",  MaxStartzeitpunkt)
        print("Just published " + str(MaxStartzeitpunkt) + " als spätester Startzeitpunkt")

    # Hier die Berechnung des Stromverbrauchs
    if value1 != 0 and value2 != 0:  # sonst wird direkt zu Anfang result = 0 ausgespuckt
        result = value1 * value2
        print("Result:", result)


#   Alternative für anderen Broker, wenn 'localhost' nicht zur Verfügung steht:
#   mqttBroker ="mqtt.eclipseprojects.io"
#   client.connect(mqttBroker)


client = mqtt.Client("Planungsalgorithmus")
client.connect("localhost", 1883)  # normalerweise hier ip-adresse vom mosquitto Broker

client.loop_start()

client.subscribe("Leistung")
client.subscribe("Dauer")
client.subscribe("MaxStartzeitpunkt")
client.subscribe("Wetterdaten")
client.on_message = on_message

time.sleep(30)
client.loop_stop()
