import json
import random
from collections import Counter


def ingredients_to_buy(recipes, products, condiments):
    recipes_condiments = []
    recipes_ingredients = {}
    for recipe in recipes:
        for ingredient_name, ingredient_amount in recipe['ingredients'].items():
            if ingredient_name in condiments:
                recipes_condiments.append(ingredient_name)
            elif ingredient_name in recipes_ingredients:
                recipes_ingredients.update({ingredient_name: (
                            int(recipes_ingredients.pop(ingredient_name)) + int(edit_weight(ingredient_amount)[0]))})
            else:
                recipes_ingredients.update({ingredient_name: edit_weight(ingredient_amount)[0]})
    '''  
    ingredients = Counter(recipes_ingredients).keys()
    output = {}

    for ingredient in ingredients:
        summ = 0
        for amount in recipes_ingredients[ingredient]:
            summ = summ + edit_weight(amount)[0]
        output.update({ingredient})
'''

    #  for ingr_name, ingr_amount in recipes_ingredients.items():
    #     for values in ingr_amount:
    #          output.update({ingr_name:[]})
    #          output[ingr_name] = edit_weight(values)

    print('ingr', recipes_ingredients)
    # print('cond', Counter(recipes_condiments).keys())
    # return recipes_ingredients, recipes_condiments


def edit_weight(ingredient_amount):
    ingredient_amount = ingredient_amount.replace('11/2', '2 ')
    ingredient_amount = ingredient_amount.replace('1/2', '1 ')
    ingredient_amount = ingredient_amount.replace('½', '1 ')
    amount = ingredient_amount.split()
    if 'кг' in amount:
        amount[0].split('кг')
        try:
            return int(amount[0]) * 1000, 'г'
        except ValueError:
            return int(amount[0].split(',')[0]) * 1000 + int(amount[0].split(',')[1]), 'г'
        except:
            return 500, 'г'
    elif 'лож' in amount[-1]:
        return 1, 'мл'
    elif 'шт' in amount[-1]:
        try:
            return int(amount[0].split('шт')[0]) * 200, 'г'
        except ValueError:
            return 200, 'г'
    elif 'голов' in amount[-1]:
        return int(amount[0]) * 200, 'г'
    elif 'пуч' in amount[-1]:
        return 50, 'г'
    elif 'мл' in amount[-1]:
        return amount[0], 'мл'
    elif 'вкусу' in amount[-1]:
        return 0, 0
    elif 'стеб' in amount[-1]:
        return 50, 'г'
    elif 'вет' in amount[-1]:
        return 50, 'г'
    elif 'стак' in amount[-1]:
        return 200, 'г'
    elif 'литр' in amount[-1]:
        return int(amount[0].split('литр')[0]) * 1000, 'мл'
    elif 'г' in amount[-1]:
        return amount[0], 'г'
    elif 'килог' in amount[-1]:
        return amount[0], 'килог'
    return ingredient_amount


def main():
    with open('recipes_out.json', 'r', encoding='utf8') as json_file:
        recipes_json = json_file.read()
    recipes = json.loads(recipes_json)
    with open('final_products.json', 'r', encoding='utf8') as json_file:
        products_json = json_file.read()
    products = json.loads(products_json)
    with open('condiments.json', 'r', encoding='utf8') as json_file:
        condiments_json = json_file.read()
    condiments = json.loads(condiments_json)
    meals_types = {'breakfasts': 'zavtraki', 'dinners': 'supy', 'suppers': 'osnovnye-blyuda'}
    '''
    random_recipes = {'breakfasts': random.sample([recipe for recipe in recipes
                                        if recipe['meal_type'] == meals_types['breakfasts']], 7),
                      'dinners': random.sample([recipe for recipe in recipes
                                                if recipe['meal_type'] == meals_types['dinners']], 7),
                      'suppers': random.sample([recipe for recipe in recipes
                                                if recipe['meal_type'] == meals_types['suppers']], 7)}
    '''
    random_recipes = []
    for meal_type in meals_types:
        random_recipes.append(random.sample([recipe for recipe in recipes
                                             if recipe['meal_type'] == meals_types[meal_type]], 7))

    ingredients_to_buy([x for l in random_recipes for x in l], products, condiments)


if __name__ == '__main__':
    main()