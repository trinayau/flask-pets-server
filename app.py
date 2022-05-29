from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from db import pets
from flask_cors import CORS
app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')
CORS(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/animals/<pet_type>')
def animals(pet_type):
  types = pets[pet_type]
  return render_template('pet_type.html', pets=types, pet_type=pet_type)

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]
  return render_template('pet.html', pet=pet)

if __name__ == "__main__":
     app.debug = False
     port = int(os.environ.get('PORT', 33507))
     waitress.serve(app, port=port)
