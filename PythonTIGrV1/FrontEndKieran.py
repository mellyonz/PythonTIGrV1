import os
import sys
import tkinter
from tkinter import filedialog
from tkinter.ttk import Combobox


class TkinterInterface:
    toDraw = "N 100 # then north 1cm"
    importedFile = 'Input.txt'
    window = tkinter.Tk()
    windowCanvas = tkinter.Tk()
    canvas = tkinter.Canvas(windowCanvas, width=500, height=500)

    def __init__(self, SourceReader):
        self.SourceReader = SourceReader
        self.windowCanvas.title("TK")
        self.canvas.pack()
        self.window.title("GUI")
        self.window.draw_btn = tkinter.Button(self.window, text="Draw", command=self.draw)
        self.window.draw_btn.grid(column=0, row=0)

        self.window.import_btn = tkinter.Button(self.window, text="Import new File to read", command=self.importfile)
        self.window.import_btn.grid(column=1, row=0)

        self.window.selectDrawer = tkinter.Label(self.window, text="Select Drawer")
        self.window.selectDrawer.grid(column=2, row=0)

        self.window.comboDrawer = Combobox(self.window, values=["DrawerJack", "DrawerKieran"])
        self.window.comboDrawer.set("DrawerKieran")
        self.window.comboDrawer.grid(column=3, row=0)

        self.window.selectParser = tkinter.Label(self.window, text="Select Parser")
        self.window.selectParser.grid(column=4, row=0)

        self.window.comboParser = Combobox(self.window, values=["ParserDang", "ParserJerry", "ParserJonathan"])
        self.window.comboParser.set("ParserDang")
        self.window.comboParser.grid(column=5, row=0)

        self.window.selectInterface = tkinter.Label(self.window, text="Select Interface")
        self.window.selectInterface.grid(column=6, row=0)

        self.window.comboInterface = Combobox(self.window, values=["FrontEndJerry", "FrontEndKieran"])
        self.window.comboInterface.set("FrontEndKieran")
        self.window.comboInterface.grid(column=7, row=0)

        self.window.close_btn = tkinter.Button(self.window, text="Restart", command=self.restart_program)
        self.window.close_btn.grid(column=8, row=0)

        self.window.toDrawLabel = tkinter.Label(self.window, text=self.toDraw)
        self.window.toDrawLabel.grid(column=1, row=1, columnspan=8)

    def start(self):
        self.window.mainloop()

    def restart_program(self):
        """Restarts the current program.
        Note: this function does not return. Any cleanup action (like
        saving data) must be done before calling this function."""
        file = open('config.txt', 'w')
        file.write(self.window.comboDrawer.get() + '\n'
                   + self.window.comboParser.get() + '\n'
                   + self.window.comboInterface.get())
        file.close()
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def draw(self):
        self.SourceReader.parser.parse(self.toDraw)
        self.window.toDrawLabel.config(text=self.toDraw)

    def importfile(self):
        self.importedFile = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file",
                                                       filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
        self.toDraw = open(self.importedFile, "r+").read()
