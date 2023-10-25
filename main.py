from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
FONT = ("Arial", 13, "normal")
password_str = ""

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def creating_random_string():
    global password_str
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    amount_of_letters = randint(8, 10)
    amount_of_numbers = randint(2, 4)
    amount_of_symbols = randint(2, 4)
    password_list = [choice(letters) for char in range(amount_of_letters)] + \
                    [choice(numbers) for num in range(amount_of_numbers)] + \
                    [choice(symbols) for sym in range(amount_of_symbols)]
    shuffle(password_list)
    password_str = "".join(password_list)
def generate_password():
    creating_random_string()
    password_entry.delete(0, END)
    new_password = password_str
    password_entry.insert(END, new_password)
    pyperclip.copy(new_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def saving_password():
    link = website_entry.get()
    email_or_username = email_or_username_entry.get()
    password = password_entry.get()
    if link == "" or email_or_username == "" or password == "":
        warning_box = messagebox.showinfo(title="Warning!", message="Please don't leave any empty fields.")
    else:
        question_box = messagebox.askyesno(title="Are you sure about that??",
                                               message="Are you happy with the information?")
        if question_box:
            confirmation_box = messagebox.showinfo(title="Popup.exe", message="Your password has been saved.")
            with open("passwords.txt", "a") as doc:
                doc.write(f"{link} | {email_or_username} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

        else:
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:", font=FONT)
label_website.grid(row=1, column=0)
label_username_or_email = Label(text="Email/Username:", font=FONT)
label_username_or_email.grid(row=2, column=0)
label_password = Label(text="Password:", font=FONT)
label_password.grid(row=3, column=0)

website_entry = Entry(font=FONT)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky="NSEW")

email_or_username_entry = Entry(font=FONT)
email_or_username_entry.insert(END, "klaidas.miller@gmail.com")
email_or_username_entry.grid(row=2, column=1, columnspan=2, sticky="NSEW")

password_entry = Entry(font=FONT)
password_entry.grid(row=3, column=1, columnspan=1, sticky="NSEW")

generate_password_button = Button(text="Generate Password", font=FONT, command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="NSEW")

add_to_notes_button = Button(text="Add to notes", font=FONT, command=saving_password)
add_to_notes_button.grid(row=4, column=1, columnspan=2, sticky="NSEW")





window.mainloop()




