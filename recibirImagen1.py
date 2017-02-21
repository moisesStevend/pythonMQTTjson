#!/usr/bin/env python
import json
import paho.mqtt.client as mqtt
import numpy as np
import cv2
# This is the Subscriber

global llego
s_array=0
img=cv2.imread("img1.jpg",0)

def plotear():
    cv2.imshow("messi",mi_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    i=False

def on_connect(client, userdata, flags, rc):
    print("Empezamos a conectarnos con calidad "+str(rc))
    client.subscribe("data_sin")

def on_message(client, userdata, msg):
    #print msg.payload,type(msg.payload)
    s=json.loads(msg.payload)
    ss=json.loads(s["cabecera"])
    s_array=np.asarray(ss)
    
    llego=True
    #print np.array_equal(s_array, img)
    #print ss, type(ss), len(ss)#type(s), len(s["cabecera"])
    print "s_array:",s_array#, s_array.shape
    
    #np.savetxt("testR.out",s_array)
    #mi_array=s_array
    #i=True
    #cv2.imshow("messi",s_array)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    
client = mqtt.Client()
client.connect("10.10.50.58",1883,60)
client.loop_start()

client.on_connect = on_connect
client.on_message = on_message

llego=False

while True:
    if llego:
        print s_array
        llego=False



