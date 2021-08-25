import requests
from bs4 import BeautifulSoup


def get_recipes():
    meal_type = 'supy'
    url = f'https://eda.ru/recepty/{meal_type}'
    payload = {"page": 1}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')
    print('name', soup.find_all("a", class_="css-17vxl0k")[0].text)
    print('href', soup.find_all("a", class_="css-17vxl0k")[0]['href'])
    img_src = soup.select('.css-3uhzwz-ImageBase > img')[0]['src']
    print(img_src)
    return soup.find_all("a", class_="css-17vxl0k")[0]['href']

def get_recipe_info(recipe_link):
    url = f'https://eda.ru{recipe_link}'
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'lxml')

    ingredients_name = [name.text for name in soup.find_all('span', attrs={'itemprop': 'recipeIngredient'})]
    ingredients_amount = [amount.text for amount in soup.find_all('span', class_='css-1t5teuh-Info')]
    ingredients = dict(zip(ingredients_name, ingredients_amount))
    print(ingredients)
    print('порция', soup.find('div', class_='css-1047m5l').text)
    energy_value = {
        'calories': soup.find('span', attrs={'itemprop': 'calories'}).text,
        'protein': soup.find('span', attrs={'itemprop': 'proteinContent'}).text,
        'fat': soup.find('span', attrs={'itemprop': 'fatContent'}).text,
        'carbohydrate': soup.find('span', attrs={'itemprop': 'carbohydrateContent'}).text
    }
    print(energy_value)
    time = soup.find_all('span', class_='css-1pyyg4z-Info')[1].text
    print(time)


def main():
    link = get_recipes()
    get_recipe_info(link)


if __name__ == '__main__':
    main()
