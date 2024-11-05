import random
import string
from tkinter import *
from tkinter import messagebox
import pyperclip

def generate():
    # Get the character types
    uppercase = uppercase_var.get()
    lowercase = lowercase_var.get()
    numbers = numbers_var.get()
    symbols = symbols_var.get()

    # Create the character set based on user selection
    character_set = ''
    if uppercase:
        character_set += string.ascii_uppercase
    if lowercase:
        
        character_set += string.ascii_lowercase
    if numbers:
        character_set += string.digits
    if symbols:
        character_set += string.punctuation

    # Check if at least one character type is selected
    if not character_set:
        messagebox.showerror("Error", "At least one character type must be selected")
        return

    password_length = int(length_box.get())
    
    # Ensure password_length is not greater than character_set length
    if password_length > len(character_set):
        messagebox.showerror("Error", "Password length cannot be greater than the number of available characters.")
        return

    password = ''.join(random.choices(character_set, k=password_length))  # Use random.choices for repetition
    password_field.delete(0, END)
    password_field.insert(0, password)

def copy():
    random_password = password_field.get()
    pyperclip.copy(random_password)

root = Tk()
root.config(bg='grey20')

# Define character type variables
uppercase_var = IntVar()
lowercase_var = IntVar()
numbers_var = IntVar()
symbols_var = IntVar()

font = ('arial', 13, 'bold')

# Password Label
password_label = Label(root, text='Password Generator', font=('times new roman', 20, 'bold'), bg='grey20', fg="white")
password_label.grid()

# Password Length Label
length_label = Label(root, text='Password Length (min 8):', font=font, bg='grey20', fg='white')
length_label.grid(pady=10)

# Length Spinbox
length_box = Spinbox(root, from_=8, to=23, width=10, font=font)
length_box.grid(pady=8)

# character Type Label
characterLabel=Label(root,text='Character Type',font=font,bg='grey20',fg='white')
characterLabel.grid(pady=8)

# Character Type Checkboxes
uppercase_checkbox = Checkbutton(root, text='Uppercase Letters', variable=uppercase_var, font=font, bg='grey20', fg='white')
uppercase_checkbox.grid(pady=7)

lowercase_checkbox = Checkbutton(root, text='Lowercase Letters', variable=lowercase_var, font=font, bg='grey20', fg='white')
lowercase_checkbox.grid(pady=7)

numbers_checkbox = Checkbutton(root, text='Numbers', variable=numbers_var, font=font, bg='grey20', fg='white')
numbers_checkbox.grid(pady=7)

symbols_checkbox = Checkbutton(root, text='Symbols', variable=symbols_var, font=font, bg='grey20', fg='white')
symbols_checkbox.grid(pady=7)

# Generate Button
generate_button = Button(root, text="Generate Password", font=font, command=generate)
generate_button.grid(pady=10)

# Password Field
password_field = Entry(root, width=25, bd=10, font=font)
password_field.grid(pady=7)

# Copy Button
copy_button = Button(root, text='Copy', font=font, command=copy)
copy_button.grid()

root.mainloop()
