import pygame as py
from control import Control
from class_Snake import snake
from gui import Gui
from food import Food
py.init()
window = py.display.set_mode((441, 441)) # создали окно
py.display.set_caption("Первая змейка !!!") # поменяли название окна
control = Control()
Snake = snake()
py.display.flip()  # отоброзили окно
qui = Gui()
food = Food()
qui.inits_field()

food.get_food_position(qui)
speed = 0
while control.flag_game: # окно перестало выключаться сомо по себе
    qui.cheeck_win_or_lose()
    control.control()
    window.fill(py.Color("Black")) # закрашивание окна в определенный цвет
    if qui.game == "GAME":
        Snake.draw_snake(window)
        food.draw_food(window)
    elif qui.game == "WIN":
        qui.draw_win(window)
    elif qui.game == 'LOSE':
        qui.draw_lose(window)
    qui.draw_indicator(window)
    qui.draw_level(window)
    if speed % 50 == 0 and control.flag_paus and qui.game == 'GAME':
        Snake.check_barriers(qui)
        Snake.move(control)
        Snake.eat(food, qui)
        Snake.check_and_window()
        Snake.animation()
    speed += 1
    py.display.flip()