import turtle

t = turtle.Turtle()
screen = turtle.Screen()


def switch_background_pic():  # screen.onkey(switch_background_pic, "b")
    bgpic_now = None
    bg_pic_num = int(0)

    for i in range(1):
        bg_pic_num += 1

    if bg_pic_num > 3:
        bg_pic_num = 0

    background_pics = ["bg_pic0.gif", "bg_pic1.gif", "bg_pic2.gif", "bg_pic3.gif"]
    bgpic_now = screen.bgpic(background_pics[bg_pic_num])
    return bgpic_now

def switch_color_pen(): # screen.onkey(switch_color_pen, "c")
    color_now = None
    color_num = int(0)

    for i in range(1):
        color_num += 1

    if color_num > 6:
        color_num = 0

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    color_now = t.fillcolor(colors[color_num])
    return color_now

def exit_program(): # screen.onkey(exit_program(), "Escape")
    exit()