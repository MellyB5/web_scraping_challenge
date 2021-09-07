from logging import debug
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")


@app.route("/")
def index():
  
    mars_info = mongo.db.collection.find_one()
    print(mars_info)
    return render_template("index.html", data=mars_info)

@app.route("/update")
def update():
    mars_data = scrape_mars.update()
    mongo.db.collection.replace_one({}, mars_data, upsert=True)
    return redirect("/")
  

if __name__=="__main__":
    app.run(debug=True)