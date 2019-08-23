import math
from TIGr import AbstractDrawer


class Drawer(AbstractDrawer):
    x_pos = 250
    y_pos = 250
    config = open('config.txt', "r+").read().splitlines()
    if config[2] == 'FrontEndKieran':
        from FrontEndKieran import TkinterInterface
        this_canvas = TkinterInterface.canvas
    elif config[2] == 'FrontEndJerry':
        from FrontEndJerry import GuiInterface
        this_canvas = GuiInterface.canvas

    def __init__(self):
        self.can_draw = False

    def select_pen(self, pen_num):
        print(f'Selected pen {pen_num}')

    def pen_down(self):
        self.can_draw = True
        print('pen down')

    def pen_up(self):
        self.can_draw = False
        print('pen up')

    def go_along(self, along):
        self.x_pos = along
        print(f'GOTO X={along}')

    def go_down(self, down):
        self.y_pos = down
        print(f'GOTO Y={down}')

    def draw_line(self, direction, distance):
        """
        This draw line abstract child class will change vector direction and distance into x and y coordinates
        :param direction: vector direction with 0 north 90 east 180 south 270 west
        :param distance: distance * number to be more noticeable
        :return: nothing
        """
        if self.can_draw:
            if direction == 0:
                direction = 360
            # test a direction angle direction = 30 Angle direction needs to be converted a decimal and divided into
            # pie. This is required math.sin and math.cos
            direction = (math.pi * 2) / (360 / direction)
            # print(direction)
            new_x = distance * math.sin(direction)
            new_y = -distance * math.cos(direction)
            # print(new_x)
            # print(new_y)
            self.this_canvas.create_line(self.x_pos, self.y_pos, self.x_pos + new_x, self.y_pos + new_y, fill="red")
            self.x_pos += new_x
            # print(self.x_pos)
            self.y_pos += new_y
            # print(self.y_pos)
            print(f'drawing line of length {distance} at {direction} degrees')
