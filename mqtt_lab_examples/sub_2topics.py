import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("connected with result code " + str(rc))
    client.subscribe("125/room/temp/ksw") 
    client.subscribe("125/room/humid/ksw")
        
def on_message(client, userdata, msg):
    print("Topic: " + msg.topic + " Message: " + msg.payload.decode("utf-8"))
    
    if msg.topic == "125/room/temp/ksw":    
        temp = int(msg.payload.decode("utf-8"))
        
        if temp >= 20 and temp < 25:
            print("Moderate temperature")
        elif temp >= 25 and temp <30:
            print("High temperature")
        else:
            print("Very high temperature")
      
    elif msg.topic == "125/room/humid/ksw":
        humid = int(msg.payload.decode("utf-8"))
        
        if humid >=20 and humid < 30:
            print("Low humidity")
        elif humid >= 30 and humid < 50:
            print("Mid humidity")
        else:
            print("High humidity")
    #else:
    #    print("Error")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
#client.connect("test.mosquitto.org")
client.connect("192.168.0.46")

try:
    client.loop_forever()
except KeyboardInterrupt:
    print("Finished!")
    client.unsubscribe("125/room/temp/ksw") 
    client.unsubscribe("125/room/humid/ksw") 
    client.disconnect()

