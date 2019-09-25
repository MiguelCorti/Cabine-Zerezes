import paho.mqtt.client as mqtt
import datetime
import time
import subprocess
import os
import sys
import cropper

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

print("Cabine ZRZS :: Server")


broker_url = "192.168.0.3" #tem que mexer nisso aqui
broker_port = 1883

mqtt.Client.connected_flag = False

client = mqtt.Client()
client.on_connect = on_connect

connection_loop()
time.sleep(.5)

date = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
client.publish(topic="cabine", payload=date, qos=1, retain=False)
print("Photos requested at " + date + "\n")

current_path = cropper.get_current_path(sys.argv[0], __file__)
img_dir = current_path + "/images"
if not os.path.exists(img_dir):
    os.mkdir(img_dir)

all_paths = []

for i in range(1,6):
    dest_image_path = img_dir + '/image_' + str(i) + '.jpg'
    org_image_path = "pi@192.168.0.1"+str(i)+":/home/pi/image_"+str(i)+".jpg"
    h = subprocess.Popen(["scp", org_image_path, dest_image_path])
    pid, sts = os.waitpid(h.pid, 0)
    print("PID Status: " + str(sts))
    if sts == 0:
      update_time = os.path.getmtime(dest_image_path)
      print("Photo taken at " + str(update_time))
      all_paths += [dest_image_path]
    print("")

client.disconnect()

margins = {
    "top": 200,
    "bottom": 25,
    "right": 100,
    "left": 100,
}
cropped_paths = cropper.rectangle_crop(all_paths, margins)
dest_path = current_path
cropper.create_gif(cropped_paths, dest_path)

quit()
