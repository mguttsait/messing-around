from flask import Flask, render_template, jsonify
from host import fetchHostDetails
from weather import getWeather

app = Flask(__name__)
HOSTNAME, IP = fetchHostDetails()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/health")
def health():
    return jsonify(
        status='UP',
        host = HOSTNAME,
        IP = IP
    )

@app.route("/weather")
def weather():
    return jsonify(getWeather('New York'))

@app.route("/details")
def hello():
    return render_template('index.html', HOSTNAME = HOSTNAME, IP = IP )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)