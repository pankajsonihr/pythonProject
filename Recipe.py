import requests
api_key = 'b66210af2884486fb77a9d2ff8018932'

def search_recipes(recipe_name):
    url = f'https://api.spoonacular.com/recipes/search?apiKey={api_key}&query={recipe_name}'

    response = requests.get(url)
    results = response.json()['results']

    return results

def get_recipe_summary(recipe_name):
    recipes = search_recipes(recipe_name)
    if len(recipes) == 0:
        print(f"No recipe found for {recipe_name}")
        return

    recipe_id = recipes[0]['id'] # use the ID of the first recipe found
    url = f'https://api.spoonacular.com/recipes/{recipe_id}/information?apiKey={api_key}'

    response = requests.get(url)
    recipe_info = response.json()

    print(recipe_info['summary'])

# example usage
def recipe_summary(recipe):
    return f"{get_recipe_summary(recipe)}"