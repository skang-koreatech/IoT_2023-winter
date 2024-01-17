import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("connected with result code " + str(rc))
    client.subscribe("125/room/temp/ksw")
        
def on_message(client, userdata, msg):
    print("Topic: " + msg.topic + " Message: " + msg.payload.decode("utf-8"))
    
    temp = int(msg.payload.decode("utf-8"))
    
    if temp >= 22 and temp < 27:
        print("기온 보통")
    elif temp >= 27:
        print("기온 높음")
        
        infot = pubClient.publish("125/room/aircon/ksw", "on")
        infot.wait_for_publish()
    else:
        print("기온 낮음")
        
        infot = pubClient.publish("125/room/aircon/ksw", "off")
        infot.wait_for_publish()   

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
#client.connect("test.mosquitto.org")
client.connect("192.168.0.46")

pubClient = mqtt.Client()
pubClient.connect("192.168.0.46")
pubClient.loop_start()

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Finished!")
    client.unsubscribe("125/room/temp/ksw") 
    client.disconnect()
    pubClient.loop_stop()
    pubClient.disconnect()

