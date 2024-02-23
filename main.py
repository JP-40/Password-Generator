#Libaries
import string
import random
import subprocess
import tkinter as tk
from tkinter import ttk

#Function
def PasswordGenerationFunction():
    from random import sample, choice 
    print(letters.get(), 'ch1')
    print(numbers.get(), 'ch2')
    print(specialCharacters.get(), 'ch3')
    
    if letters.get() == 1 and numbers.get() == 0 and specialCharacters.get() == 0:
        characters = string.ascii_letters
        output_string.set('Copied to clipboard')
        print('opt 1')
    elif letters.get() == 1 and numbers.get() == 1 and specialCharacters.get() == 0:
        characters = string.ascii_letters + string.digits
        output_string.set('Copied to clipboard')
        print('opt 2')
    elif letters.get() == 1 and numbers.get() == 1 and specialCharacters.get() == 1:
        characters = string.ascii_letters + string.punctuation + string.digits
        output_string.set('Copied to clipboard')
        print('opt 3')
    elif letters.get() == 0 and numbers.get() == 1 and specialCharacters.get() == 1:
        characters = string.digits + string.punctuation
        output_string.set('Copied to clipboard')
        print('opt 4')
    elif letters.get() == 0 and numbers.get() == 0 and specialCharacters.get() == 1:
        characters = string.punctuation
        output_string.set('Copied to clipboard')
        print('opt 5')
    elif letters.get() == 1 and numbers.get() == 0 and specialCharacters.get() == 1:
        characters = string.punctuation + string.ascii_letters
        output_string.set('Copied to clipboard')
        print('opt 6')
    elif letters.get() == 0 and numbers.get() == 1 and specialCharacters.get() == 0:
        characters = string.digits
        print('opt 7')
    else:
        print('no boxes selected')
        output_string.set('No password for you')
    
    password = ''.join(choice(characters) for i in range (input_Int.get()))
    subprocess.run("clip", text=True, input=password)

#GUI

#window
window = tk.Tk()
window.title('Password Generator made by JP-40')
window.geometry('450x250')


#Title
title_label = ttk.Label(master = window , text = 'Password Generator' , font = 'Calibri 24 bold')
title_label.pack()

#input field
input_box = ttk.Frame(master = window)
input_Int = tk.IntVar()
entry = ttk.Entry(master = input_box, textvariable = input_Int)
button = ttk.Button(master = input_box , text = 'Generate', command = PasswordGenerationFunction)
entry.pack(side = 'left' , padx = 15 )
button.pack(side ='left')
input_box.pack(pady = 10)

#Check boxes
letters = tk.IntVar()
numbers = tk.IntVar()
specialCharacters = tk.IntVar()
check_box_output_label = ttk.Label(master = window, text = 'Tick to add to password')
check_box_output_label.pack()

check_box1 = ttk.Checkbutton(master = window, text = 'Letters', variable=letters)
check_box1.pack()
check_box2 = ttk.Checkbutton(master = window, text = 'Numbers', variable=numbers)
check_box2.pack()
check_box3 = ttk.Checkbutton(master = window, text = 'Special Characters', variable=specialCharacters)
check_box3.pack()

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output' , font = 'Calibri 24', textvariable= output_string)
output_label.pack(pady = 10)

#Run 
window.mainloop()