import subprocess
import os
import time

print("Cabine ZRZS :: Download Photos")

h = subprocess.Popen(["scp", "pi@192.168.0.11:/home/pi/image_1.jpg", "~/Desktop/image_1.jpg"], shell=False)
time.sleep(.2)
#subprocess.Popen(["raspberry"], shell=False)
sts = os.waitpid(h.pid, 0)

i = subprocess.Popen(["scp", "pi@192.168.0.11:/home/pi/image_2.jpg", "~/Desktop/image_2.jpg"], shell=False)
time.sleep(.2)
#subprocess.Popen(["raspberry"], shell=False)
sts = os.waitpid(i.pid, 0)

j = subprocess.Popen(["scp", "pi@192.168.0.11:/home/pi/image_3.jpg", "~/Desktop/image_3.jpg"], shell=False)
time.sleep(.2)
#subprocess.Popen(["raspberry"], shell=False)
sts = os.waitpid(j.pid, 0)

k = subprocess.Popen(["scp", "pi@192.168.0.11:/home/pi/image_4.jpg", "~/Desktop/image_4.jpg"], shell=False)
time.sleep(.2)
#subprocess.Popen(["raspberry"], shell=False)
sts = os.waitpid(k.pid, 0)

l = subprocess.Popen(["scp", "pi@192.168.0.11:/home/pi/image_5.jpg", "~/Desktop/image_5.jpg"], shell=False)
time.sleep(.2)
#subprocess.Popen(["raspberry"], shell=False)
sts = os.waitpid(l.pid, 0)

quit()
