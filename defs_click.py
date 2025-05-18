import defs_keys
import turtle

t = turtle.Turtle()
screen = turtle.Screen()

t.hideturtle()
t.penup()
t.pensize(16)
t.speed(0)
t.pencolor("red")
t.fillcolor("red")

background_start = 1 # Состояние 0 - Календарь, Состояние 1 - Главное меню, Состояние 2 - Опции.

def click_enter(x, y): #Эта функция выполняет нажатие на кнопку "Войти"
    global background_start
    if -185 <= x <= 155 and -75 <= y <= 75:
        screen.bgpic("backgrounds/bg_pic0.gif")
    background_start = 0

def click_option(x, y): #Эта функция выполняет нажатие на кнопку "Опции"
    global background_start
    if -185 <= x <= 155 and -247 <= y <= -96:
        screen.bgpic("backgrounds/Option.gif")
    background_start = 2

def back_of_option(x, y):
    global background_start
    if 455 <= x <= 640 and 232 <= y <= 361:
        screen.bgpic("backgrounds/Pxlendar_menu.gif")
    background_start = 1

def click_on_menu(x, y):
    click_enter(x, y)
    click_option(x, y)
    back_of_option(x, y)

# УЖЕ НЕ НУУУУЖНО, МИША НЕ СМОТРИ СЮДА ПОКА ПИШЕШЬ КООРДИТАТЫ, СЛЫШИШЬ? АЛОООООООО! СЛЫШИШЬ????
# Для первой недели t.goto(±..., 179)
# Для второй недели t.goto(±..., 51)
# Для третьей недели t.goto(±..., -79)
# Для четвёртой недели t.goto(±..., -207)
# Для пятой недели t.goto(±..., -355)
# Для дней в неделях (с 1 по 7)(-484,-302,-119,66,249,432,615)

def click_day1(x, y):
    t.penup()
    if -640 <= x <= -461 and 156 <= y <= 280:
        t.goto(-484, 179)
        t.pendown()
        t.begin_fill()
        t.fillcolor(defs_keys.color_now)
        t.circle(1)
        t.end_fill()

def click_day2(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(-302, 179)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day3(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(-119, 179)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day4(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(66, 179)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day5(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(249, 179)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day6(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(432, 179)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day7(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(615, 179)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day8(x, y):
    if -640 <= x <= -461 and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(-484, 51)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day9(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(-302, 51)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day10(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(-119, 51)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day11(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(66, 51)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day12(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(249, 51)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day13(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(432, 51)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day14(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(615, 51)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day15(x, y):
    if -640 <= x <= -461 and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(-484, -79)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day16(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(-302, -79)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day17(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(-119, -79)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day18(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(66, -79)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day19(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(249, -79)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day20(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(432, -79)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day21(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(615, -79)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day22(x, y):
    if -640 <= x <= -461 and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(-484, -207)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day23(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(-302, -207)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day24(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(-119, -207)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day25(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(66, -207)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day26(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(249, -207)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day27(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(432, -207)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day28(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(615, -207)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day29(x, y):
    if -640 <= x <= -461 and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(249, -355)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day30(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(432, -355)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()

def click_day31(x, y):
    if 1 <= x <= ... and 2 <= y <= ...:
        ...
    t.penup()
    t.hideturtle()
    t.goto(615, -355)
    t.pendown()
    t.begin_fill()
    t.fillcolor(defs_keys.color_now)
    t.circle(1)
    t.end_fill()