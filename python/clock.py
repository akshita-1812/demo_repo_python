from tkinter import *
import time
screen = Tk()
def timing ():
   c_t=time.strftime("%H : %M : %S :%p")
   lbl2.config(text=c_t)
   lbl2.after(1000,timing)
lbl=Label(screen,text="Digital clock",font="arial 30 bold")
lbl.pack()

lbl2=Label(screen,font="arial 30 bold")
lbl2.pack()
timing()
mainloop()

# import time
# print(time.strftime("%H : %M : %S :%p"))