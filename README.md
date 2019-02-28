# Flaskbook
This repository contains the code for an online Cookbook/Recipe application. It is primarily built using Python and the Flask framework

## UX
This application is built with a mobile first, responsive design in mind.

### User stories

- As a new user, I should:
    - see a homepage with a cover image with a tag line.
    - see a main navigation with links to main recipe categories.
    - see a search bar for finding recipes.
    - see a floating button to allow users to create a new recipe.

- As a user who wishes to create a recipe, I should:
    - see a form allowing me to add the following fields:
        - title, description, method.
        - main ingredient, with the option to add/remove more ingredients as necessary.
        - choose a meal time i.e. breakfast/lunch/dinner etc.
        - servings per recipe.
        - cooking and preparation time.
        - cuisine i.e. Irish, Italian etc.
        - assign a user name from dropdown (authentication is not required for this project).
    - see a submit to send the form
    - see a cancel button to return to all recipes.

- As a user who wants to view all recipes, I should see a link to "all recipes" where I can see preview cards of each of the stored recipes, each displaying the following:
    - thumbnail image.
    - like count.
    - preview icon, to view basic recipe details i.e. prep time, cook time, description etc.
    - link to the full recipe listing.

- As a user who wants to view sort all recipes, I should:
    - on the al recipes page, see a dropdown listing various sorting methods:
        - newest/oldest.
        - cooking time descending/ascending
        - votes descending/ascending.

- As a user who wants to view a certain category of recipes, I should:
    - click on the category name from a link and be taken to a page only returning recipes contained within those recipes

- A a user who wants to view the full recipe listing, I should:
    - click on a recipe card from the all recipes page and be taken to a page where I should:
        - see a page detailing all recipe fields:
            - title, description, method.
            - ingredients.
            - meal time.
            - servings per recipe.
            - cooking and preparation time.
            - cuisine.
            - user name.
            - date/time entered or updated.
            - votes.
            - edit/delete controls.

- As a user who wishes to see a shopping list - a helpful list which they can tick off as they collect items in a store - I should click on a shopping basket icon on the full recipe page.

- As a user who wants to delete a recipe, I should click an appropriate icon on the recipe's page which will remove the recipe form the database.

- As a user who wants to edit a recipe, I should click an appropriate icon on the recipe's page which will direct me to a form where I can edit all of the form fields and either submit the changes or cancel, returning to all recipes.

- As user who wants to edit recipe, I should click on a particular recipe , w


Create a web application that allows users to store and easily access cooking recipes
Put some effort into designing a database schema based on recipes, and any other related properties and entities (e.g. views, upvotes, ingredients, recipe authors, allergens, author’s country of origin, cuisine etc…). 
Make sure to put some thought into the relationships between them, and use either foreign keys (in the case of a relational database) or nesting (in the case of a document store) to connect these pieces of data.

Create the backend code and frontend form to allow users to add new recipes to the site (at least a basic one, if you haven’t taken the frontend course). Create the backend code to group and summarise the recipes on the site, based on their attributes such as cuisine, country of origin, allergens, ingredients, etc. and a frontend page to show this summary, and make the categories clickable to drill down into a filtered view based on that category. This frontend page can be as simple or as complex as you’d like; you can use a Python library such as matplotlib, or a JS library such as d3/dc (that you learned about if you took the frontend modules) for visualisation.

