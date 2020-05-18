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
    app.run()
