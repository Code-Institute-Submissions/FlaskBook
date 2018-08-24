import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'testmenudb'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", 
    recipes=mongo.db.recipes.find())


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
    recipe_title = request.form["title"]
    recipe_method = request.form["method"]
    recipe_cuisine =  request.form["cuisine"]
    
    ingredient_1 = request.form["ingredient1"]
    ingredient_2 = request.form["ingredient2"]
    ingredient_3 = request.form["ingredient3"]
    ingredient_4 = request.form["ingredient4"]

    # allergen_1 = request.form["allergen1"]
    # allergen_2 = request.form["allergen2"]
    # allergen_3 = request.form["allergen3"]
    # allergen_4 = request.form["allergen4"]
    allergens = request.form.getlist("allergens")

    # recipe_author = request.form["author"]
    recipe_form = {
        "title": recipe_title,
        "method": recipe_method,
        "cuisine": recipe_cuisine,
        "ingredients": {
            "first": ingredient_1,
            "second": ingredient_2,
            "third": ingredient_3,
            "fourth": ingredient_4,
        },
        "allergens": allergens
    }
    recipes.insert_one(recipe_form)
    return redirect(url_for('get_recipes'))
    
    
if __name__ == '__main__':
    app.run(debug=True)