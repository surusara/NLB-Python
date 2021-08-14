import tkinter

top = tkinter.Tk()

C = tkinter.Canvas(top, bg="green", height=800, width=800)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")

C.pack()
top.mainloop()
