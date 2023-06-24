from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 18))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbol + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(text=password)    #to copy password into clipboard

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    mail = mail_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="please dont leave any field empty")

    else:

        is_ok = messagebox.askokcancel(title=website, message=f"These are details entered: \nEmail: {mail}"
                                       f"\nPassword: {password} \n is it ok to save?")

        if is_ok:
            with open("data.txt", "a") as f:
                f.write(f"{website} | {mail} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Password manager")
windows.config(padx= 20, pady=20)

web_label = Label(text="Website", fg="black")
web_label.grid(row=2, column=1)

user_label = Label(text="Email/Username", fg="black")
user_label.grid(row=3, column=1)

password_label= Label(text="Password", fg="black")
password_label.grid(row=4, column=1)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=2, column=2, columnspan=2)

mail_entry = Entry(width=35)
mail_entry.insert(0,"hisana6123@gmail.com")
mail_entry.grid(row=3, column=2, columnspan=2)

password_entry = Entry(width=20)
password_entry.grid(row=4, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=5, column=2, columnspan=2)

password_button = Button(text="generate password", command=generate_password)
password_button.grid(row=4, column=3, columnspan=2)


canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=1, column=2)

windows.mainloop()

