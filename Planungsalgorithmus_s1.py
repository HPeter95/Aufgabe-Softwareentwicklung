import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("received message: ", str(message.payload.decode("utf-8")))

    if message.topic == "Leistung":
        value1 = float(message.payload.decode())
    elif message.topic == "Dauer":                              #das klappt noch nicht!
        value2 = float(message.payload.decode())

    result = value1 * value2
    print("Result:", result)


#   Alternative für anderen Broker, wenn 'localhost' nicht zur Verfügung steht:
#   mqttBroker ="mqtt.eclipseprojects.io"
#   client.connect(mqttBroker)

client = mqtt.Client("Planungsalgorithmus")
client.connect("localhost", 1883)       #normalerweise hier ip-adresse vom mosquitto Broker

client.loop_start()

client.subscribe("Leistung")
client.subscribe("Dauer")
client.on_message = on_message

time.sleep(30)
client.loop_stop()



