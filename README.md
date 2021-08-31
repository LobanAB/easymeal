# Easy Meal

Программа генерирует план питания на неделю, выводит рецепты по дням в консоль, а с помощью специальной команды генерирует список покупок, необходимых для приготовления блюд.


## Как установить

Скачать программу из удаленного репозитория:

```
git clone https://github.com/LobanAB/easymeal.git
```

Python3 должен быть уже установлен.


## Как запустить

Для генерации плана питания на неделю запустите в консоли:

```
$ python3 easymeal.py
```
Эта команда сгенерирует файл `your_meal.json`.

Чтобы узнать меню на конкретный день, в консоли нужно выполнить:

```
python3 get_meal.py -day 1
```
Цифра "1" в конце - день недели. В консоль при этом выведется меню на понедельник. Чтобы узнать менб на вторник, среду и другие дни, нужно ввести "2", "3" и т.д.

Чтобы узнать список покупок на неделю, в консоль нужно ввести следующую команду:

```
get_meal.py -gp 1
```

## Цель проекта

Код написан в учебных целях — это проект на курсе по Python и веб-разработке на сайте [dvmn.org](https://dvmn.org/).