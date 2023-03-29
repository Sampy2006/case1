from flask import Flask, render_template
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
def main_window():
    return render_template('index.html')


@app.route('/pedagog1')
def pedagog1():
    return render_template('pedagog1.html')


@app.route('/pedagog2')
def pedagog2():
    return render_template('pedagog2.html')


@app.route('/pedagog3')
def pedagog3():
    return render_template('pedagog3.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
