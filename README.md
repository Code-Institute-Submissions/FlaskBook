[![Build Status](https://travis-ci.com/davedodea/FlaskBook.svg?branch=master)](https://travis-ci.com/davedodea/FlaskBook)
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

- As a user who wants to view all cuisines, I should see a link to "cuisines" where I can see a list of all cuisines, each displaying the following:
    - cuisine name.
    - edit button.
    - delete button.

- As user who wants to add a cuisine, I should see a link on the cuisines page where i can see a form with the option to add a cuisine by title to the database.


## Testing, validation and styling
#### Testing
- The site was tested on all modern desktop and mobile browsers to ensure cross compatibility and functionality.
- The site was tested to be responsive and to ensure it would be correctly displayed across mobile devices.
- I ensured that each one of the user stories were thoroughly tested to be functional without errors.
- Testing for this project was implemented manually. The majority of testing covered the various Flask routes. Some examples of issues/tests on routes:
- When on the homepage, when clicking on a recipe category and no recipes for such a category exist then the user will be directed to the all recipes route.
- When using the search bar, if nothing is input into the search field then the user will shown al recipes.
- When sorting recipes by parameters i.e. newest/oldest, votes desc/asc etc. - if such a parameter is not recorded in any given document, it is omitted from the sorted list which is returned.
- On the add recipe form all necessary fields i.e. title, cuisine etc. - were given the `required` tag to ensure the user did not submit empty/partially filled recipes.
- For text-area and inputs, a `max-length` was added to restrict input length.

#### Python linting
- All code was linted and formatted to the [Pep8](https://www.python.org/dev/peps/pep-0008/) standard.

## Features overview
- Add a recipe.
- Edit recipes.
- Search for recipes.
- Add cuisines.
- Edit cuisines.

### Features I'd like to implement in future versions
- User authentication system
- Sharable recipes.
- Export to PDF.
- Implement search caching/indexing.

## Challenges
- Learning how to integrate Flask and MongoDB was a great learning experience. I learned much from how to manage and interact with a NoSQL data store.

- Managing routes and URL's with Flask was also very interesting and I learned a great deal from reading the documentation around Flask and MongoDB.


## Technologies Used
- [HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/bm/docs/Web/JavaScript)
- [jQuery](https://jquery.com/) - for DOM manipulation.
- [Bootstrap](https://getbpptstrap.com) - Bootstrap is used as the primary CSS framework.
- [Flask](http://flask.pocoo.org/) - MVT (Mode-View-Template) framework used to build the application. 
- [MongoDB](https://www.mongodb.com/) - Relational database store for model data.
- [Heroku](https://www.heroku.com/) - Platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
- [Travis-CI](https://travis-ci.com) - Test and deploy code projects.
- [mLab](https://mlab.com/) - Database-as-a-Service for MongoDB.


## Production Deployment
I have written an article on the rest of the process which is available [here](https://dev.to/davedodea/how-to-deploy-a-python-app-toheroku-5djn).

- A live version of this app is available [here](https://glacial-brook-98593.herokuapp.com/).

- The Flask application is deployed to a Heroku instance.

- The MongoDB is deployed to an mLab instance.

- Testing is triggered via TravisCI upon PR's to the GitHub repository.

- Once TravisCI builds successfully, deployment is carried out on Heroku.

##### The process I took was as follows:
- Set up a new instance of a Heroku app, along with a mLab instance.
- Store the necessary config variables in the Heroku app settings.
- Set the necessary  variables in the Flask app settings.
- Set up Travis-CI to trigger when pushes are made to the repository, set up with a yml config file.
- Set up a automatic deployment hook on Heroku to trigger once Travis-CI has completed.
- Deploy by pushing to GitHub

- If you wish to deploy - ensure you have set the following config vars set in Heroku app settings:
```
    - 'IP'
    - 'MONGO_URI'
    - 'PORT'
```

## Install/deploy locally
### Ensure to comment out the `# For Heroku deployment` section of `app.py` when deploying locally.
### Uncomment the `# For local deployment` section

This is the process I have tested to enable local development and deployment.
- Clone the repository.

- CD into the repository.

- Activate a virtual environment using `pipenv shell`.

- ### **Important** Ensure you have set the environment variables in `env.py`: 
    ```python
    import os

    # assessor DB user details
    os.environ['MONGO_URI'] = 'mongodb://codeinst:codeinstitute2019@ds125402.mlab.com:25402/testmenudb'
    os.environ['MONGO_DBNAME'] = 'testmenudb'
    ```
- Install requirements: `pipenv install`

- Run the server: `python3 app.py`


## References:
- PyMongo docs: https://api.mongodb.com/python/current/tutorial.html
- Flask docs: http://flask.pocoo.org/docs/1.0/

## Databse schema:
- The main MongoDB collection `recipes` takes he following schema.

```json
{
    "_id": {
        "$oid": "5c78652fe64d1e68d7eba7a6"
    },
    "title": "Chocolate cake",
    "description": "Dark chocolate sponge cake",
    "method": "Mix all ingredients. Bake for 35 mins at 180C",
    "ingredients": [
        "Chocolate",
      "6 Eggs",
      "125ml millke",
      "200g Flour"
    ],
    "meal": "dessert",
    "serves": "4",
    "cooking-time": "30",
    "prep-time": "10",
    "cuisine": "French",
    "user": "Dave",
    "last_modified": "Thu Feb 28 22:48:15 2019"
  }
```

## Credits

### Third-party
- [Materialize CSS](https://materializecss.com/) CSS framework implementing Material design guidelines

- [Font awesome](fontawesome.com/v4.7.0/icons/) for app icon set.

- [Hover CSS](http://ianlunn.github.io/Hover/) for CSS on hover animations.

- [Unsplash](https://unsplash.com) for images.