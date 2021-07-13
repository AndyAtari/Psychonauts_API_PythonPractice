import requests
import jsonify
from flask import Flask
app = Flask(__name__)

if __name__ == "__main__":
    app.run()

@app.route("/")
def home():
    response = requests.get("https://psychonauts-api.herokuapp.com/api/characters?name=raz")
    print(type(response))
    return response.json()

   
