from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
import smtplib
my_addr = "benw.python.test@gmail.com"
my_passw = "Resco123!"



# ---------------------------- Find Password ------------------------- #
def search_passw():


    web = web_input.get()
    try:
        with open("data.json", "r") as data_file:
            #Reading Old Data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File found.")
    else:
        if web in data:
            user_input.delete(0, END)
            pass_input.delete(0, END)
            email = data[web]["email"]
            passw = data[web]["password"]
            pass_input.insert(0, passw)
            user_input.insert(0, email)
            messagebox.showinfo(title=web, message=f"Website: {web} \n Email: {email} \n Password: {passw}")

        else:
            messagebox.showerror(title="Error", message=f"No details for {web} found.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    #Password Generator Project
    pass_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)    

    password = "".join(password_list)
    pass_input.insert(0, f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def data():
    global my_addr
    global my_passw
    global connection
    web = web_input.get()
    user = user_input.get()
    passw = pass_input.get()
    new_data = {
        web: {
            "email": user,
            "password": passw,
        }
    }
     
    if len(web) == 0 or len(user) == 0 or len(passw) ==0:
        messagebox.showwarning(title="Error", message="You can not leave boxes empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #Reading Old Data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
        
            with open("data.json", "w") as data_file:
                #Saving update data
                json.dump(data, data_file, indent=4)
            
        finally:
            web_input.delete(0, END)
            pass_input.delete(0, END)
            with smtplib.SMTP(host="smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_addr, password=my_passw)
                connection.sendmail(from_addr=my_addr, to_addrs="benw.pythontest@yahoo.com", msg=f"Subject:{web}. \n\n Email: {user} \n Password: {passw}")
            


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
background = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=background)
canvas.grid(column=1, row=0)

#website input:
web_input = Entry(width=20)
web_input.grid(column=1, row=1, sticky=W)
web_input.focus()
web_label = Label(text="Website: ")
web_label.grid(column=0, row=1)

#User input area:
user_input = Entry(width=30)
user_input.grid(column=1, row=2, columnspan=2, sticky=W)
user_input.insert(END, "Benrwalker@icloud.com")
user_label = Label(text="Email/Username: ")
user_label.grid(column=0, row=2)

#Password input and generate button
pass_input = Entry(width=20)
pass_input.grid(column=1, row=3, sticky=W)
pass_label = Label(text="Password: ")
pass_label.grid(column=0, row=3)
gen_pass = Button(text="Generate Password", command=generate)
gen_pass.grid(column=2, row=3, sticky=W)

#Add button
add = Button(text= "Add", width=36, command=data)
add.grid(column=1, row=4, columnspan=2, sticky=W)

#Search button
search = Button(text="Search", width=13, command=search_passw)
search.grid(column=2, row=1, sticky=W)

window.mainloop()