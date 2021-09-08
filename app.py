from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<int:number>/')
def incrementer(number):
    return f"{number * number}"

@app.route('/<string:name>/')
def hello(name):
    return f"Hello {name}"
    
@app.route('/person/')
def hi():
    return jsonify({'name': 'Jimit', 'address':'India'})