Create the backend code to retrieve a list of recipes, filtered based on various criteria (e.g. allergens, cuisine, etc…) and order them based on some reasonable aspect (e.g. number of views or upvotes). Create a frontend page to display these, and to show some summary statistics around the list (e.g. number of matching recipes, number of new recipes. Optionally, add support for pagination, when the number of results is large.

Create a detailed view for each recipes, that would just show all attributes for that recipe, and the full preparation instructions.
Allow for editing and deleting of the recipe records, either on separate pages, or built into the list/detail pages.
Optionally, you may choose to add basic user registration and authentication to the site. This can as simple as adding a username field to the recipe creation form, without a password (for this project only, this is not expected to be secure)

# Demo:
A development(subject to current dev changes) demo of this app can be viewed [here](https://glacial-brook-98593.herokuapp.com/). It is hosted on the Heroku platform on server that may take a few seconds to spin up when you first visit.

# Technology stack:
- Python
- [Flask framework](http://flask.pocoo.org/)
- HTML
- CSS
- Javascript
- jQuery
- [Materialize CSS](https://materializecss.com/) - CSS framwork implementing Material design guidelines
- [MongoDB](https://www.mongodb.com/) - NoSQL/Document structure database
- [mLab](https://mlab.com/) for MongoDB hosting
- [Heroku](https://heroku.com) - for Python app deployment


# UX:
TODO:

# Testing:
Testing for this project was implemented manually. The majority of testing covered the various Flask routes. Some examples of issues/tests on routes:
- When on the homepage, when clicking on a recipe category and no recipes for such a category exist then the user will be directed to the all recipes route.
- When using the search bar, if nothing is input into the search field then the user will shown al recipes.
- When sorting recipes by parameters i.e. newest/oldest, votes desc/asc etc. - if such a parameter is not recored in any given document, it is omitted from the sorted list which is returned.
- On the add recipe form all neccessary fields i.e. title, cuisine etc. - were given the `required` tag to ensure the user did not submit empty/partially filled recipes.
- For textareas and inputs, a `max-length` was added to restrict input length.

# Databse schema:
- The main MongoDB collection `recipes` takes he following schema.

```json

{
    "_id" : ObjectId("5b9271df57eed8a9d19e1cf6"),
    "title" : "Albondigas",
    "description" : "This is a short description of the recipe.",
    "methods" : "Include all method steps for the recipe",
    "ingredients" : [ 
        {
            "name" : "1",
            "qty" : 125.0,
            "unit" : "grams"
        }, 
        {
            "name" : "2",
            "qty" : 45.0,
            "unit" : "grams"
        }, 
        {
            "name" : "3",
            "qty" : 11.0,
            "unit" : "grams"
        }, 
        {
            "name" : "4",
            "qty" : 32.0,
            "unit" : "grams"
        }, 
        {
            "name" : "5",
            "qty" : 87.0,
            "unit" : "grams"
        }, 
        {
            "name" : "6",
            "qty" : 312.0,
            "unit" : "grams"
        }
    ],
    "meal" : "lunch",
    "cooking-time" : 45.0,
    "prep-time" : 23.0,
    "votes" : 6.0,
    "cuisine" : "Spanish",
    "user" : "Dave",
    "last_modified" : "Fri Aug 24 11:29:22 2018"
}
```
# Deployment:
- Comment out `# For local deployment ...` section when deploying to Heroku and uncomment `# For Heroku deployment ...` section .

I have written an article on the rest of the process which is available [here](https://dev.to/davedodea/how-to-deploy-a-python-app-toheroku-5djn).

# Local install:
To install on your own machine:
- Comment out `# For Heroku deployment ...` section when deploying locally and uncomment `# For local deployment ...` section .

- Install Python3 and Pip3.

- Clone the repository to your machine: 

`git clone https://github.com/davedodea/CI-Project4.git`

- Enter the directory: 

`cd CI-Project4`

- Install the neccessary modules: 

`sudo pip3 -r install requirements.txt`

- Export the MONGO_URI for your Mongo instance: 

`export 'MONGO_URI=mongodb://<DBUSER>:<DBPASSWORD>@<SERVERURL>:<PORT>/<DBNAME>'`

- Export the MONGO_DBNAME:

`export 'MONGO_DBNAME=<DBNAME>'`

- See [here](https://docs.mlab.com/connecting/#connect-string) on how to obtain yours.

- Run the app:

`python3 app.py`

# References:
- PyMongo docs: https://api.mongodb.com/python/current/tutorial.html

# User stories/TODO lists:
Trello board can be viewed here:
https://trello.com/b/3Ks2F0lg

# Credits:
- [Materialize CSS](https://materializecss.com/) - CSS framework implementing Material design guidelines

- [Font awesome](fontawesome.com/v4.7.0/icons/) for app icon set.

- [Hover CSS](http://ianlunn.github.io/Hover/) for CSS on hover animations.

- Images from [Unsplash](https://unsplash.com).