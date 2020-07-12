from tkinter import *

class Window:
    def __init__(self, width, height, title="MyWindow", resizable=(False, False), icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

    def run(self):
        self.root.mainloop()


if __name__ == "__maine__":
    window = Window(500, 500, "TKINTER")
    window.run()

"""
#create window
window = Tk()

#Set Title of window
window.title("TkinterExample")

#Set size window
window.geometry("500x300+200+300")

#resizable() method is used to allow Tkinter root window to change it’s size according
# to the users need as well we can prohibit resizing of the Tkinter window.
window.resizable(False, False)

#Set bitmap for the iconified widget to BITMAP. Return the bitmap if None is given.
window.iconbitmap("icoTK.ico")

window.mainloop()

"""