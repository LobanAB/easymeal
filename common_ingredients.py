import json

from collections import Counter


def main():
    with open('recipes.json', 'r', encoding='utf8') as json_file:
        recipes_json = json_file.read()
    recipes = json.loads(recipes_json)
    with open('final_products.json', 'r', encoding='utf8') as json_file:
        final_products_json = json_file.read()
    final_products = json.loads(final_products_json)
    with open('condiments.json', 'r', encoding='utf8') as json_file:
        condiments_json = json_file.read()
    condiments = json.loads(condiments_json)
    all_products = []
    for product in final_products:
        all_products.append(product['ingredient'])
    ingredients = []
    for recipe in recipes:
        for ingredient in recipe['ingredients']:
            ingredients.append(ingredient)
    data = Counter(ingredients)

    common_ingr = []
    for ingr in data.most_common():
        if (ingr[1] > 2) and (ingr[0] in all_products or ingr[0] in condiments):
            # common_ingr.append({ingr[0]: ingr[1]})
            common_ingr.append(ingr[0])
    with open('common_ingr.json', 'w', encoding='utf8') as my_file:
        json.dump(common_ingr, my_file, ensure_ascii=False)

    output_recepies = []
    for recipe in recipes:
        good = True
        for ingredient in recipe['ingredients']:
            if ingredient not in common_ingr:
                good = False
        if good:
            output_recepies.append(recipe)
    with open('recipes_out.json', 'w', encoding='utf8') as my_file:
        json.dump(output_recepies, my_file, ensure_ascii=False)


if __name__ == '__main__':
    main()
