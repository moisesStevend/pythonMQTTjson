#!/usr/bin/env python
import paho.mqtt.client as mqtt
import time
import serial
import json
import numpy as np
import cv2

class Envio_plot(object):
    def __init__(self,clientid=None):
        try:
            self.client = mqtt.Client(clientid,transport='websockets')
            self.client.connect("10.10.50.58",9001,60)
            self.client.on_connect = self.on_connect
            self.client.loop_start()
            
        except:
            print "no se pudo conectar al broker"

    def on_connect(self,client, userdata, flags, rc):
		print("Empezamos a conectarnos con calidad "+str(rc))
	
    def publicar(self, topico,mensaje):
        self.client.publish(topico, mensaje)

    def terminar(self):
        self.client.disconnect()
	
	def loopForever(self):
		self.client.loop_forever()	
        
try:
	img=cv2.imread("img1.jpg",0)
	#print img,type(img), img.dtype
	mi_envio=Envio_plot("STEVEND")
	#mapeo=[45,67,78.90,45,67.89]
	mapeo=img.tolist()
	"""
	img=np.loadtxt("./testS.out")
	cv2.imshow("messi",img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()	
	"""
	
	data={
		"cabecera": json.dumps(mapeo)
		#"cabecera": json.dumps([[1,2,3],[4,5,6]])
	}
	#while(1):
	mi_envio.publicar('data_sin', json.dumps(data))
	
	#mi_envio.terminar()
	#mi_envio.publicar('data_sin', json.dumps(data))
	#mi_envio.publicar('data_sin', json.dumps(data))
	#np.savetxt("testS.out",img)
	#mi_envio.loopForever()

except:
	print "No se conecto"
