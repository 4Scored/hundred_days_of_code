from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def gen_password():
    pass_letters = [choice(letters) for _ in range(randint(8, 10))] 
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))] 
    pass_numbers = [choice(numbers) for _ in range(randint(2, 4))] 
    pass_list = pass_letters + pass_symbols + pass_numbers
    shuffle(pass_list)

    password = "".join(pass_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email_user = email_user_entry.get()
    password = password_entry.get()
    # is_ok = False
    new_data = {
        website: {
            "email": email_user,
            "password": password,
        }
    }

    if website == "" or password == "":
        messagebox.showinfo(title="Empty Entries...", message="Please don't leave any fields empty!")
    else:        
        try:
            with open("data.json", "r") as df:        
                data = json.load(df) # reading old data
                data.update(new_data) # updating old data with new_data
        except FileNotFoundError:
            with open("data.json", "w") as df:
                json.dump(new_data, df, indent=4)
        else:
            data.update(new_data)            
            with open("data.json", "w") as df:
                json.dump(data, df, indent=4) # writing, saving updated data                
                # json.load(df) # reading, serializess data and loads them into a dict
        finally:
                # is_ok = messagebox.askokcancel(title=website, message=f"Details entered --\nEmail: {email_user}\nPassword:{password}\nIs this okay to save?")
                # if is_ok:
                # df.write(f"{website} | {email_user} | {password}\n")
                website_entry.delete(0, END)
                # email_user_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as df:
            data = json.load(df)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="No details for searched website.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=18)
website_entry.grid(column=1, row=1)
website_entry.focus() # cursor on launch
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)

email_user_label = Label(text="Email/Username:")
email_user_label.grid(column=0, row=2)
email_user_entry = Entry(width=35)
email_user_entry.grid(column=1, row=2, columnspan=2)
email_user_entry.insert(0, "abcdefg@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)
password_button = Button(text="Generate Password", command=gen_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
