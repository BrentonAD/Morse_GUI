import RPi.GPIO as GPIO
import time

def blinkLed(pin, blinkDuration):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(blinkDuration)
    GPIO.output(pin, GPIO.LOW)

def morseBlink(morseCode, morseTiming, pin):
    for char in morseCode:
        if char == '.':
            # Blink Short (1 unit)
            blinkLed(pin, morseTiming)
            time.sleep(morseTiming)
        elif char == '-':
            # Blink Long (3 units)
            blinkLed(pin, 3*morseTiming)
            time.sleep(morseTiming)
        elif char == ' ':
            # Delay Short (3-1=2 units)
            time.sleep(2*morseTiming)
        elif char == '/':
            # Delay Long (7-1=6 units)
            time.sleep(6*morseTiming)