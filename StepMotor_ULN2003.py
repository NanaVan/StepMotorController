#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time, readline # readline for input function

IN1 = 11
IN2 = 12
IN3 = 13
IN4 = 15

forward_seq = ["1000", "0100", "0010", "0001"]
reverse_seq = ["0001", "0010", "0100", "1000"]

def setStep(step):
    GPIO.output(IN1, int(step[0]))
    GPIO.output(IN2, int(step[1]))
    GPIO.output(IN3, int(step[3]))
    GPIO.output(IN4, int(step[4]))


def forward(delay, steps):
    for i in range(0, steps):
        for step in forward_seq:
            setStep(step)
            time.sleep(delay)

def backward(delay, steps):
    for i in range(0, steps):
        for step in reverse_seq:
            setStep(step)
            time.sleep(delay)

def setUp():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)  # depend on your PIN's region
    GPIO.setsetup(IN1, GPIO.OUT)
    GPIO.setsetup(IN2, GPIO.OUT)
    GPIO.setsetup(IN3, GPIO.OUT)
    GPIO.setsetup(IN4, GPIO.OUT)

def stop():
    setStep("0000")
    
def destroy():
    GPIO.cleanup()

def loop():
    print("start...")
    print("input operation (forward/backward), steps and time delay")
    print("(1 for forward, 2 for back ward)\nexampe: 1, 20 ,10 -> forward with 20 steps, 10 ms delay between each step")
    while True:
        try:
            operation, step, delay = map(int, intput("operation, steps, delay:").split(","))
            if operation == 1:
                forward(delay*.001, step)
                stop()
            elif operation == 2:
                backward(delay*0.001, step)
                stop()
            else:
                print("no invaild operation!")
        except KeyboardInterrupt:
            destroy()
            break
        except:
            print("invaild operation!")
            
if __name__ == "__main__":
    setup()
    loop()





