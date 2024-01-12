import RPi.GPIO as gpio
import time

red_pin = 5
blue_pin = 25

gpio.setmode(gpio.BCM)
gpio.setup(red_pin, gpio.OUT)
gpio.setup(blue_pin, gpio.OUT)


num = int(input("숫자 입력: "))

if num == 1:
    gpio.output(red_pin, True)
    time.sleep(1.0)
    gpio.output(red_pin, False)
    time.sleep(1.0)
    gpio.output(red_pin, True)
    time.sleep(1.0)
    gpio.output(red_pin, False)
    
elif num == 2:
    gpio.output(blue_pin, True)
    time.sleep(3.0)
    gpio.output(blue_pin, False)
    
else:
    print("빨간색 LED는 1, 파란색 LED는 2를 입력하세요.")


print("Blink Finished")
gpio.cleanup()

