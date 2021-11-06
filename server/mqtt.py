import paho.mqtt.client as mqtt

def mqtt_subscriber():
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("test")

    def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("localhost", 1883, 60)

    client.loop_forever()

def mqtt_publisher(payload):
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))

    def on_message(client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("localhost", 1883, 60)

    client.publish("test", payload=payload , qos=0, retain=False)
