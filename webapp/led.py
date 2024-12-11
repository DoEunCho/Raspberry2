import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

test_pin = 19  # Replace with your GPIO pin number
GPIO.setup(test_pin, GPIO.OUT)

print("Turning LED on and off...")
for _ in range(5):
    GPIO.output(test_pin, GPIO.HIGH)  # Turn LED on
    time.sleep(1)  # Wait for 1 second
    GPIO.output(test_pin, GPIO.LOW)   # Turn LED off
    time.sleep(1)

GPIO.cleanup()
