# Фильтрация данных

# Предположим, что есть какой-то массив содержащий данные о разных людях и их возрасте и вас попросили ответить на следующий вопрос: “сколько в массиве людей возраста > 30?”. Для этого, вы хотите написать программу для фильтрации наблюдений по возрастному признаку.
# Ваша задача: Написать скрипт принимающий на вход массив с данными о людях и число - возраст, а возвращающий число - количество людей старше указанного возраста.

people = [
    {'name': 'Hghgh', 'age': 20},
    {'name': 'Jsdes', 'age': 25},
    {'name': 'Lifnhc', 'age': 30},
    {'name': 'Mjncdy', 'age': 35},
    {'name': 'Dokmnf', 'age': 40},
]
def filter_by_age(people:list, min_age:int) -> list:
    return list(filter(lambda pers: min_age <= pers['age'], people))

age = 27
filterd_people = filter_by_age(people, age)
print(filterd_people)
print(len(filterd_people))