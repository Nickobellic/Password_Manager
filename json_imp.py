from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    # Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list = [random.choice(symbols)+char for char in password_list]
    password_list = [random.choice(numbers)+char for char in password_list]

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    new_data = {
        website.get(): {
                'Email':email.get(),
                'Password': password.get()
                }
            }
    if website.get() is None or password.get() is None:
        messagebox.askretrycancel(title='Empty Fields', message='Don\'t Leave any empty fields.')

    else:
        try:
            with open('passwords.json','r') as file:
                data = json.load(file)
                data.update(new_data)
            with open('passwords.json','w') as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            with open('passwords.json','w') as file:
                json.dump(new_data, file, indent=4)
        website_entry.delete(0,END)
        password_entry.delete(0,END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    try:
        with open('passwords.json', 'r') as file:
            data = json.load(file)
            websites = [i.title() for i in data.keys()]
            website_search = website.get().title()
            if website_search in websites:
                messagebox.showinfo(title=website_search, message=f" Here\'s the Details \n Email: {data[website_search]['Email']} \n Password: {data[website_search]['Password']}")
            else:
                messagebox.showinfo(title='Not Found', message=f"We can\'t able to find Password for {website_search}")
                website_entry.delete(0,END)
    except FileNotFoundError:
        messagebox.showinfo(title='File not Found',message='File of Passwords is not found.')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50)
window.title('Password Manager')

# Variables which stores the entered elements
website = StringVar()
password = StringVar()
email = StringVar()

# Frontend Creation
img_obj = Canvas(height=200, width=200)
img = PhotoImage(file='logo.png')
img_obj.create_image(100, 100, image=img, anchor=CENTER)
img_obj.grid(row=0 ,column=1)
website_label = Label(text='Website:')
website_label.grid(row=1 ,column=0)

website_entry = Entry(width=35, textvariable=website)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

search_button = Button(text='Search', width=15, command=search)
search_button.grid(row=1, column=3, columnspan=1)

email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)

email_entry = Entry(width=35, textvariable=email)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0,'avrahulkanna17@gmail.com')

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

password_entry = Entry(width=21, textvariable=password)
password_entry.grid(row=3, column=1)

generate_button = Button(text='Generate Password', command=generate)
generate_button.grid(row=3, column=3)

add_button = Button(text='Add', width=36, command=add)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
