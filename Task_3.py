# This is a password generator that generates an 8 character password.It made with the Tkinter module.
# on clicking the generate password button a random password is generated in the empty field. This is password is saved to the clipboard
# with commands from pyperclip.
# reset button can be used to clear the password entry field.

import random
from tkinter import *
import pyperclip

# characters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!', '#', '$', '%', '&', '*', '+']
# print("Welcome to Password Generator!")
# print(logo)
# length=int(input("Enter the length of the password you would like to generate:"))
# chosen=[]
#
# for i in range(1,length+1):
#     chosen.append(random.choice(characters))
#
# random.shuffle(chosen)
#
# password=""
# for char in chosen:
#     password+=char
#
# print(f"Your password is {password}")
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pw_letters = [random.choice(letters) for _ in range(random.randint(8,16))]
    pw_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]
    pw_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]

    password_list=pw_letters+pw_numbers+pw_symbols
    random.shuffle(password_list)

    password="".join(password_list)
    password_entry.insert(0, f"{password[0:8]}")
    pyperclip.copy(password[0:8])




window=Tk()
window.title("Password Generator")
window.config(padx=50,pady=50,bg="white")

canvas=Canvas(width=200,height=200,highlightthickness=0,bg="white")
pic=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=pic)
canvas.grid(column=0,row=0,columnspan=2)

title_label=Label(text="Welcome to password Generator!",bg="white",font=("Courier",18))
title_label.grid(column=0,row=1,columnspan=3)

generate_button=Button(text="Generate Password",command=password_generator)
generate_button.grid(column=0,row=2)

password_entry=Entry(width=25)
password_entry.grid(column=1,row=2)

reset_Button=Button(text="Reset",bg="white",width=14,command=lambda:password_entry.delete(0,"end"))
reset_Button.grid(column=0,row=3)


window.mainloop()
