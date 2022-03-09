import tkinter as tk
import math

def position(data):
    center_x, center_y, r, distance, angle, angle_speed, x, y = data
    x = center_x - distance * math.sin(math.radians(-angle))
    y = center_y - distance * math.cos(math.radians(-angle))
    data[6] = x
    data[7] = y
    x1 = x - r
    y1 = y - r
    x2 = x + r
    y2 = y + r
    return x1, y1, x2, y2

def create_object(data):
    x1, y1, x2, y2 = position(data)
    return canv.create_oval(x1, y1, x2, y2, fill="white")

def move_object(object_id, data):
    x1, y1, x2, y2 = position(data)
    canv.coords(object_id, x1, y1, x2, y2)

def animation():
    moving_oval[4] += moving_oval[5]
    move_object(e_id, moving_oval)
    main.after(move_speed_control, animation)


# регулизование значений
move_clockwise = 1  # 1: движение по часовой, 0 - против
move_speed_control = 10  # переменная отвечает за скорость движения круга

width = 600
height = 600
center_x = width//2
center_y = height//2

main_oval = [center_x, center_y, 200, 0, 0, 0, 0, 0]
moving_oval = [center_x, center_y, 10, 200, 200, move_clockwise, 0, 0]

main = tk.Tk()
main.title("tkinter")

canv = tk.Canvas(main, width=width, heigh=height, bg="green")
canv.pack()

create_object(main_oval)
e_id = create_object(moving_oval)

animation()
main.mainloop()