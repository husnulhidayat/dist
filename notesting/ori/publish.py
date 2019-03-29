import sys
import paho.mqtt.client as mqtt
import pyaes
import configparser
import hashlib
import time
import argparse

config = configparser.RawConfigParser()
config.read('config/config-publisher.txt')
username = config.get('credential','username')
password = config.get('credential','password')
topic = config.get('credential','topic')
server = config.get('host','server')
port = config.getint('host','port')
keepalive = config.getint('host','keep-alive')
qosval = config.getint('credential','qos')
clientid = config.get('credential','client')


parser = argparse.ArgumentParser()
parser.add_argument("-m",help="message")
args = parser.parse_args()

def on_connect( client, userdata, flags, rc):
    print ("Connected with Code : " +str(rc))
    #client.subscribe(topic)

def on_message( client, userdata, msg):
    print(str(msg.payload))

def on_log(client, userdata, level, buf):
    print("log: ",buf)


client = mqtt.Client(clientid)
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(username, password)
client.connect(server, port, keepalive)

client.loop_start()
time.sleep(1)


def main():
    client.loop_start()
    try:
        #startprocessexec
        start = time.clock()

        #get message from arge
        message = args.m

        #publishing cipher to broker
        client.publish(topic,message,qos=qosval)

        end = time.clock()

        ptob = end-start
        f = open('ptob.txt','w')
        f.write(str(ptob))
        f.close()



    except KeyboardInterrupt:
        sys.exit(0)

    client.loop_stop()
    client.disconnect()

if __name__ == '__main__':
    main()
