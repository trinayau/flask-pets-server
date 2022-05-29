from flask import Flask
from helper import pets
app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
  return """<h1>Adopt a Pet!</h1>
            <p>Browse through the links below to find your new furry friend:</p>
            <ul>
            <li><a href="/animals/dogs">Dogs</a></li>
            <li><a href="/animals/cats">Cats</a></li>
            <li><a href="/animals/rabbits">Rabbits</a></li>
            </ul>
            """

@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = f"""<h1>List of {pet_type}</h1>
              """
  html += '<ul>'
  #step 12 
  #step 16:
  # for each index and pet in pets dict of pets type, give a li linking to its individual page
  #enumerate() is needed to give each one an index and str() to turn it into a string type
  for index, pet in enumerate(pets[pet_type]):
    html += f"""<li><a href="/animals/{pet_type}/{str(index)}">{pet["name"]}</a></li>"""
  return html

#step 13
@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  #step 14
  #get specific pet from type and id in request parameters
  pet = pets[pet_type][pet_id]
  # step 15 - show pet name in html
  #step 17 - add img, p, ul, li
  html = f"""<h1>{pet["name"]}</h1>
              <img src="{pet["url"]}"></img>
              <p>{pet["description"]}</p>
              <ul>
              <li>Breed: {pet["breed"]}</li>
              <li>Age: {pet["age"]}</li>
              <ul>
              """
  return html

if __name__ == "__main__":
     app.debug = False
     port = int(os.environ.get('PORT', 33507))
     waitress.serve(app, port=port)
