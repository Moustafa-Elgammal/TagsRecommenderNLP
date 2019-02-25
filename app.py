from flask import Flask
import pandas as pd
from flask import render_template
from flask import request
from typing import Optional, Dict, Any, Union
from flask import jsonify

from ContentBased import ContentBased
app = Flask(__name__)
cb = ContentBased()


@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/api/tags", method = ['post', 'get'])
def getTags():
    title = request.form.get("title")
    body = request.form.get("body")

    if title is None:
        title = request.args['title']

    if body  is None:
        body = request.args['body']

    if body is None & title is None:
        req = {"title": None, "body": None}
        res = {
        'tags':[],
        'req': req
        }

    return jsonify("sdfjk")

    tags = cb.getTags(title, body)

    res = {
    'tags': tags,
    'req': req
    }

    return jsonify(res)

if __name__ == "__main__":
    app.run()
