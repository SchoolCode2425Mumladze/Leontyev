import defs_click
import turtle


bg_pic_num = 0
bg_pic_now = "backgrounds/bg_pic0.gif"

def switch_background_pic():  # screen.onkey(switch_background_pic, "b")
    global bg_pic_num
    global bg_pic_now

    bg_pic_num = int(0)

    for i in range(1):
        bg_pic_num += 1

    if bg_pic_num > 3:
        bg_pic_num = 0

    background_pics = ["backgrounds/bg_pic0.gif", "backgrounds/bg_pic1.gif", "backgrounds/bg_pic2.gif", "backgrounds/bg_pic3.gif"]
    bg_pic_now = background_pics[bg_pic_num]
    defs_click.screen.bgpic(background_pics[bg_pic_num])
    return print(bg_pic_now)


colors = ["red", "orange", "yellow", "green", "blue", "purple"]
color_num = 0
color_now = colors[color_num]


def switch_color_pen():
    global color_num, color_now

    color_num = (color_num + 1) % len(colors)
    color_now = colors[color_num]

    # Обновляем цвет черепашки сразу при переключении
    defs_click.t.pencolor(color_now)
    defs_click.t.fillcolor(color_now)

    return color_now


def back_of_option():
    defs_click.screen.bgpic("backgrounds/Pxlendar_menu.gif")
    defs_click.background_start = 1
    defs_click.t.clear()