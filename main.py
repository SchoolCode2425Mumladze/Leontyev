import defs_click
from defs_click import *
import turtle

#Создание объекта черепашки и окна
t = turtle.Turtle()
screen = turtle.Screen()

#Создание и настройка окна
bg_pic_num = int(0) # Переменная необходимая для работы функции switch_background_pic() (в файле "defs_click.py")

screen.setup(1280, 720)
screen.bgpic("backgrounds/bg_pic0.gif") # Я не смог найти как указать ПУТЬ к файлу в папке, и я опять потратил на это кучу времени вручную перебирая варианты, простите...

#Настройка черепашки
color_num = int(0) # Переменная необходимая для работы функции switch_color_pen() (в файле "defs_click.py")


t.hideturtle()
t.pencolor("red")
t.fillcolor("red")
t.pensize(16)
t.speed(0)
t.penup()

defs_click.click_day1()
defs_click.click_day10()
defs_click.click_day21()
defs_click.click_day17()

screen.mainloop()
