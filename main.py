import defs_click
# import turtle

#Настройка черепашки
defs_click.t.pencolor("red")
defs_click.t.fillcolor("red")
defs_click.t.pensize(16)
defs_click.t.speed(0)
defs_click.t.penup()
defs_click.t.hideturtle()

defs_click.screen.setup(1280, 720)
defs_click.screen.bgpic("backgrounds/Pxlendar_menu_buttons.gif")

defs_click.screen.onscreenclick(defs_click.click_entrance)

defs_click.screen.mainloop()
