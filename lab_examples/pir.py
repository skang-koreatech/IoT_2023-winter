import RPi.GPIO as gpio
import time

pir_pin = 21


# setup 함수를 이용하여 핀을 입력용으로 설정하기


try:
    while True:
        # input 함수를 이용하여 핀에서 값을 읽고 그것을 pir_in 변수에 할당    
        # pir_in = 
        
        # pir_in 값이 1이면 화면에 Detected 출력
        #if 조건문
            # 출력
            # 0.5초간 sleep

        # pir_in 값이 1이 아니면 화면에 Not detected 출력
        #else:
            # 출력
            # 0.5초간 sleep
            
except KeyboardInterrupt:
    gpio.cleanup()
