# Works by KC
from TIGr import AbstractParser, AbstractSourceReader
import re

# class AbstractParser(ABC):
#     def __init__(self, drawer):
#         self.drawer = drawer
#         self.source = []
#         self.command = ''
#         self.data = 0
#
#     @abstractmethod
#     def parse(self, raw_source):
#         pass


class Parser(AbstractParser):

    def parse(self, raw_source):
        self.source = raw_source.splitlines()

        for command in self.source:
            command = self.remove_comment(command)
            if re.search("^P|p", command):
                # number needs to be 4 or less
                self.drawer.select_pen(int(re.search("[1-4]", command).group(0)))
                print(int(re.search("[1-4]", command).group(0)))

            elif re.search("^X|x", command):
                self.drawer.go_along(int(re.search("[-+]?[0-9]+", command).group(0)))
                print(int(re.search("[-+]?[0-9]+", command).group(0)))

            elif re.search("^Y|y", command):
                self.drawer.go_down(int(re.search("[-+]?[0-9]+", command).group(0)))
                print(int(re.search("[-+]?[0-9]+", command).group(0)))

            elif re.search("^D|d", command):
                self.drawer.pen_down()

            elif re.search("^U|u", command):
                self.drawer.pen_up()

            elif re.search("^W|w", command):
                self.drawer.draw_line(90, int(re.search("[-+]?[0-9]+", command).group(0)))
                print(int(re.search("[-+]?[0-9]+", command).group(0)))

            elif re.search("^E|e", command):
                self.drawer.draw_line(270, int(re.search("[-+]?[0-9]+", command).group(0)))
                print(int(re.search("[-+]?[0-9]+", command).group(0)))

            elif re.search("^N|n", command):
                self.drawer.draw_line(0, int(re.search("[-+]?[0-9]+", command).group(0)))
                print(int(re.search("[-+]?[0-9]+", command).group(0)))

            elif re.search("^S|s", command):
                self.drawer.draw_line(180, int(re.search("[-+]?[0-9]+", command).group(0)))
                print(int(re.search("[-+]?[0-9]+", command).group(0)))

    # Remove comment from a command
    def remove_comment(self, command):
        command_tuple = command.partition("#")
        return command_tuple[0]

    # Select a different drawer
    def select_drawer(self, drawer):
        self.drawer = drawer
