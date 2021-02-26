import json
import random
import time
from datetime import datetime

from flask import Flask, Response, render_template, url_for

application = Flask(__name__)
random.seed()  # Initialize the random number generator


@application.route('/')
def index():
    return render_template('main.html')

@application.route('/temperature')
def temp():
    return render_template('temp.html')

@application.route('/voltage')
def voltage():
    return render_template('voltage.html')

@application.route('/soc')
def soc():
    return render_template('soc.html')

@application.route('/soh')
def soh():
    return render_template('soh.html')


@application.route('/chart-data')
def chart_data():
    def generate_random_data():
        while True:
            json_data = json.dumps(
                {'time': datetime.now().strftime('%M:%S'), 'temp': random.randint(25, 35), 'voltage': random.randint(25, 35)/10, 'soc': random.randint(90, 100), 'soh': random.randint(90, 100)})
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    return Response(generate_random_data(), mimetype='text/event-stream')


if __name__ == '__main__':
    application.run(debug=True, threaded=True)
