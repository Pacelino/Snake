import pygame as py


class snake:

    def __init__(self):

        self.head = [45, 45]
        self.body = [[45, 45], [34, 45], [23, 45]]

    def move(self, control):  # движение в зависимости от напровления
        if control.flag_direction == "Right":
            self.head[0] += 11
        elif control.flag_direction == "Left":
            self.head[0] -= 11
        elif control.flag_direction == "UP":
            self.head[1] -= 11
        elif control.flag_direction == "Down":
            self.head[1] += 11

    def animation(self):
        '''Добавляем в списока тела голову, а хвост удаляем'''
        self.body.insert(0, list(self.head))
        self.body.pop()

    def draw_snake(self, window):
        """Отресова змеи """
        for segment in self.body:
            py.draw.rect(window, py.Color("Green"), py.Rect(segment[0], segment[1], 10, 10))

    def check_and_window(self):
        '''отслеживает достижение змеей края экрана'''
        if self.head[0] == 419:
            self.head[0] = 23
        elif self.head[0] == 12:
            self.head[0] = 419
        elif self.head[1] == 23:
            self.head[1] = 419
        elif self.head[1] == 419:
            self.head[1] = 34

    def eat(self, food, qui):
        '''Змея ест еду'''
        if self.head == food.food_position:
            self.body.append(food.food_position)
            food.get_food_position(qui)
            qui.get_new_indicator()
    def check_barriers(self, qui):
        if self.head in self.body[1:]:
            self.body.pop()
            qui.indicator.pop()
        if self.head in qui.barrier:
            self.body.pop()

