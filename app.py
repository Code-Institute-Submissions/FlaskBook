# Import necessary modules
import datetime
import os
import time

from bson.objectid import ObjectId
from flask import Flask, redirect, render_template, request, url_for
from flask_pymongo import PyMongo
from werkzeug import secure_filename

# Uncomment on local deployment
# import env

app = Flask(__name__)
# Set app variables
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

mongo = PyMongo(app)


# Homepage route
@app.route('/')
def home_page():
    return render_template("home.html")


# Recipes **********************************************************************
# Get all recipes
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html",
                           recipes=mongo.db.recipes.find())


# Add recipe form
@app.route('/add_recipe')
def add_recipe():
    return render_template('addrecipe.html',
                           users=mongo.db.users.find(), cuisines=mongo.db.cuisine.find(), meals=mongo.db.meals.find())


# Submit add recipe form
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes

    recipe_title = request.form['title']
    recipe_description = request.form['description']
    recipe_method = request.form['method']
    recipe_ingredient = request.form.getlist('ingredient')
    recipe_meal = request.form.get('meal')
    recipe_serves = request.form['serves']
    recipe_cookingtime = request.form['cooking_time']
    recipe_preptime = request.form['prep_time']
    recipe_cuisine = request.form['cuisine']
    recipe_user = request.form['user']

    recipe_form = {
        "title": recipe_title,
        "description": recipe_description,
        "method": recipe_method,
        "ingredients": recipe_ingredient,
        "meal": recipe_meal,
        "serves":  recipe_serves,
        "cooking-time": recipe_cookingtime,
        "prep-time": recipe_preptime,
        "cuisine": recipe_cuisine,
        "user": recipe_user,
        "last_modified": time.asctime(time.localtime(time.time()))
    }

    recipes.insert_one(recipe_form)
    return redirect(url_for('get_recipes'))


# Edit recipe form
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    cuisines = mongo.db.cuisine.find()
    meals = mongo.db.recipes.find()
    ingredients = mongo.db.recipes.ingredients.find()
    users = mongo.db.users.find()
    return render_template('editrecipe.html',
                           recipe=recipe, cuisines=cuisines, users=users, ingredients=ingredients, meals=meals)


# Submit edit recipe form
@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes

    recipe_title = request.form['title']
    recipe_description = request.form['description']
    recipe_method = request.form['method']
    recipe_ingredient = request.form.getlist('ingredient')
    recipe_meal = request.form.get('meal')
    recipe_serves = request.form['serves']
    recipe_cookingtime = request.form['cooking_time']
    recipe_preptime = request.form['prep_time']
    recipe_cuisine = request.form['cuisine']
    recipe_user = request.form['user']

    recipes.update({'_id': ObjectId(recipe_id)},
                   {
        "title": recipe_title,
        "description": recipe_description,
        "method": recipe_method,
        "ingredients": recipe_ingredient,
        "meal": recipe_meal,
        "serves":  recipe_serves,
        "cooking-time": recipe_cookingtime,
        "prep-time": recipe_preptime,
        "cuisine": recipe_cuisine,
        "user": recipe_user,
        "last_modified": time.asctime(time.localtime(time.time()))
    })
    return redirect(url_for('get_recipes'))


# Delete/Mark done recipe
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_recipes'))


# Render the single recipe
@app.route('/recipe_single/<recipe_id>')
def recipe_single(recipe_id):
    return render_template("recipepage.html",
                           recipes=mongo.db.recipes.find({'_id': ObjectId(recipe_id)}))


# Construct shopping list for given recipe
@app.route('/shopping_list/<recipe_id>')
def shopping_list(recipe_id):
    return render_template("shoppinglist.html",
                           recipes=mongo.db.recipes.find({
                               '_id': ObjectId(recipe_id)}))


# Meal types *******************************************************************
# Sort recipes:
# by Cooking-time descending
@app.route('/recipes_time_desc')
def recipes_time_desc():
    col_sorted_desc = mongo.db.recipes.find(
        {"cooking-time": {"$gt": 0}}).sort([("cooking-time", -1)])
    return render_template("recipes.html", recipes=col_sorted_desc)


# by Cooking-time ascending
@app.route('/recipes_time_asc')
def recipes_time_asc():
    col_sorted_asc = mongo.db.recipes.find(
        {"cooking-time": {"$gt": 0}}).sort([("cooking-time", 1)])
    return render_template("recipes.html", recipes=col_sorted_asc)


