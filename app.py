import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'testmenudb'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

@app.route('/')
# Recipes *********************************************************************

# Get all recipes
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", 
        recipes=mongo.db.recipes.find())

# Add recipe form
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
    users=mongo.db.users.find(),
    allergens=mongo.db.allergens.find(),
    cuisines=mongo.db.cuisine.find())

# Submit add recipe form    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes =  mongo.db.recipes
    recipe_title = request.form["title"]
    recipe_method = request.form["method"]
    recipe_cuisine =  request.form["cuisine"]
    # recipe_user = request.form["user"]
    
    # ingredient_1 = request.form["ingredient1"]
    # ingredient_2 = request.form["ingredient2"]
    # ingredient_3 = request.form["ingredient3"]
    # ingredient_4 = request.form["ingredient4"]
    
    #  FIXME: allergen list not being passed 
    # allergen_1 = request.form["allergen1"]
    # allergen_2 = request.form["allergen2"]
    # allergen_3 = request.form["allergen3"]
    # allergen_4 = request.form["allergen4"]
    # allergens = request.form.getlist("allergens", None)
    # print("Allergens are: ", allergens)
    # recipe_author = request.form["author"]

    recipe_form = {
        "title": recipe_title,
        "method": recipe_method,
        "cuisine": recipe_cuisine,
        # "user": recipe_user
        # "ingredients": {
        #     "first": ingredient_1,
        #     "second": ingredient_2,
        #     "third": ingredient_3,
        #     "fourth": ingredient_4,
        # },
        # "allergens": allergens
    }
    print(recipe_form)
    recipes.insert_one(recipe_form)
    return redirect(url_for('get_recipes'))

# Edit recipe form
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe =  mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    cuisines =  mongo.db.cuisine.find()
    users = mongo.db.users.find()
    return render_template('editrecipe.html', recipe=the_recipe, cuisines=cuisines, users=users)


# Submit edit recipe form
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    # FIXME: cuisine and author is causing bug to not send form
    # print({'_id': ObjectId(recipe_id)},
    # {
    #     'title':request.form['recipe_title'],
    #     'method':request.form['recipe_method'],
    #     # 'cuisine': request.form['cuisine_name']
    # })
    recipes.update( {'_id': ObjectId(recipe_id)},
    {
        'title':request.form['recipe_title'],
        'method':request.form['recipe_method'],
        'author': request.form['user_name']
        # 'cuisine': request.form['cuisine_name']
    })
    return redirect(url_for('get_recipes'))


# Delete/Mark done recipe
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))

# Cuisines *********************************************************************

# Get cuisines route
@app.route('/get_cuisines')
def get_cuisines():
    return render_template('cuisines.html', 
        cuisines=mongo.db.cuisine.find())

# Edit cuisine
@app.route('/edit_cuisine/<cuisine_id>')
def edit_cuisine(cuisine_id):
    the_cuisine = mongo.db.cuisine.find_one({"_id": ObjectId(cuisine_id)})    
    return render_template('editcuisine.html', cuisine=the_cuisine )


# Submit Edit cuisine form
@app.route('/update_cuisine/<cuisine_id>', methods=["POST"])
def update_cuisine(cuisine_id):
    cuisines = mongo.db.cuisine
    cuisines.update({'_id': ObjectId(cuisine_id)},
    {
        'cuisine_name': request.form['cuisine_name']
    })
    return redirect(url_for('get_cuisines'))


# Delete new cuisine
@app.route('/delete_cuisine/<cuisine_id>')
def delete_cuisine(cuisine_id):
    mongo.db.cuisine.remove({'_id': ObjectId(cuisine_id)})
    return redirect(url_for('get_cuisines'))

# Add new cuisine form
@app.route('/add_cuisine')
def add_cuisine():
    return render_template('addcuisine.html',
        cuisines=mongo.db.cuisine.find())


    cuisines = mongo.db.cuisine
    cuisine_name = request.form['cuisine_name']
    cuisines.insert_one(cuisine_name)

    return redirect(url_for('get_cuisines'))

# Submit add cuisine form
@app.route('/insert_cuisine', methods=["POST"])
def insert_cuisine():
    cuisines = mongo.db.cuisine
    cuisine_name = request.form['cuisine_name']
    
    cuisine_form = {
        'cuisine_name': cuisine_name
    }

    cuisines.insert_one(cuisine_form)
    return redirect(url_for('get_cuisines'))

# Users *********************************************************************

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)