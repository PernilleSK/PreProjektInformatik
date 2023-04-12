from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/p')
def wuu_huuu():
    return 'wuhuu!'

if __name__ == '__main__':
    app.run()
