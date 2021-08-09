import pygame as py
import random

class Food:
    def __init__(self):
        self.food_position = []

    def get_food_position(self, qui):
        '''выдает рандомное значение координат для еды'''
        self.food_position = random.choice(qui.field)
    def draw_food(self, window):
        '''Отрисовавывает еду'''
        py.draw.rect(window, py.Color("Red"), py.Rect(self.food_position[0], self.food_position[1], 10, 10))