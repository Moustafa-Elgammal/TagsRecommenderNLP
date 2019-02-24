from flask import Flask
from flask import render_template
from flask import request
from typing import Optional, Dict, Any, Union


import pandas as pd

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html', classifiers=classifiers)


if __name__ == "__main__":
    app.run()
