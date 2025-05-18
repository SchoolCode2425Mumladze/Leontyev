import defs_click
import turtle

from defs_click import screen

#Настройка черепашки
defs_click.t.pencolor("red")
defs_click.t.fillcolor("red")
defs_click.t.pensize(16)
defs_click.t.speed(0)
defs_click.t.penup()
defs_click.t.hideturtle()

defs_click.screen.setup(1280, 720)
background = ["backgrounds/Pxlendar_menu.gif"]
defs_click.screen.bgpic(background[0])
defs_click.background_start = 1 # Состояние 0 - Календарь, Состояние 1 - Главное меню, Состояние 2 - Опции.


if defs_click.background_start == 1:
    while True:
        defs_click.screen.onscreenclick(defs_click.click_on_menu)
        break
    background_start = 0

if defs_click.background_start == 2:
    while True:
        defs_click.screen.onscreenclick(defs_click.back_of_option)
        break
    background_start = 1

defs_click.screen.mainloop()
