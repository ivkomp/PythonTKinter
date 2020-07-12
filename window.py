from tkinter import *

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