from tkinter import * 
class GuiInterface:
    def __initGui__(self,button1,button2):
        self.__button1 = button1
        self.__button2 = button2
    def getButton1(self):
        return self.__button1
    def getButton2(self):
        return self.__button2
    def setButton1(self, setButton):
        self.__button1 = setButton
    def setButton2(self, setButton):
        self.__button2 = setButton
    def runGui(self):
        self.gui = Tk()
        self.gui.title("Hello World")
        self.gui.geometry('900x150')
        self.gui.tk.call('tk','scaling',3.0)
        self.gui.mainloop()