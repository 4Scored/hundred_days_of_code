from tkinter import *

window = Tk()
window.title("Mi -> Km CONVERTER")
window.config(padx=25, pady=25)

def convert():
    mi = float(input_mi.get())
    km_res.config(text=f"{mi*1.609}")

input_mi = Entry(width=5)
input_mi.grid(column=1,row=0)
label_mi = Label(text="Miles")
label_mi.grid(column=2,row=0)

eq_to = Label(text="is equal to")
eq_to.grid(column=0,row=1)
km_res = Label(text="0")
km_res.grid(column=1,row=1)
label_km = Label(text="Km")
label_km.grid(column=2,row=1)

button = Button(text="Calculate", command=convert)
button.grid(column=1,row=2)

window.mainloop()