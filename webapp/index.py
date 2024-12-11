from flask import Flask

#인스턴스(객체) 생성
app = Flask(__name__)

#URL "/"요청이 오면
@app.route('/')
def hello():
	return 'Hello Flask'

@app.route('/sub1')
def sub1():
	return 'Sub1 Page'

@app.route('/sub2')
def sub2():
	return 'Sub2 Page'

if __name__ == '__main__' :
	app.run(debug=True, port=80, host='0.0.0.0')

