# 1. Императивная и декларативная парадигмы:  генераторы списков и метод map - признаки декларативной (если быть точным - функциональной) парадигмы, а весь остальной код остаётся в рамках императивного стиля

numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
even_numbers = [x for x in numbers if x % 2 == 0]
doubled_numbers = list(map(lambda x: x * 2, numbers))

print("Квадраты чисел: ", squared_numbers)
print("Четные числа: ", even_numbers)
print("Удвоенные числа: ", doubled_numbers)

# 2.  Объектно-ориентированная парадигма:  в данном коде определяются два класса Vehicle и Car и их методы __init__, start_engine, stop_engine

class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

class Car(Vehicle):
    def start_engine(self):
        print(f"{self.color} автомобиль {self.brand} завел двигатель")
    
    def stop_engine(self):
        print(f"{self.color} автомобиль {self.brand} заглушил двигатель")

# 3.  Объектно-ориентированная парадигма (ООП), процедурная и структурная парадигмы: объявлен класс MusicPlayer, его конструктор и метод add_song. Для создания плейлиста используется стандартная процедура (НЕ метод), также используется цикл for, и нет goto.

class MusicPlayer:
    def __init__(self):
        self.playlist = []

    def add_song(self, song):
        self.playlist.append(song)

def create_playlist(player:MusicPlayer, songs:list):
    for song in songs:
        player.add_song(song)

player = MusicPlayer()
create_playlist(player)