import paho.mqtt.client as mqtt
import random
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

mqttc = mqtt.Client()
mqttc.on_connect = on_connect

#mqttc.connect("test.mosquitto.org")
mqttc.connect("192.168.0.46")
mqttc.loop_start()

try:
    while True:
        d = random.randrange(20, 36)
        temp = str(d)                
        print("temp", temp)
        
        h = random.randrange(20, 71, 10)
        humid = str(h)
        print("humidity", humid)        
        
        infot = mqttc.publish("125/room/temp/ksw", temp)
        infot.wait_for_publish()
        infot = mqttc.publish("125/room/humid/ksw", humid)
        infot.wait_for_publish()
        
        time.sleep(2)
except KeyboardInterrupt:
    print("Finished!")
    mqttc.loop_stop()
    mqttc.disconnect()

