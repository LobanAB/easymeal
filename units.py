import json

from collections import Counter
from pprint import pprint


def main():
    with open('recipes_out.json', 'r', encoding='utf8') as json_file:
        recipes_json = json_file.read()
    recipes = json.loads(recipes_json)
    ingredients = []
    for recipe in recipes:
        for ingredient in recipe['ingredients']:
            ingredients.append(ingredient)
    data = Counter(ingredients)
    # print(data.pop('Куриное яйцо'))
    # ingr = data.keys()
    # for ingredient in ingredients:
    ingr = {}
    for recipe in recipes:
        for ingredient_name, ingredient_amount in recipe['ingredients'].items():
            if ingredient_name in ingr.keys():
                ing = ingr.pop(ingredient_name)
                ing.append(ingredient_amount)
                ingr.update({ingredient_name: ing})
            else:
                ingr.update({ingredient_name: [ingredient_amount]})
    pprint(ingr)

    '''
    with open('units.json', 'w', encoding='utf8') as my_file:
        json.dump(ingr, my_file, ensure_ascii=False)
    '''


if __name__ == '__main__':
    main()
