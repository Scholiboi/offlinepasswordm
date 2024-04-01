from tkinter import *
from tkinter import messagebox
from passwordgenerator import generate_password
import pyperclip
import json


# ---------------------------- SHOW PASSWORD ------------------------------- #
def show_password():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "No Data Stored")
    else:
        website = entry_website.get()
        if website == '':
            messagebox.showerror('Error', 'Please enter Website field')
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                pyperclip.copy(password)
                messagebox.showinfo(website, f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showerror("Error", f"No details for the {website} exists.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def new_password():
    entry_password.delete(0, END)
    password = generate_password()
    entry_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    website = entry_website.get()
    email_username = entry_username.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password
        }
    }
    if website == '':
        messagebox.showerror('Error', 'Please enter Website field')
    elif email_username == '':
        messagebox.showerror('Error', 'Please enter Email/Username field')
    elif password == '':
        messagebox.showerror('Error', 'Please enter Password field')
    else:
        confirm = messagebox.askokcancel("Information",
                                         f"Website: {website}\nEmail/Username: {email_username}\nPassword: "
                                         f"{password}\nDo you want to continue?")
        if confirm:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                pyperclip.copy(password)
                entry_website.delete(0, END)
                entry_username.delete(0, END)
                entry_password.delete(0, END)
                entry_website.focus()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
# window.geometry("240x240")
window.config(padx=50, pady=50)

# label1 = Label(window)
# label1.grid(row=0, column=0)

# label2 = Label(window, text="Website:", font=("Arial", 9 ,"normal"), width=10)
label2 = Label(window, text="Website:")
label2.grid(row=1, column=0)

# label3 = Label(window, text="Email/Username:", width=15)
label3 = Label(window, text="Email/Username:")
label3.grid(row=2, column=0)

# label4 = Label(window, text="Password:", width=10)
label4 = Label(window, text="Password:")
label4.grid(row=3, column=0)

canvas = Canvas(window, width=200, height=200)
password_lock_img = PhotoImage(file="C:/Users/SY/OneDrive/VSC Files Python/pycharm projects/passwordmanager/logo.png")
canvas.create_image(100, 100, image=password_lock_img)
canvas.grid(row=0, column=1)

entry_website = Entry(window, width=33)
entry_website.grid(row=1, column=1)
entry_website.focus()  # new

button_add_show = Button(window, text="Search", width=14, command=show_password)
button_add_show.grid(row=1, column=2)

entry_username = Entry(window, width=51)
entry_username.grid(row=2, column=1, columnspan=2)

entry_password = Entry(window, width=33)
entry_password.grid(row=3, column=1)

button_gen_password = Button(window, text="Generate Password", width=14, command=new_password)
button_gen_password.grid(row=3, column=2)

button_add_password = Button(window, text="Add", width=43, command=add_password)
button_add_password.grid(row=4, column=1, columnspan=2)



window.mainloop()
