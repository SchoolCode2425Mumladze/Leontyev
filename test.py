# import turtle as t
# turtle = t.Turtle()
# screen = t.Screen()
#
#
#Создание и настройка окна
#bg_pic_num = int(0) # Переменная необходимая для работы функции switch_background_pic() (в файле "defs_click.py")
#
#screen.setup(1280, 720)
#screen.bgpic("backgrounds/bg_pic0.gif") # Я не смог найти как указать ПУТЬ к файлу в папке, и я опять потратил на это кучу времени вручную перебирая варианты, простите...
#
#Настройка черепашки
#color_num = int(0) # Переменная необходимая для работы функции switch_color_pen() (в файле "defs_click.py")
#
#screen.onscreenclick(defs_click.click_day1)
#
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
#
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


import tkinter as tk


class HoverApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")
        self.root.title("Hover Detection")

        # Создаем зону для отслеживания (прямоугольник)
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Рисуем целевую область
        self.target_area = self.canvas.create_rectangle(
            150, 100, 250, 200,  # Координаты [x1, y1, x2, y2]
            fill="lightblue",
            outline="black"
        )

        # Текст для отображения статуса
        self.status_text = self.canvas.create_text(
            200, 50,
            text="Наведите курсор на синий квадрат",
            font=("Arial", 12)
        )

        # Привязываем события мыши
        self.canvas.tag_bind(self.target_area, "<Enter>", self.on_hover_enter)
        self.canvas.tag_bind(self.target_area, "<Leave>", self.on_hover_exit)

        # Для произвольных координат используем Motion
        self.canvas.bind("<Motion>", self.track_motion)

    def on_hover_enter(self, event):
        self.canvas.itemconfig(self.target_area, fill="green")
        self.canvas.itemconfig(self.status_text, text="Курсор ВНУТРИ зоны!")

    def on_hover_exit(self, event):
        self.canvas.itemconfig(self.target_area, fill="lightblue")
        self.canvas.itemconfig(self.status_text, text="Курсор СНАРУЖИ зоны")

    def track_motion(self, event):
        # Проверяем, находится ли курсор в произвольной области
        x, y = event.x, event.y
        if 150 < x < 250 and 100 < y < 200:  # Координаты целевой зоны
            self.canvas.itemconfig(self.status_text, text=f"Координаты: ({x}, {y})")


if __name__ == "__main__":
    root = tk.Tk()
    app = HoverApp(root)
    root.mainloop()