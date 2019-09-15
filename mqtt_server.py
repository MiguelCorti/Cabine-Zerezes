import paho.mqtt.client as mqtt
import datetime
import time
from picamera import PiCamera
import subprocess
import os
from cropper import rectangle_crop, bottom_crop

print("Cabine ZRZS :: Server")

date = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

broker_url = "192.168.0.11"
broker_port = 1883

def on_connect(client, userdata, flags, rc):
   print("Connected With Result Code " (rc))

client = mqtt.Client()
client.connect(broker_url, broker_port)
time.sleep(.5)
client.on_connect = on_connect

client.subscribe("cabine", qos=1)

client.publish(topic="cabine", payload=date, qos=1, retain=False)
print("photo requested: " + date)


h = subprocess.Popen(["scp", "pi@192.168.0.11:/home/pi/image_1.jpg", "/home/pi/image_1.jpg"])
sts = os.waitpid(i.pid, 0)

i = subprocess.Popen(["scp", "pi@192.168.0.12:/home/pi/image_2.jpg", "/home/pi/image_2.jpg"])
sts = os.waitpid(i.pid, 0)

j = subprocess.Popen(["scp", "pi@192.168.0.13:/home/pi/image_3.jpg", "/home/pi/image_3.jpg"])
sts = os.waitpid(j.pid, 0)

k = subprocess.Popen(["scp", "pi@192.168.0.14:/home/pi/image_4.jpg", "/home/pi/image_4.jpg"])
sts = os.waitpid(k.pid, 0)

l = subprocess.Popen(["scp", "pi@192.168.0.15:/home/pi/image_5.jpg", "/home/pi/image_5.jpg"])
sts = os.waitpid(l.pid, 0)

rectangle_crop()

client.disconnect()

quit()
