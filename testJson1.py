import time
import json
import paho.mqtt.client as paho

a=[12,13,14,15]

data={
	"heights": json.dumps(a)
}

