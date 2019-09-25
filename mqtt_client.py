import paho.mqtt.client as mqtt
import subprocess
import datetime
import time
import os
from picamera import PiCamera

MY_NUMBER = 1

def connection_loop():
  while not client.connected_flag:
    print("Attempting MQTT connection...")
    # Attempt to connect
    try:
      client.connect(broker_url, broker_port)
      print("Connected to " + str(broker_url) + ":" + str(broker_port))
      # Once connected, subscribe
      client.subscribe("cabine", qos=1)
      client.connected_flag = True
    except Exception as e:
      print(e)
      print("Failed to connect, server is probably off the network.")
      print("Retrying in 2 seconds.")
      print("")
      # Wait 2 seconds before retrying
      time.sleep(2)

def on_connect(client, userdata, flags, rc):
  if rc == 0:
    client.connected_flag = True
    print("Connected with Result Code " (rc))
  else:
    print("Bad connection with Result Code " (rc))

def on_message(client, userdata, message):
  path = '/home/pi/image_' + str(MY_NUMBER) + '.jpg'
  camera = PiCamera()
  camera.resolution = (1920, 1400)
  camera.awb_mode = 'fluorescent'
  camera.capture(path)
  time.sleep(.5)
  camera.close()
  date = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
  print("Photo taken at " + date)

print("Cabine ZRZS :: Client")

broker_url = "192.168.0.3"
broker_port = 1883

mqtt.Client.connected_flag = False
client = mqtt.Client()

client.message_callback_add("cabine", on_connect)
client.message_callback_add("cabine", on_message)

client.on_connect = on_connect
client.on_message = on_message

connection_loop()

client.loop_forever()
