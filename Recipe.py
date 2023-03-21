import requests
import API

# https://developer.edamam.com/

APP_ID = API.RECIPE_APP_ID
APP_KEY = API.RECIPE_APP_KEY

endpoint = "https://api.edamam.com/search"


def search_recipes(recipe_name):
    info = ""
    # Set parameters for recipe search
    params = {
        "app_id": APP_ID,
        "app_key": APP_KEY,
        "q": recipe_name
    }

    # Send GET request to API with search parameters
    response = requests.get(endpoint, params=params)
    # Check if response was successful
    if response.status_code == 200:
        # Extract recipe information from JSON response
        data = response.json()
        hits = data["hits"]
        for hit in hits:
            recipe = hit["recipe"]
            info = "Recipe name is " + recipe["label"] + "I can only give the name of ingredient that you can use to cook it for more information you have to visit www.edamam.com"
            for ingredient in recipe["ingredientLines"]:
                info = info + ingredient + ", "
            # So we don't get more than one recipe info.
            break
        return info
    else:
        return "Error: Could not retrieve recipe information."
