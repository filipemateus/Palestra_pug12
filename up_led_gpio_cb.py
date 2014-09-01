import serial
from time import sleep
import os
ser = serial.Serial('/dev/ttyACM0', 9600)
#state = str(ser.read())


while True:
  if (str(ser.read()) == 1):
    os.system('echo "high" > /sys/class/gpio/gpio1_ph20')
    sleep(1)
 
