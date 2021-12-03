from tkinter import *
from tkinter import ttk
import tkinter

root = Tk()
frm = ttk.Frame(root,padding=10)
frm.grid()
ttk.Label(frm, text="CALCULADORA").grid(column=0, row=0, columnspan=3)


ttk.Button(frm, text="9").grid(column=2, row=3)
ttk.Button(frm, text="8").grid(column=1, row=3)
ttk.Button(frm, text="7").grid(column=0, row=3)

ttk.Button(frm, text="6").grid(column=2, row=4)
ttk.Button(frm, text="5").grid(column=1, row=4)
ttk.Button(frm, text="4").grid(column=0, row=4)

ttk.Button(frm, text="3").grid(column=2, row=5)
ttk.Button(frm, text="2").grid(column=1, row=5)
ttk.Button(frm, text="1").grid(column=0, row=5)


ttk.Button(frm, text="0").grid(column=1, row=6)
ttk.Button(frm, text=".").grid(column=2, row=6)
ttk.Button(frm, text="-").grid(column=0, row=6)
ttk.Button(frm, text="=").grid(column=3, row=6)


ttk.Button(frm, text="/").grid(column=3, row=2)
ttk.Button(frm, text="x").grid(column=3, row=3)
ttk.Button(frm, text="-").grid(column=3, row=4)
ttk.Button(frm, text="+").grid(column=3, row=5)

#frm, text="+", command=

root.mainloop()