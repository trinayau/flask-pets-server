from flask import Flask, render_template, request, redirect, url_for
from db import pets, add_pet
from flask_cors import CORS
from werkzeug import exceptions

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        name = request.form.get('name')
        age = request.form.get('age')
        breed = request.form.get('breed')
        species = request.form.get('species')
        description = request.form.get('description')
        new_id = len(pets[species])+1
        new_pet = {"name": name, "age": age, "breed": breed, "description": description}
        print(new_pet, 'new pet')
        add_pet(species, new_pet)
        return redirect(url_for('animals', pet_type=species))
    return render_template('index.html')

@app.route('/animals/<pet_type>')
def animals(pet_type):
  types = pets[pet_type]
  print(pet_type)
  return render_template('pet_type.html', pets=types, pet_type=pet_type)

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  pet = pets[pet_type][pet_id]
  return render_template('pet.html', pet=pet)

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return render_template('404.html'), 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return render_template('400.html'), 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return render_template('500.html'), 500

if __name__ == "__main__":
     app.debug = False
     port = int(os.environ.get('PORT', 33507))
     waitress.serve(app, port=port)
