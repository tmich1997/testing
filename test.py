import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

# function

def convert():
    mile_input = entry_int.get()
    km_output = mile_input * 1.61
    output_string.set(f'{km_output} km/h')

# main window
window = ttk.Window(themename= 'journal')

# title for the window
window.title('Demo')

# setting the size of the window
window.geometry('300x150')

# title_label
title_label = ttk.Label(master = window, text = 'Miles to Kilometers', font = 'Calibri 18 bold')
title_label.pack()

# input field (another widget)
input_frame = ttk.Frame(master= window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text='Convert', command=convert)

entry.pack(side = 'left', padx= 10)
button.pack(side= 'left')
input_frame.pack(pady= 10)

# output_label
output_string = tk.StringVar()
output_label = ttk.Label(master= window, text= 'Output', font= 'Calibri 18', textvariable=output_string)
output_label.pack(pady= 5)

# the main loop
# this has to be called for the main program
window.mainloop()