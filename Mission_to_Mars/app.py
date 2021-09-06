from logging import debug
from flask import Flask, render_template, redirect
# Import mongoDB
from flask_pymongo import PyMongo
import scrape_mars
# os.add_dll_directory("PATH_TO_DLL")

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")
# mars_db = mongo.db.mars_db


@app.route("/")
def index():
  
    mars_info = mongo.db.collection.find_one()
    return render_template("index.html", data=mars_info)

@app.route("/update")
def update_data():
    mars_data = scrape_mars.update()
    mongo.db.collection.update({}, mars_data, upsert=True)
    return redirect("/")
  

if __name__=="__main__":
    app.run(debug=True)