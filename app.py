from flask import Flask, json
import logging
from werkzeug.wrappers import response


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/status")
def get_status():
    response = app.response_class(
        response= json.dumps({'result': 'Ok - healthy'}),
        mimetype='application/json'
    )
    ## log line
    app.logger.info('Status request successfull')
    return response

@app.route("/metrics")
def get_metrics():
    metrics_response = {
        'UserCount': 140,
        'UserCountActive': 23
    }
    response = app.response_class(
        response= json.dumps(metrics_response),
        status=200,
        mimetype='application/json'
    )
    ## log line
    app.logger.info('Metrics request successfull')
    return response

if __name__ == "__main__":

    ## stream logs to app.log file
    logging.basicConfig(filename='app.log',level=logging.DEBUG)

    app.run(host='0.0.0.0')
