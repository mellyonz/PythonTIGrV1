# Works by Jack

import turtle
from tkinter import *

import pygame
import sys
from pygame.locals import *
import MyEnums
from TIGr import AbstractDrawer


class Drawer(AbstractDrawer):
    def __init__(self, set_width=1000, set_height=1000):
        self.window = Tk()
        canvas = Canvas(self.window, width=set_width, height=set_height)
        canvas.pack()
        self.cursor = turtle.RawPen(canvas)
        self.cursor.speed(1)

    # pen_num should be int
    def select_pen(self, pen_num):
        self.cursor.color(MyEnums.Pen.colours[pen_num])

    def pen_down(self):
        self.cursor.pendown()

    def pen_up(self):
        self.cursor.penup()

    # along should be int
    def go_along(self, along):
        self.pen_up()
        self.cursor.setx(along)

    # down should be int
    def go_down(self, down):
        self.pen_up()
        self.cursor.sety(down)

    # direction and distance should be int
    def draw_line(self, direction, distance):
        self.cursor.setheading(direction)
        self.cursor.forward(distance)


# if __name__ == '__main__':
#     drawer = TurtleDrawer()
#     drawer.select_pen(2)
#     drawer.go_along(200)
#     drawer.go_down(-100)
#     drawer.pen_down()
#     drawer.draw_line(90, 100)
#     drawer.draw_line(180, 100)
#     drawer.pen_up()
#     drawer.draw_line(90, 100)
#     drawer.pen_down()
#     drawer.draw_line(90, 100)
#     drawer.draw_line(180, 100)
#     drawer.window.mainloop()


class TkinterDrawer(AbstractDrawer):

    def __init__(self, set_width=1000, set_height=1000):
        self.window = Tk()
        self.canvas = Canvas(self.window, width=set_width, height=set_height)
        self.canvas.grid(row=0, column=0)
        self.colour = ''
        self.src_x = 500
        self.src_y = 500
        self.des_x = 0
        self.des_y = 0
        self.penIsDown = False

    def select_pen(self, pen_num):
        self.colour = MyEnums.Pen.colours[pen_num]
        print("Current colour is " + self.colour)

    def pen_down(self):
        self.penIsDown = True
        print("penIsDown == " + str(self.penIsDown))

    def pen_up(self):
        self.penIsDown = False
        print("penIsDown == " + str(self.penIsDown))

    def go_along(self, along):
        self.src_x += along
        print("Move " + str(along) + " along")
        print("source_x == " + str(self.src_x) + "source_y == " + str(self.src_y))

    def go_down(self, down):
        self.src_y += down
        print("Move " + str(down) + " along")
        print("source_x == " + str(self.src_x) + "source_y == " + str(self.src_y))

    def draw_line(self, direction, distance):
        if direction == 90:
            self.des_y = self.src_y - distance
            self.des_x = self.src_x
            print("going UP " + str(distance))
        if direction == 270:
            self.des_y = self.src_y + distance
            self.des_x = self.src_x
            print("going DOWN " + str(distance))
        if direction == 0:
            self.des_x = self.src_x + distance
            self.des_y = self.src_y
            print("going RIGHT " + str(distance))
        if direction == 180:
            self.des_x = self.src_x - distance
            self.des_y = self.src_y
            print("going LEFT  " + str(distance))

        if self.penIsDown:
            print("src_x == " + str(self.src_x) + "/ src_y == " + str(self.src_y) + "des_x == " + str(
                self.des_x) + "/ des_y == " + str(self.des_y))
            self.canvas.create_line(self.src_x, self.src_y, self.des_x, self.des_y, fill=self.colour)
            print("just drew a line")

        self.src_x, self.src_y = self.des_x, self.des_y
        print("source_x == " + str(self.src_x) + "source_y == " + str(self.src_y))


# if __name__ == '__main__':
#     drawer = TkinterDrawer()
#     drawer.select_pen(2)
#     print("source_x == " + str(drawer.src_x) + "source_y == " + str(drawer.src_y))
#     drawer.go_along(200)
#     drawer.go_down(-100)
#     drawer.pen_down()
#     drawer.draw_line(90, 100)
#     drawer.draw_line(180, 100)
#     drawer.pen_up()
#     drawer.draw_line(90, 100)
#     drawer.pen_down()
#     drawer.draw_line(90, 100)
#     drawer.draw_line(180, 100)
#     drawer.window.mainloop()

class PygameDrawer(AbstractDrawer):
    def __init__(self, set_width=1000, set_height=1000):
        self.window = pygame.display.set_mode((set_width, set_height))
        self.src_x = 500
        self.src_y = 500
        self.des_x = 0
        self.des_y = 0
        self.penIsDown = False
        self.colour = MyEnums.Pen.rgb_colours[1]  # default color is red

    def select_pen(self, pen_num):
        self.colour = MyEnums.Pen.rgb_colours[pen_num]
        # print("Current colour is " + self.colour)

    def pen_down(self):
        self.penIsDown = True
        print("penIsDown == " + str(self.penIsDown))

    def pen_up(self):
        self.penIsDown = False
        print("penIsDown == " + str(self.penIsDown))

    def go_along(self, along):
        self.src_x += along
        print("Move " + str(along) + " along")
        print("source_x == " + str(self.src_x) + "source_y == " + str(self.src_y))

    def go_down(self, down):
        self.src_y += down
        print("Move " + str(down) + " along")
        print("source_x == " + str(self.src_x) + "source_y == " + str(self.src_y))

    def draw_line(self, direction, distance):
        if direction == 90:
            self.des_y = self.src_y - distance
            self.des_x = self.src_x
            print("going UP " + str(distance))
        if direction == 270:
            self.des_y = self.src_y + distance
            self.des_x = self.src_x
            print("going DOWN " + str(distance))
        if direction == 0:
            self.des_x = self.src_x + distance
            self.des_y = self.src_y
            print("going RIGHT " + str(distance))
        if direction == 180:
            self.des_x = self.src_x - distance
            self.des_y = self.src_y
            print("going LEFT  " + str(distance))

        if self.penIsDown:
            pygame.draw.line(self.window, self.colour, (self.src_x, self.src_y), (self.des_x, self.des_y))

        self.src_x, self.src_y = self.des_x, self.des_y

    @staticmethod
    def update():
        while True:
            for events in pygame.event.get():
                if events.type == QUIT:
                    sys.exit(0)
            pygame.display.update()


# if __name__ == '__main__':
#     drawer = PygameDrawer()
#     drawer.select_pen(2)
#     drawer.go_along(200)
#     drawer.go_down(-100)
#     drawer.pen_down()
#     drawer.draw_line(90, 100)
#     drawer.draw_line(180, 100)
#     drawer.pen_up()
#     drawer.draw_line(90, 100)
#     drawer.pen_down()
#     drawer.draw_line(90, 100)
#     drawer.draw_line(180, 100)
#     drawer.update()
