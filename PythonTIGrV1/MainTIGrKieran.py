from TIGr import AbstractSourceReader
"""These implementations should be replaced,
by more flexible, portable and extensible solutions.
"""


class MainTIGr(AbstractSourceReader):

    def go(self):
        if config[2] == 'FrontEndKieran':
            from FrontEndKieran import TkinterInterface
            interface = TkinterInterface(self)
        elif config[2] == 'FrontEndJerry':
            from FrontEndJerry import GuiInterface
            interface = GuiInterface(self)

        interface.start()


if __name__ == '__main__':
    config = open('config.txt', "r+").read().splitlines()
    if config[0] == 'DrawerKieran':
        from DrawerKieran import Drawer
    elif config[0] == 'DrawerJack':
        from DrawerJack import Drawer

    if config[1] == 'ParserDang':
        from ParserDang import Parser
    elif config[1] == 'ParserJerry':
        from ParserJerry import Parser
    elif config[1] == 'ParserJonathan':
        from ParserJonathan import Parser

    main = MainTIGr(Parser(Drawer()))
    main.go()
