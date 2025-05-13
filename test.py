# import turtle
#
# def click(x, y):
#     if -40 <= x <= 40 and -20 <= y <= 20:
#         turtle.write("Thank you!", align='center', font=('Arial', 18, 'bold'))
#
# screen = Screen()
#
# turtle = Turtle()
# turtle.hideturtle()
# turtle.penup()
# turtle.fillcolor('gray')
# turtle.goto(-40, -20)
#
# turtle.begin_fill()
# for _ in range(2):
#     turtle.forward(80)
#     turtle.left(90)
#     turtle.forward(40)
#     turtle.left(90)
# turtle.end_fill()
#
# turtle.goto(0, 30)
#
# screen.onclick(click)
# screen.mainloop()

# from defs_click import *
# import turtle
#
# #Создание объекта черепашки и окна
# t = turtle.Turtle()
# screen = turtle.Screen()
#
# #Создание и настройка окна
# bg_pic_num = int(0) # Переменная необходимая для работы функции switch_background_pic() (в файле "defs_click.py")
#
# screen.setup(1280, 720)
# screen.bgpic("bg_pic0.gif")
#
# #Настройка черепашки
# color_num = int(0) # Переменная необходимая для работы функции switch_color_pen() (в файле "defs_click.py")
#
#
# t.hideturtle()
# t.pencolor("red")
# t.pensize(16)
# t.speed(0)
# t.penup()
#
# click_day20()
# screen.mainloop()


