import json

import requests
from bs4 import BeautifulSoup
import time


def get_recipes(meal_type='supy', page=1):
    url = f'https://eda.ru/recepty/{meal_type}'
    payload = {"page": page}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    name = [name.text for name in soup.find_all("a", class_="css-17vxl0k")]
    recipe_link = [href['href'] for href in soup.find_all("a", class_="css-17vxl0k")]
    img_link = [img_src['src'] for img_src in soup.select('.css-3uhzwz-ImageBase > img')]
    return [{'name': name[i],
             'recipe_link': recipe_link[i],
             'img_link': img_link[i],
             'meal_type': meal_type} for i in range(len(name))]


def get_recipe(recipe_link):
    url = f'https://eda.ru{recipe_link}'
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    ingredients_name = [name.text for name in soup.find_all('span', attrs={'itemprop': 'recipeIngredient'})]
    ingredients_amount = [amount.text for amount in soup.find_all('span', class_='css-1t5teuh-Info')]
    ingredients = dict(zip(ingredients_name, ingredients_amount))
    portion = soup.find('div', class_='css-1047m5l').text
    energy_value = {
        'calories': soup.find('span', attrs={'itemprop': 'calories'}).text,
        'protein': soup.find('span', attrs={'itemprop': 'proteinContent'}).text,
        'fat': soup.find('span', attrs={'itemprop': 'fatContent'}).text,
        'carbohydrate': soup.find('span', attrs={'itemprop': 'carbohydrateContent'}).text
    }
    cooking_time = soup.find_all('span', class_='css-1pyyg4z-Info')[1].text
    cooking_stages = [stage.text for stage in soup.find_all('span', attrs={'itemprop': 'text'})]
    recipe = {'ingredients': ingredients,
              'portion': portion,
              'energy_value': energy_value,
              'cooking_time': cooking_time,
              'cooking_stages': cooking_stages
              }
    return recipe


def get_recipes_type2(meal_type='osnovnye-blyuda', page=1):
    url = f'https://eda.ru/recepty/{meal_type}'
    payload = {"page": page}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    name = [name.span.text.strip() for name in soup.find_all("h3", class_="horizontal-tile__item-title item-title")]
    recipe_link = [href.a['href'] for href in soup.find_all("h3", class_="horizontal-tile__item-title item-title")]
    img_link = [img_src['data-src'] for img_src in soup.find_all("div", class_="lazy-load-container")]
    return [{'name': name[i],
             'recipe_link': recipe_link[i],
             'img_link': img_link[i],
             'meal_type': meal_type} for i in range(len(name))]


def get_recipe_type2(recipe_link):
    url = f'https://eda.ru{recipe_link}'
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    ingredients_name = [name.text.strip() for name in soup.find_all('span', attrs={'itemprop': 'recipeIngredient'})]
    ingredients_amount = [amount.text for amount in soup.find_all('span', class_='content-item__measure '
                                                                                 'js-ingredient-measure-amount')]
    ingredients = dict(zip(ingredients_name, ingredients_amount))
    portion = soup.find('span', attrs={'itemprop': 'recipeYield'}).text
    energy_value = {
        'calories': soup.find('span', attrs={'itemprop': 'calories'}).text,
        'protein': soup.find('span', attrs={'itemprop': 'proteinContent'}).text,
        'fat': soup.find('span', attrs={'itemprop': 'fatContent'}).text,
        'carbohydrate': soup.find('span', attrs={'itemprop': 'carbohydrateContent'}).text
    }
    cooking_time = soup.select('.info-text')[1].text
    cooking_stages = [stage.text for stage in soup.find_all('span', attrs={'itemprop': 'text'})]
    recipe = {'ingredients': ingredients,
              'portion': portion,
              'energy_value': energy_value,
              'cooking_time': cooking_time,
              'cooking_stages': cooking_stages
              }
    return recipe


def save_recipes_to_file(recipes):
    with open('recipes.json', 'w', encoding='utf8') as my_file:
        json.dump(recipes, my_file, ensure_ascii=False)


def main():
    meals_types1 = ['zavtraki', 'supy']
    meals_types2 = ['osnovnye-blyuda']
    pages = 10
    recipes = []
    for meal in meals_types1:
        for page in range(1, pages + 1):
            page_recipes = get_recipes(meal, page)
            for recipe in page_recipes:
                recipes.append(recipe)
            time.sleep(5)
        for recipe in recipes:
            recipe.update(get_recipe(recipe['recipe_link']))
    recipes_type2 = []
    for meal in meals_types2:
        for page in range(1, pages + 1):
            page_recipes = get_recipes_type2(meal, page)
            for recipe in page_recipes:
                recipes_type2.append(recipe)
            time.sleep(5)
        for recipe in recipes_type2:
            recipe.update(get_recipe_type2(recipe['recipe_link']))
    recipes = recipes + recipes_type2
    save_recipes_to_file(recipes)


if __name__ == '__main__':
    main()
