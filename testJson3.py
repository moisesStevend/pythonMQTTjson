#!/usr/bin/env python
import paho.mqtt.client as mqtt
import time
import serial
import json
import numpy as np
import cv2

def on_connect(client, userdata, flags, rc):
	print("Empezamos a conectarnos con calidad "+str(rc))
	
def publicar(topico,mensaje):
    client.publish(topico, mensaje)

def terminar():
    client.disconnect()
	
def loopForever():
	client.loop_forever()	
	 
client = mqtt.Client("STEVEND",transport='websockets')
client.connect("10.10.50.58",9001,60)
client.on_connect = on_connect

#client.loop()
#rc = 0
#while rc == 0:
#	rc = client.loop()
#	print rc
	
#print rc
                   
img=cv2.imread("img1.jpg",0)
#img=cv2.imread("yun_pinout.png",0)
mapeo=img.tolist()

data={
	"cabecera": json.dumps(mapeo)
}

while(1):
	client.loop()
	publicar('data_sin', json.dumps(data))
	time.sleep(0.1)
