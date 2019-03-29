import paho.mqtt.client as mqtt
import pyaes
import hashlib
import time
import configparser
from time import sleep

# import psutil

config = configparser.RawConfigParser()
config.read('config/config-subscriber.txt')
username = config.get('credential', 'username')
password = config.get('credential', 'password')
topic = config.get('credential', 'topic')
server = config.get('host', 'server')
port = config.getint('host', 'port')
keepalive = config.getint('host', 'keep-alive')
secretkey = config.get('key', 'key')
clientid = config.get('credential', 'client')
#server = "192.168.1.158"


def on_connect(client, userdata, flags, rc):
    print("Connected with Code :" + str(rc))
    client.subscribe(topic)


key = secretkey
key = key.encode('utf-8')
counter = pyaes.Counter(initial_value=0)
aes = pyaes.AESModeOfOperationCTR(key, counter=counter)



def on_message(client, userdata, msg):
    client = mqtt.Client()

    #start process exec
    start = time.clock()

    msg = msg.payload

    #start decrypption time
    startDS = time.clock()

    decrypted = aes.decrypt(msg).decode('utf-8')

    n = 96
    parts = [decrypted[i:i + n] for i in range(0, len(decrypted), n)]
    hashValue = ''.join(parts[0])
    pesanAsli = ''.join(parts[1])
    print("")

    m = hashlib.sha384()
    m.update(pesanAsli.encode('utf-8'))
    digest = m.hexdigest()

    if hashValue == digest:
        mout.append(pesanAsli)

    sleep(0.1)

    #end decryption time
    endDS = time.clock()

    #end process exec
    end = time.clock()

    #variable temp
    btos = end-start
    btosdec = endDS-startDS

    #open file
    f = open('ptob.txt').readline()
    fd = open('ptob-ds.txt').readline()
    timeexec = btos+float(f)
    timedec = btosdec+float(fd)

    #write file
    f = open('delivery.txt', 'a')
    f.write(str(timeexec)+"\n")
    f = open('outds.txt', 'a')
    f.write(str(timedec)+"\n")


client = mqtt.Client(clientid)
client.username_pw_set(username, password)
client.connect(server, port, keepalive)

client.on_connect = on_connect

client.on_message = on_message
mout = []
client.loop_start()
while True:
    sleep(0.1)
    if len(mout) > 0:
        counter = pyaes.Counter(initial_value=0)
        aes = pyaes.AESModeOfOperationCTR(key, counter=counter)
        print(mout.pop())
client.loop_stop()