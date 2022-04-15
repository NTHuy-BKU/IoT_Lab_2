import json
import time
import serial.tools.list_ports
import paho.mqtt.client as mqttclient
import random
print("Xin chào ThingsBoard")

BROKER_ADDRESS = "mqttserver.tk"
PORT = 1883
USERNAME = "bkiot"
PASSWORD = "12345678"


temp = 25
humi = 60


def subscribed(client, userdata, mid, granted_qos):
    print("Subscribed...")

def publishData(client):
    temp = random.randint(0, 60)
    humi = random.randint(1, 99)
    ledStatus = 'on' if random.randint(0, 1) == 1 else 'off'
    pumpStatus = 'on' if random.randint(0, 1) == 1 else 'off'
    temp_data = {'temp': temp, 'humi': humi}
    try:
        client.publish('/bkiot/1812404/status', json.dumps(temp_data))
        print(temp_data)
        # client.publish('/bkiot/1812404/led',
        #                json.dumps({"device": "led", "status": ledStatus}))
        # print(ledStatus)
        # client.publish('/bkiot/1812404/pump',
        #                json.dumps({"device": "pump", "status": pumpStatus}))
        # print(pumpStatus)
    except:
        pass


def connected(client, usedata, flags, rc):
    if rc == 0:
        print("Thingsboard connected successfully!!")
        client.subscribe("/bkiot/1914738/status")
    else:
        print("Connection is failed")


client = mqttclient.Client("Gateway_Thingsboard")
client.username_pw_set(USERNAME, PASSWORD)

client.on_connect = connected
client.connect(BROKER_ADDRESS, 1883)
client.loop_start()

client.on_subscribe = subscribed
# client.on_message = recv_message


def processData(data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)


while True:
    publishData(client)
    time.sleep(2)
