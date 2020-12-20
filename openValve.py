import RPi.GPIO as GPIO
import time
import sys
import datetime
import os
import config

GPIO.setmode(GPIO.BCM)
GPIO.setup(15,GPIO.OUT)
                    
if len(sys.argv) > 1:
   wateringTime = float(sys.argv[1]) * 60.0
else:
    wateringTime = 60
    
print("Watering Starts ", datetime.datetime.now())
for email in config.notificationList:
  stream = os.popen("echo 'I have started watering your garden' | msmtp " + email)
  print("email message :" + stream.read())

GPIO.output(15,GPIO.HIGH)

time.sleep(wateringTime)

GPIO.output(15,GPIO.LOW)
GPIO.cleanup()
                    
print("Watering Ends ", datetime.datetime.now())
for email in config.notificationList:
  stream = os.popen("echo 'I have finished watering your garden' | msmtp " + email)
  print("email message :" + stream.read())
