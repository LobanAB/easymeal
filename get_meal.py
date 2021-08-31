import argparse
import json
from pprint import pprint


def main():
    with open('your_meal.json', 'r', encoding='utf8') as json_file:
        recipes_json = json_file.read()
    recipes = json.loads(recipes_json)
    parser = argparse.ArgumentParser(
        description='Программа показывает список покупок на неделю, и меня на день.')
    parser.add_argument(
        '-gp', '--get_products', help='получить список продуктов', type=str, default='')
    parser.add_argument(
        '-day', '--day', help='Номер дня недели на который нужен рецепт', type=int, default=0)
    args = parser.parse_args()
    if args.get_products:
        print('Продукты для покупки:')
        for product, items in recipes[0]['products'].items():
            print(f'{product}, {items[1]}{items[2]} примерно {items[0]}руб.')
        print('Не забудьте проверить специи:')
        pprint(recipes[1]['condiments'])
    if args.day in range(1, 8):
        print('Завтрак:\n')
        print(recipes[2]['recipes'][0][args.day-1]['name'], '\n')
        print(recipes[2]['recipes'][0][args.day-1]['ingredients'])
        print([stage.replace('\xa0', ' ') for stage in recipes[2]['recipes'][0][args.day-1]['cooking_stages']], '\n')
        print('Обед:\n')
        print(recipes[2]['recipes'][1][args.day-1]['name'], '\n')
        print(recipes[2]['recipes'][1][args.day-1]['ingredients'])
        print([stage.replace('\xa0', ' ') for stage in recipes[2]['recipes'][1][args.day - 1]['cooking_stages']], '\n')
        print('Ужин:\n')
        print(recipes[2]['recipes'][2][args.day-1]['name'], '\n')
        print(recipes[2]['recipes'][2][args.day-1]['ingredients'])
        print([stage.replace('\xa0', ' ') for stage in recipes[2]['recipes'][2][args.day - 1]['cooking_stages']], '\n')


if __name__ == '__main__':
    main()
