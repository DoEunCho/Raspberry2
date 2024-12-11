from flask import Flask, render_template
import RPi.GPIO as GPIO
import threading
import time

# Initialize Flask app
app = Flask(__name__)

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pin = 26
pir_pin = 4

GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(pir_pin, GPIO.IN)

# Shared variable for motion status
motion_status = "No Motion"


# Function to monitor PIR sensor
def monitor_pir():
    global motion_status
    while True:
        if GPIO.input(pir_pin):  # Motion detected
            GPIO.output(led_pin, GPIO.HIGH)  # Turn on LED
            motion_status = "Motion Detected!"
        else:  # No motion
            GPIO.output(led_pin, GPIO.LOW)  # Turn off LED
            motion_status = "No Motion"
        time.sleep(0.1) 


# Define routes
@app.route("/")
def index():
    return render_template("led_pir_check.html", motion_status=motion_status)


@app.route("/motion_status")
def motion_status_route():
    return motion_status


if __name__ == "__main__":
    try:
        # Start PIR monitoring
        pir_thread = threading.Thread(target=monitor_pir, daemon=True)
        pir_thread.start()

        # Run Flask server
        app.run(debug=False, host="0.0.0.0", port=5000)
    finally:
        GPIO.cleanup()
