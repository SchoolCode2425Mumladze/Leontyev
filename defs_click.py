import defs_keys
import turtle
import tkinter as tk
from tkinter import messagebox

t = turtle.Turtle()
screen = turtle.Screen()

t.hideturtle()
t.penup()
t.pensize(16)
t.speed(0)
t.pencolor(defs_keys.color_now)
t.fillcolor(defs_keys.color_now)

t2 = turtle.Turtle()
t2.hideturtle()

# Функции для сохранения события
def save_theme_to_file():
    window = tk.Tk()
    window.title("Ввод события")
    window.geometry("300x150")

    def save_text():
        user_text = text_entry.get("1.0", "end-1c")
        if user_text.strip():  # Проверяем, что текст не пустой
            try:
                with open("events.txt", "a", encoding="utf-8") as file:
                    file.write(user_text + "\n")
                messagebox.showinfo("Успех", "Событие успешно сохранено!")
                window.destroy()
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")
        else:
            messagebox.showwarning("Пусто", "Введите текст перед сохранением!")

    # Элементы интерфейса
    tk.Label(window, text="Введите событие:", font=("Arial", 12)).pack(pady=10)

    text_entry = tk.Text(window, height=1, width=40, font=("Arial", 10))
    text_entry.pack(pady=5)

    save_button = tk.Button(window, text="Сохранить", command=save_text,
                            bg="#4CAF50", fg="white", font=("Arial", 10))
    save_button.pack(pady=10)

    window.mainloop()

background_start = 1 # Переменная нужна для проверки состояния экрана. Состояние 0 - Календарь, Состояние 1 - Главное меню, Состояние 2 - Опции.

def click_enter(x, y): #Эта функция выполняет нажатие на кнопку "Войти"
    global background_start
    if -185 <= x <= 155 and -75 <= y <= 75 and background_start == 1:
        screen.bgpic("backgrounds/bg_pic0.gif")
        background_start = 0

def click_option(x, y): #Эта функция выполняет нажатие на кнопку "Опции"
    global background_start
    if -185 <= x <= 155 and -247 <= y <= -96 and background_start == 1:
        screen.bgpic("backgrounds/Option.gif")
        background_start = 2

def click_on_menu(x, y):
    click_enter(x, y)
    click_option(x, y)

# Для первой недели t.goto(±..., 179)
# Для второй недели t.goto(±..., 51)
# Для третьей недели t.goto(±..., -79)
# Для четвёртой недели t.goto(±..., -207)
# Для пятой недели t.goto(±..., -355)
# Для дней в неделях (с 1 по 7)(-484,-302,-119,66,249,432,615)
day1 = 0
day2 = 0
day3 = 0
day4 = 0
day5 = 0
day6 = 0
day7 = 0
day8 = 0
day9 = 0
day10 = 0
day11 = 0
day12 = 0
day13 = 0
day14 = 0
day15 = 0
day16 = 0
day17 = 0
day18 = 0
day19 = 0
day20 = 0
day21 = 0
day22 = 0
day23 = 0
day24 = 0
day25 = 0
day26 = 0
day27 = 0
day28 = 0
day29 = 0
day30 = 0
day31 = 0
day32 = 0
day33 = 0
day34 = 0
day35 = 0
def click_day1(x, y):
    global day1
    if -640 <= x <= -461 and 156 <= y <= 280:
        t.goto(-484, 179)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day1 = 1
        save_theme_to_file()

def click_day2(x, y):
    global day2
    if -457 <= x <= -278 and 156 <= y <= 280:
        t.goto(-302, 179)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day2 = 1
        save_theme_to_file()

def click_day3(x, y):
    global day3
    if -274 <= x <= -95 and 156 <= y <= 280:
        t.goto(-119, 179)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day3 = 1
        save_theme_to_file()

def click_day4(x, y):
    global day4
    if -91 <= x <= 90 and 156 <= y <= 280:
        t.goto(66, 179)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day4 = 1
        save_theme_to_file()

def click_day5(x, y):
    global day5
    if 94 <= x <= 273 and 156 <= y <= 280:
        t.goto(249, 179)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day5 = 1
        save_theme_to_file()

def click_day6(x, y):
    global day6
    if 277 <= x <= 456 and 156 <= y <= 280:
        t.goto(432, 179)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day6 = 1
        save_theme_to_file()

def click_day7(x, y):
    global day7
    if 460 <= x <= 639 and 156 <= y <= 280:
        t.goto(615, 179)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day7 = 1
        save_theme_to_file()

def click_day8(x, y):
    global day8
    if -640 <= x <= -461 and 28 <= y <= 151:
        t.goto(-484, 51)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day8 = 1
        save_theme_to_file()

def click_day9(x, y):
    global day9
    if -457 <= x <= -278 and 28 <= y <= 151:
        t.goto(-302, 51)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day9 = 1
        save_theme_to_file()

def click_day10(x, y):
    global day10
    if -274 <= x <= -95 and 28 <= y <= 151:
        t.goto(-119, 51)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day10 = 1
        save_theme_to_file()

def click_day11(x, y):
    global day11
    if -91 <= x <= 90 and 28 <= y <= 151:
        t.goto(66, 51)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day11 = 1
        save_theme_to_file()

def click_day12(x, y):
    global day12
    if 94 <= x <= 273 and 28 <= y <= 151:
        t.goto(249, 51)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day12 = 1
        save_theme_to_file()

