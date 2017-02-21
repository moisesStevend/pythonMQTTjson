#!/usr/bin/env python
import paho.mqtt.client as mqtt
import time
import serial
import json
import numpy as np
import cv2

class Envio_plot:
    def __init__(self,clientid=None):
        self.mi_array=0
        self.llego=False
        try:
            self.client = mqtt.Client(clientid,transport='websockets')
            self.client.connect("10.10.50.58",9001,60)
            self.client.on_connect = self.mqtt_on_connect
            self.client.on_message = self.mqtt_on_message
            self.client.loop_start()
        except:
            print "no se pudo conectar al broker"

    def publicar(self, topico,mensaje):
        self.client.publish(topico, mensaje)

    def terminar(self):
        self.client.disconnect()
    
    def mqtt_on_connect(self,client, userdata, flags, rc):
    	print("Empezamos a conectarnos con calidad "+str(rc))    
        self.client.subscribe("data_sin")
    
    def mqtt_on_message(self,client, userdata, msg):
        s=json.loads(msg.payload)
        ss=json.loads(s["cabecera"])
        s_array=np.asarray(ss)
        
        self.mi_array=s_array.astype(np.uint8)
        self.llego=True

        #cv2.imshow("messi",s_array)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        

mqttc=Envio_plot("MOISES")
img=cv2.imread("img1.jpg",0)
while 1:
    if mqttc.llego:
        print mqttc.mi_array, type(mqttc.mi_array)
        mqttc.llego=False
        break

print np.array_equal(mqttc.mi_array, img), mqttc.mi_array.dtype

cv2.imshow("messi",mqttc.mi_array)
cv2.waitKey(0)
cv2.destroyAllWindows()

mqttc.terminar()

