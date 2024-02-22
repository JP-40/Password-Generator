#Libaries
import string
import random
import subprocess
import tkinter as tk
from tkinter import ttk

#Function
def PasswordGenerationFunction():
    from random import sample, choice
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(choice(characters) for i in range (input_Int.get()))
    subprocess.run("clip", text=True, input=password)
    output_string.set('Copied to clipboard')
    output_string2.set(password)


#GUI

#window
window = tk.Tk()
window.title('Password Generator made by JP-40')
window.geometry('450x250')
window.config(bg='grey')

#Title
title_label = ttk.Label(master = window , text = 'Password Generator' , font = 'Calibri 24 bold', background ='grey')
title_label.pack()

#input field
input_box = ttk.Frame(master =window)
input_Int = tk.IntVar()
entry = ttk.Entry(master = input_box, textvariable = input_Int)
button = ttk.Button(master = input_box , text = 'Generate', command = PasswordGenerationFunction)
entry.pack(side = 'left' , padx = 15)
button.pack(side ='left')
input_box.pack(pady = 10)

#Output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'Output' , font = 'Calibri 24', textvariable= output_string)
output_label.pack(pady = 10)

output_string2 = tk.StringVar()
output_label2 = ttk.Label(master = window, text = 'Output' ,  font = 'Calibri 24', textvariable= output_string2)
output_label2.pack(pady = 10)

#Run 
window.mainloop()