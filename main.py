from flask import Flask, jsonify

app = Flask(__name__)

# a simple page that says hello
@app.route('/hello')
def hello():
  return 'Hello, World!'

@app.route('/points', methods = ["GET"])
def getPoints():
  return jsonify([{'x': 0, 'y': 0}])

@app.route('/points', methods = ["POST"])
def addToPoints():
  return "Points added"

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8080, debug=True)