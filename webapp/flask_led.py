from flask import Flask
import RPi.GPIO as GPIO

GPIO.cleanup()
GPIO.setwarnings(False)

#라즈베리파이 설정
GPIO.setmode(GPIO.BCM)

led_pin = 26
GPIO.setup(led_pin, GPIO.OUT)

#인스턴스(객체) 생성
app = Flask(__name__)

#URL "/"요청이 오면
@app.route('/')
def hello():
	return 'Hello Flask'

@app.route('/led_on')
def led_on():
	GPIO.output(led_pin, GPIO.HIGH)
	return 'LED On'

@app.route('/led_off')
def led_off():
	GPIO.output(led_pin, GPIO.LOW)
	return 'LED Off'

@app.route('/clean_up')
def clean_up():
	GPIO.cleanup()
	return 'GPIO cleanup'

if __name__ == '__main__' :
	app.run(debug=False, port=80, host='0.0.0.0')