# by Votes descending
@app.route('/votes_desc')
def votes_desc():
    col_sorted_votes_desc = mongo.db.recipes.find(
        {"votes": {"$gt": -1}}).sort([("votes", -1)])
    return render_template("recipes.html", recipes=col_sorted_votes_desc)


# by Votes ascending
@app.route('/votes_asc')
def votes_asc():
    col_sorted_votes_asc = mongo.db.recipes.find(
        {"votes": {"$gt": -1}}).sort([("votes", 1)])
    return render_template("recipes.html", recipes=col_sorted_votes_asc)


# by Date descending
@app.route('/date_desc')
def date_desc():
    col_sorted_date_desc = mongo.db.recipes.find().sort("last_modified", -1)
    # for item in col_sorted_date_desc:
    #     print("Item: ", item)
    return render_template("recipes.html", recipes=col_sorted_date_desc)


# by Date ascending
@app.route('/date_asc')
def date_asc():
    col_sorted_date_asc = mongo.db.recipes.find().sort("last_modified", 1)
    # for item in col_sorted_date_asc:
    #     print("Item: ", item)
    return render_template("recipes.html", recipes=col_sorted_date_asc)


# Meal types *******************************************************************
# Breakfast meals
@app.route('/breakfast_meals')
def breakfast_meals():
    return render_template("recipes.html",
                           recipes=mongo.db.recipes.find({"meal": "breakfast"}))


# Lunch meals
@app.route('/lunch_meals')
def lunch_meals():
    return render_template("recipes.html",
                           recipes=mongo.db.recipes.find({"meal": "lunch"}))


# Dinner meals
@app.route('/dinner_meals')
def dinner_meals():
    return render_template("recipes.html",
                           recipes=mongo.db.recipes.find({"meal": "dinner"}))


# Dessert meals
@app.route('/dessert_meals')
def dessert_meals():
    return render_template("recipes.html",
                           recipes=mongo.db.recipes.find({"meal": "dessert"}))


# Snack meals
@app.route('/snack_meals')
def snack_meals():
    return render_template("recipes.html",
                           recipes=mongo.db.recipes.find({"meal": "snack"}))


# Ligt-bites meals
@app.route('/lightbites_meals')
def lightbites_meals():
    return render_template("recipes.html",
                           recipes=mongo.db.recipes.find({"meal": "light-bites"}))


# Cuisines *********************************************************************
# Get cuisines route
@app.route('/get_cuisines')
def get_cuisines():
    get_cuisines = mongo.db.cuisine.find()

    # TESTING:
    for item in get_cuisines:
        print(item)

    return render_template('cuisines.html', cuisines=mongo.db.cuisine.find())


# Edit cuisine
@app.route('/edit_cuisine/<cuisine_id>')
def edit_cuisine(cuisine_id):
    the_cuisine = mongo.db.cuisine.find_one({"_id": ObjectId(cuisine_id)})
    return render_template('editcuisine.html', cuisine=the_cuisine)


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


# Submit add cuisine form
@app.route('/insert_cuisine', methods=["POST"])
def insert_cuisine():
    cuisines = mongo.db.cuisine
    cuisines.insert_one(request.form.to_dict())
    return redirect(url_for('get_cuisines'))


# Users ************************************************************************
# Voting:
# Upvote recipe
@app.route('/upvote_recipe/<recipe_id>', methods=["GET", "POST"])
def upvote_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)},
                   {
        '$inc': {'votes': 1}
    }
    )
    return redirect(url_for('get_recipes'))


# Downvote recipe
@app.route('/downvote_recipe/<recipe_id>', methods=["GET", "POST"])
def downvote_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipe_id)},
                   {
        '$inc': {'votes': -1}
    }
    )
    return redirect(url_for('get_recipes'))


# Search  **********************************************************************
# Search term from search box
@app.route('/search_box/', methods=["POST"])
def search_box():
    search_term = request.form['search_text']
    if (search_term != ''):
        return redirect(url_for('search_results', search_text=search_term))
    else:
        return render_template("recipes.html", recipes=mongo.db.recipes.find())


# Search results route
@app.route('/search_results/<search_text>')
def search_results(search_text):
    search_results = mongo.db.recipes.find(
        {'$text': {'$search': search_text}})
    # for item in search_results:
    #     print("Search results: ", item)
    return render_template("search-results.html", recipes=search_results)

# **********************************************************************
# For local deployment
# if __name__ == '__main__':
#     app.run(debug=True)

# For Heroku deployment
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
