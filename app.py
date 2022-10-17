from flask import Flask
from controller import getClockAngle, getQueries

app = Flask(__name__)

@app.route('/')
def index():
	return "Use http://[domain]:8080/rest/clock/[hour]/[minute] \t angle"

@app.route('/rest/<string:petition>/<int:hour>/')
@app.route('/rest/<string:petition>/<int:hour>/<int:minute>')
def rest(petition,hour,minute=0):
	if petition == 'Relogio':
		return getClockAngle(hour,minute)

@app.route('/queries')
def queries():
	return getQueries()

if __name__=='__main__':
	app.run(host='0.0.0.0',debug=True)