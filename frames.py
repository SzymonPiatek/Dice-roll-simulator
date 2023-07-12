# Import data from other files
from settings import *
from widgets import *

# Import needed libraries
import tkinter as tk
import customtkinter as ctk

class StartFrame(ctk.CTkFrame):
    def __init__(self, master):
        # setup
        super().__init__(master = master, fg_color = COLOR)

        # variable
        global name_label_var, name_var
        name_var = tk.StringVar(value = '')
        name_var.trace('w', self.update_label)
        name_label_var = tk.StringVar()
        
        # create widgets
        welcome_label = FirstLabel(self, text = WELCOME, font_size = FONT_SIZE)
        name_ask_label = FirstLabel(self, text = NAME_ASK, font_size = FONT_SIZE2)
        name_entry = FirstEntry(self, var = name_var)
        submit_button = FirstButton(self, text = SUBMIT, func = self.submit)
        # test = SecondLabel(self, textvariable = name_label_var, fg_color = COLOR, text_color = TEXT_COLOR3, font_size = FONT_SIZE2)
        
        # display widgets
        welcome_label.place(relx = 0.5, rely = 0.25, anchor = 'center',
                            relwidth = 1, relheight = 0.15)
        name_ask_label.place(relx = 0.5, rely = 0.5, anchor = 'center',
                             relwidth = 1, relheight = 0.1)
        name_entry.place(relx = 0.5, rely = 0.65, anchor = 'center',
                         relwidth = 0.5, relheight = 0.15)
        submit_button.place(relx = 0.5, rely = 0.85, anchor = 'center',
                            relwidth = 0.25, relheight = 0.1)
        # test.place(relx = 0.5, rely = 0.8)
        
    # methods
    def update_label(self, *args):
        name_label_var.set(name_var.get().lower().capitalize())
        name = name_label_var.get()
        
    def submit(self):
        pass
    