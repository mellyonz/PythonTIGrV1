from TIGr import AbstractParser
import re


class Parser(AbstractParser):

    def parse(self, raw_source):
        """hard coded parsing like this is a Bad Thing!
            It is inflexible and has no error checking
        """
        self.source = raw_source
        if raw_source is not '':
            command = re.findall(r'P\s+\d+|X\s+\d+|D|G|N\s+\d+|E\s+\d+|S\s+\d+|W\s+\d+|Y\s+\d+|U', self.source, re.M)
            print(command)
            for index in range(len(command)):
                direction = ''.join(re.findall(r'[A-Z]', command[index]))
                try:
                    data = int(''.join(re.findall(r'\d+', command[index])))
                    if direction == 'P':
                        self.drawer.select_pen(data)
                    if direction == 'G':
                        self.drawer.goto(data)
                    if direction == 'N':
                        self.drawer.draw_line(0, data)
                    if direction == 'E':
                        self.drawer.draw_line(90, data)
                    if direction == 'S':
                        self.drawer.draw_line(180, data)
                    if direction == 'W':
                        self.drawer.draw_line(270, data)
                    if direction == 'X':
                        self.drawer.go_along(data)
                    if direction == 'Y':
                        self.drawer.go_down(data)

                except ValueError:
                    if direction == 'D':
                        self.drawer.pen_down()
                    if direction == 'U':
                        self.drawer.pen_up()
