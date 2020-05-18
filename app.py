import os

from flask import Flask, Response

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/file')
def get_file():
    content = open('static/state-income.csv').read()
    return Response(content, mimetype='text/csv')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
