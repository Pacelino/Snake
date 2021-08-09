import pygame as py
from pygame.locals import *
class Control:
    def __init__(self):
        self.flag_game = True
        self.flag_direction = "Right"
        self.flag_paus = True
    def control (self):
        '''управления в зависимости от флага '''
        for event in py.event.get():  # сделили рабочей верхную панель
            if event.type == QUIT:
                self.flag_game = False
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT and self.flag_direction != "Left": # кнопка вправо
                    self.flag_direction = 'Right'
                elif event.key == K_LEFT and self.flag_direction != "Right":
                    self.flag_direction = "Left"
                elif event.key == K_UP and self.flag_direction != "Down":
                    self.flag_direction = 'UP'
                elif event.key == K_DOWN and self.flag_direction != "UP":
                    self.flag_direction = "Down"
                elif event.key == K_ESCAPE:
                    self.flag_game = False
                elif event.key == K_SPACE:
                    if self.flag_paus:
                        self.flag_paus = False
                    elif self.flag_paus == False:
                        self.flag_paus = True