def click_day13(x, y):
    global day13
    if 277 <= x <= 456 and 28 <= y <= 151:
        t.goto(432, 51)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day13 = 1
        save_theme_to_file()

def click_day14(x, y):
    global day14
    if 460 <= x <= 639 and 28 <= y <= 151:
        t.goto(615, 51)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day14 = 1
        save_theme_to_file()

def click_day15(x, y):
    global day15
    if -640 <= x <= -461 and -102 <= y <= 23:
        t.goto(-484, -79)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day15 = 1
        save_theme_to_file()

def click_day16(x, y):
    global day16
    if -457 <= x <= -278 and -102 <= y <= 23:
        t.goto(-302, -79)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day16 = 1
        save_theme_to_file()

def click_day17(x, y):
    global day17
    if -274 <= x <= -95 and -102 <= y <= 23:
        t.goto(-119, -79)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day17 = 1
        save_theme_to_file()

def click_day18(x, y):
    global day18
    if -91 <= x <= 90 and -102 <= y <= 23:
        t.goto(66, -79)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day18 = 1
        save_theme_to_file()

def click_day19(x, y):
    global day19
    if 94 <= x <= 273 and -102 <= y <= 23:
        t.goto(249, -79)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day19 = 1
        save_theme_to_file()

def click_day20(x, y):
    global day20
    if 277 <= x <= 456 and -102 <= y <= 23:
        t.goto(432, -79)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day20 = 1
        save_theme_to_file()

def click_day21(x, y):
    global day21
    if 460 <= x <= 639 and -102 <= y <= 23:
        t.goto(615, -79)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day21 = 1
        save_theme_to_file()

def click_day22(x, y):
    global day22
    if -640 <= x <= -461 and -230 <= y <= -107:
        t.goto(-484, -207)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day22 = 1
        save_theme_to_file()

def click_day23(x, y):
    global day23
    if -457 <= x <= -278 and -230 <= y <= -107:
        t.goto(-302, -207)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day23 = 1
        save_theme_to_file()

def click_day24(x, y):
    global day24
    if -274 <= x <= -95 and -230 <= y <= -107:
        t.goto(-119, -207)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day24 = 1
        save_theme_to_file()

def click_day25(x, y):
    global day25
    if -91 <= x <= 90 and -230 <= y <= -107:
        t.goto(66, -207)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day25 = 1
        save_theme_to_file()

def click_day26(x, y):
    global day26
    if 94 <= x <= 273 and -230 <= y <= -107:
        t.goto(249, -207)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day26 = 1
        save_theme_to_file()

def click_day27(x, y):
    global day27
    if 277 <= x <= 456 and -230 <= y <= -107:
        t.goto(432, -207)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day27 = 1
        save_theme_to_file()

def click_day28(x, y):
    global day28
    if 460 <= x <= 639 and -230 <= y <= -107:
        t.goto(615, -207)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day28 = 1
        save_theme_to_file()

def click_day29(x, y):
    global day29
    if -640 <= x <= -461 and -360 <= y <= -235:
        t.goto(-484, -355)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day29 = 1
        save_theme_to_file()

def click_day30(x, y):
    global day30
    if -457 <= x <= -278 and -360 <= y <= -235:
        t.goto(-302, -355)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day30 = 1
        save_theme_to_file()

def click_day31(x, y):
    global day31
    if -274 <= x <= -95 and -360 <= y <= -235:
        t.goto(-119, -355)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day31 = 1
        save_theme_to_file()

def click_day32(x, y):
    global day32
    if -91 <= x <= 90 and -360 <= y <= -235:
        t.goto(66, -355)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day32 = 1
        save_theme_to_file()

def click_day33(x, y):
    global day33
    if 94 <= x <= 273 and -360 <= y <= -235:
        t.goto(249, -355)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day33 = 1
        save_theme_to_file()

def click_day34(x, y):
    global day34
    if 277 <= x <= 456 and -360 <= y <= -235:
        t.goto(432, -355)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day34 = 1
        save_theme_to_file()

def click_day35(x, y):
    global day35
    if 460 <= x <= 639 and -360 <= y <= -235:
        t.goto(615, -355)
        t.pendown()
        t.begin_fill()
        t.circle(1)
        t.end_fill()
        t.penup()
        day35 = 1
        save_theme_to_file()

def clicks(x, y):
    if background_start == 1:
        while True:
            click_on_menu(x, y)
            break

    elif background_start == 0:
        print(defs_keys.color_now)
        click_day1(x, y)
        click_day2(x, y)
        click_day3(x, y)
        click_day4(x, y)
        click_day5(x, y)
        click_day6(x, y)
        click_day7(x, y)
        click_day8(x, y)
        click_day9(x, y)
        click_day10(x, y)
        click_day11(x, y)
        click_day12(x, y)
        click_day13(x, y)
        click_day14(x, y)
        click_day15(x, y)
        click_day16(x, y)
        click_day17(x, y)
        click_day18(x, y)
        click_day19(x, y)
        click_day20(x, y)
        click_day21(x, y)
        click_day22(x, y)
        click_day23(x, y)
        click_day24(x, y)
        click_day25(x, y)
        click_day26(x, y)
        click_day27(x, y)
        click_day28(x, y)
        click_day29(x, y)
        click_day30(x, y)
        click_day31(x, y)
        click_day32(x, y)
        click_day33(x, y)
        click_day34(x, y)
        click_day35(x, y)
