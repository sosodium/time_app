from flask import Flask
from datetime import datetime, timedelta, timezone
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def curr_time():
    tz_utc_est = timezone(timedelta(hours=-5))
    curr_time = datetime.now(tz_utc_est)
    curr_time = curr_time.strftime("%m/%d/%Y, %H:%M:%S")
    return curr_time

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
