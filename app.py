from flask import Flask
from flask import json
from flask.wrappers import Response
import logging

app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info('Main request successful')

    return "Hello World!"

@app.route("/status")
def status():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype= "application/json"
    )
    app.logger.info("Status request successful")

    return response

@app.route("/metrics")
def metrics():
    response = app.response_class(
        response=json.dumps({'data': {'User Count': 140, 'UserCountActive': 23}}),
        status=200,
        mimetype="application/json"
    )
    app.logger.info('Metrics request successful')
    
    return response

if __name__ == "__main__":

    # stream logs to app.log file
    #logging.basicConfig(filename='app.log',level=logging.DEBUG, format='%(asctime)s %(module)s %(funcName)s endpoint was reached %(levelname)s %(message)s')
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(debug=True)
    app.run(host='0.0.0.0')

