from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    print("starting python flask server ")
    app.run()