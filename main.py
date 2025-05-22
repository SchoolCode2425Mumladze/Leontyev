import defs_click
import defs_keys
import turtle

defs_click.screen.setup(1280, 725)
background = ["backgrounds/Pxlendar_menu.gif"]
defs_click.screen.bgpic(background[0])
defs_click.background_start = 1 # Состояние 0 - Календарь, Состояние 1 - Главное меню, Состояние 2 - Опции.


defs_click.screen.onscreenclick(defs_click.clicks)

defs_click.screen.onkey(defs_keys.switch_color_pen, "c")
defs_click.screen.onkey(defs_keys.back_of_option, "Escape")

defs_click.points_return()
turtle.listen()
defs_click.screen.mainloop()
