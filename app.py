import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'testmenudb'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

@app.route('/')
# Get all recipes
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", 
    recipes=mongo.db.recipes.find())

# Generate HTML template
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
    users=mongo.db.users.find(),
    allergens=mongo.db.allergens.find(),
    cuisines=mongo.db.cuisine.find(),)
    
# Send the form
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes =  mongo.db.recipes
    form_dict = dict()
    form_dict["title"] =  request.form["title"]
    form_dict["cuisine"] =  request.form["cuisine"]
    mylist = request.form.to_dict('allergenlist')
    form_dict["allergenlist"] = mylist
    recipes.insert(form_dict)
    # form_dict["allergenlist"] =  request.form["allergenlist"]
    # print(form_dict)
    # multi_result = request.form["allergenlist"].to_dict(flat=False)
    # form_dict["allergenlist"] =  multi_result
    return redirect(url_for('get_recipes'))
    
    
if __name__ == '__main__':
    app.run(debug=True)