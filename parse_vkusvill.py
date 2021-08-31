import json
import time
import requests
import re
from bs4 import BeautifulSoup


filename = 'final_products.json'


def parse_products():
    data = []

    for ingredient in ingredients:
        url = 'https://vkusvill.ru/search/?q={}'.format(ingredient)
        soup = get_soup(url)
        if soup is None:
            break
        print(url)
        title_tag = soup.select_one('.ProductCard__link')
        if title_tag is None:
            continue
        img = soup.select_one('.ProductCard__imageImg')
        weight_tag = soup.select_one('.ProductCard__weight').text.strip()
        price = soup.select_one('.Price__value').text.strip()
        name = title_tag.text.strip()
        units_raw = soup.select_one('.Price__unit').text.strip()
        if units_raw == 'руб /кг':
            units = 'кг'
        else:
            units = 'уп'
        weight = re.sub('[^0-9\,]', '', weight_tag)
        weight_units = weight_tag.replace('        Точная стоимость товара зависит от веса и будет известна после сборки заказа', '').split()[-1]
        product_url = title_tag.attrs['href']
        product_image = img.attrs['data-src']

        item = {
            'ingredient': ingredient,
            'name': name,
            'price': price,
            'units': units,
            'weight': weight,
            'weight_units': weight_units,
            'product_url': 'https://vkusvill.ru{}'.format(product_url),
            'product_image': product_image,
        }
        data.append(item)
        time.sleep(2)
    
    return data


def get_soup(url, **kwargs):
    response = requests.get(url, **kwargs)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features="html.parser")
    else:
        soup = None
    return soup


def main():
    data = parse_products()

    with open(filename, 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
