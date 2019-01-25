from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello, World!'

@app.route('/health')
def health():
    return 'health ok!'

app.run(port=8887)