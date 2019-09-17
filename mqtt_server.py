import paho.mqtt.client as mqtt
import datetime
import time
import subprocess
import os
import cropper

print("Cabine ZRZS :: Server")

date = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

broker_url = "192.168.0.3" #tem que mexer nisso aqui
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

image_path = get_current_path() + '/image_1.jpg'
h = subprocess.Popen(["scp", "pi@192.168.0.11:/home/pi/image_1.jpg", image_path])
sts = os.waitpid(h.pid, 0)

image_path = get_current_path() + '/image_2.jpg'
i = subprocess.Popen(["scp", "pi@192.168.0.12:/home/pi/image_2.jpg", image_path])
sts = os.waitpid(i.pid, 0)

image_path = get_current_path() + '/image_3.jpg'
j = subprocess.Popen(["scp", "pi@192.168.0.13:/home/pi/image_3.jpg", image_path])
sts = os.waitpid(j.pid, 0)

image_path = get_current_path() + '/image_4.jpg'
k = subprocess.Popen(["scp", "pi@192.168.0.14:/home/pi/image_4.jpg", image_path])
sts = os.waitpid(k.pid, 0)

image_path = get_current_path() + '/image_5.jpg'
l = subprocess.Popen(["scp", "pi@192.168.0.15:/home/pi/image_5.jpg", image_path])
sts = os.waitpid(l.pid, 0)

cropper.rectangle_crop()
cropper.create_gif(cropper.get_current_path())

client.disconnect()

quit()
