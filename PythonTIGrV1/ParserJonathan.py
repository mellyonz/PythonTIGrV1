from TIGr import AbstractParser
import re


class Parser(AbstractParser):
    def __init__(self, drawer):
        super().__init__(drawer)
        self.command_list = {
            "P": "self.drawer.select_pen(self.data)",
            "D": "self.drawer.pen_down()",
            "N": "self.drawer.draw_line(360, self.data)",
            "E": "self.drawer.draw_line(90, self.data)",
            "S": "self.drawer.draw_line(180, self.data)",
            "W": "self.drawer.draw_line(270, self.data)",
            "X": "self.drawer.go_along(self.data)",
            "Y": "self.drawer.go_down(self.data)",
            "U": "self.drawer.pen_up()"
        }

    def parse(self, raw_source):
        # Jonathan Holdaway worked on this
        self.source = raw_source.splitlines()
        for line in self.source:
            inputs = re.findall("[.\w]+", line)
            self.command = inputs[0].upper()
            try:
                self.data = int(inputs[1])
            except():
                self.data = 0
            # if self.command[0] == 'P':
            #     self.drawer.select_pen(self.data)
            # if self.command[0] == 'D':
            #     self.drawer.pen_down()
            # if self.command[0] == 'N':
            #     self.drawer.draw_line(360, self.data)
            # if self.command[0] == 'E':
            #     self.drawer.draw_line(90, self.data)
            # if self.command[0] == 'S':
            #     self.drawer.draw_line(180, self.data)
            # if self.command[0] == 'W':
            #     self.drawer.draw_line(270, self.data)
            # if self.command[0] == 'X':
            #     self.drawer.go_along(self.data)
            # if self.command[0] == 'Y':
            #     self.drawer.go_down(self.data)
            # if self.command[0] == 'U':
            #     self.drawer.pen_up()
            if self.command[0] in self.command_list:
                parsed_command = self.command_list[self.command[0]]
                exec(parsed_command)
