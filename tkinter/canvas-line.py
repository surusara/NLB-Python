import tkinter
top = tkinter.Tk()
C = tkinter.Canvas(top, bg="green", height=800, width=800)
line = C.create_line(0, 0, 100, 100, fill="red")
C.pack()
top.mainloop()
