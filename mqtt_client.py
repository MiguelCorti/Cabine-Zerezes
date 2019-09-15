import paho.mqtt.client as mqtt
import subprocess
import datetime
import time
from picamera import PiCamera

print("Cabine ZRZS :: Client")

broker_url = "192.168.0.11"
broker_port = 1883

def on_connect(client, userdata, flags, rc):
   print("Connected With Result Code " (rc))

def on_message(client, userdata, message):
   camera = PiCamera()
   #camera.rotation = 270
   camera.resolution = (3280, 2464)
   camera.awb_mode = 'fluorescent'
   camera.capture('/home/pi/image_5.jpg')
   time.sleep(.5)
   camera.close()
   date = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
   print("photo taken: " +date)


client = mqtt.Client()

client.message_callback_add("cabine", on_connect)
client.message_callback_add("cabine", on_message)

client.on_connect = on_connect
client.on_message = on_message


client.connect(broker_url, broker_port)


client.subscribe("cabine", qos=1)

client.loop_forever()

#client.publish(topic="cabine", payload="MENSAGEM", qos=1, retain=False)
