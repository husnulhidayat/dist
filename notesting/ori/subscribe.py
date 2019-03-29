import paho.mqtt.client as mqtt
import pyaes
import hashlib
import configparser
import time
import psutil

config = configparser.RawConfigParser()
config.read('config/config-subscriber.txt')
username = config.get('credential','username')
password = config.get('credential','password')
topic = config.get('credential','topic')
server = config.get('host','server')
port = config.getint('host','port')
keepalive = config.getint('host','keep-alive')



def on_connect( client, userdata, flags, rc):
    print ("Connected with Code :" +str(rc))
    client.subscribe(topic)

def on_message( client, userdata, msg):

    start = time.clock()
    msg = msg.payload

    print(msg.decode('utf-8'))

    end = time.clock()
    btos = end-start

    f = open('ptob.txt').readline()
    timeexec = btos+float(f)
    f = open('delivery.txt', 'a')
    f.write(str(timeexec)+"\n")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(username, password)
client.connect(server, port, keepalive)

client.loop_forever()
