# tkinter basics

from tkinter import *

window = Tk()
window.title("GUI Window")
window.minsize(500, 300)
window.config(padx=20, pady=50) # padding

# labels
label = Label(text="I'm a label", font=("Arial", 24, "bold"))
label.grid(column=0, row=0) # can use .pack(), .place(x=__, y=__), or .grid(column=__, row=__) for specificity
label["text"] = "A modified label!" # or my_label.config(text="A modified label!")

# button
def button_clicked():
    print("I got clicked.")
    new_text = input.get()
    label["text"] = new_text

button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

button2 = Button(text="Click me", command=button_clicked)
button2.grid(column=2, row=1)

# entry (input)
input = Entry(width=12)
input.grid(column=2, row=2)

# other widgets: text (multiline entry), spinbox, scale, checkbutton, radiobutton, listbox
# can't mix grid() and pack(), choose one or the other

window.mainloop()
