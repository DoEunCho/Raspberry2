from flask import Flask, render_template
import RPi.GPIO as GPIO

# Initialize Flask app
app = Flask(__name__)

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led_pin = 26  
GPIO.setup(led_pin, GPIO.OUT)

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led_on', methods=['POST'])
def led_on():
    GPIO.output(led_pin, GPIO.HIGH)
    return "LED ON"

@app.route('/led_off', methods=['POST'])
def led_off():
    GPIO.output(led_pin, GPIO.LOW)
    return "LED OFF"

if __name__ == '__main__':
    try:
        app.run(debug=False, host='0.0.0.0', port=5000)
    finally:
        GPIO.cleanup()
