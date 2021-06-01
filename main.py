from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config.from_object("config.Config")
db = SQLAlchemy(app)

class Points(db.Model):
  __tablename__ = "points"
  id = db.Column(db.Integer, primary_key=True)
  x = db.Column(db.Float, nullable=False)
  y = db.Column(db.Float, nullable=False)
  def __init__(self, x, y):
    self.x = x
    self.y = y

# a simple page that says hello
@app.route('/hello')
def hello():
  return 'Hello, World!'

@app.route('/points', methods = ["GET"])
def getPoints():
  points = Points.query.all()

  outPoints = [{'x': pnt.x, 'y':pnt.y} for pnt in points]

  return jsonify(outPoints)

@app.route('/points', methods = ["POST"])
def addToPoints():
  point = Points(random.random(), random.random())
  db.session.add(point)
  db.session.commit()
  return "Points added"

@app.route('/addTenPoints', methods = ["POST"])
def addTenPoints():
  for _ in range(10):
    point = Points(random.random(), random.random())
    db.session.add(point)
  db.session.commit()
  return "Points added"


@app.route('/pi', methods=["GET"])
def getPi():
  points = Points.query.all()
  total = 0
  insideCircle = 0
  for pnt in points:
    if pnt.x <= pnt.y:
      insideCircle += 1
    total += 1
  ratio = insideCircle / total
  return jsonify({"pi": str(4 * ratio)})

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8080, debug=True)