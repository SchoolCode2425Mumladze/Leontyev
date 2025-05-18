import defs_click
#import turtle


bg_pic_num = None
bg_pic_now = None
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

color_num = None
color_now = None
def switch_color_pen(): # screen.onkey(switch_color_pen, "c")
    global color_num
    global color_now

    color_num = int(0)

    for i in range(1):
        color_num += 1

    if color_num > 6:
        color_num = 0

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    color_now = colors[color_num]
    defs_click.t.fillcolor(colors[color_num])
    return color_now

def exit_program(): # screen.onkey(exit_program, "Escape")
    exit()