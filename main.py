from datetime import datetime, date
import time
from flask import Flask, render_template


def feb():
    time_now = datetime.now()
    seco = time_now.second
    minu = time_now.minute
    jhbv = time_now.hour
    day = time_now.day
    mon = time_now.month
    yea = time_now.year
    t1 = datetime(year=yea+1, month=2, day=22, second=59, hour=23, minute=59)

    enbt = datetime(year=yea, month=mon, day=day, minute=minu, second=seco, hour=jhbv)

    times = t1 - enbt
    time_split = str(times).split()
    times_ = time_split[2].split(":")
    ads = str(times).replace("days", "дней")

def index():
    time_now = datetime.now()
    html = render_template('main.html', now_time=time_now)
    return html
app = Flask(__name__)
app.add_url_rule('/', 'index', index)
if __name__ == "__main__":
    app.run()