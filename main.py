import defs_click
import turtle

#Создание объекта черепашки и окна
t = turtle.Turtle()
screen = turtle.Screen()

#Настройка черепашки
t.pencolor("red")
t.fillcolor("red")
t.pensize(16)
t.speed(0)
t.penup()
t.hideturtle()

#Создание и настройка окна
bg_pic_num = int(0) # Переменная необходимая для работы функции switch_background_pic() (в файле "defs_click.py")

screen.setup(1280, 720)
screen.bgpic("backgrounds/bg_pic0.gif") # Я не смог найти как указать ПУТЬ к файлу в папке, и я опять потратил на это кучу времени вручную перебирая варианты, простите...

#Настройка черепашки
color_num = int(0) # Переменная необходимая для работы функции switch_color_pen() (в файле "defs_click.py")

screen.onscreenclick(defs_click.click_day1)

screen.mainloop()
