import jsonify
import requests

from flask import Flask
from flask import render_template
app = Flask(__name__)

if __name__ == "__main__":
    app.run()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/raz")
def characters(): 
    response = requests.get("https://psychonauts-api.herokuapp.com/api/characters?name=raz")
    data = response.json() 
    name = data['name']
    img = data['img']
    powers = data['psiPowers']
    for x in powers: 
     psi = powers
    return render_template("characters.html", raz = name, pic = img, psi_powers = psi)
