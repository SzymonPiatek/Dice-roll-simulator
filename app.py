# Import data from other files
from settings import *
from widgets import *
from frames import *

# Import needed libraries
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox

# Create an application class
class App(ctk.CTk):
    def __init__(self):
        # setup
        super().__init__(fg_color = COLOR)
        
        # center window variables
        window_width = self.winfo_screenwidth()
        window_height = self.winfo_screenheight()
        center_width = int(round(window_width / 2 - int(APP_SIZE[0])/2, 0))
        center_height = int(round(window_height / 2 - int(APP_SIZE[1])/2, 0))
        
        # window setup
        self.geometry(f'{APP_SIZE[0]}x{APP_SIZE[1]}+{center_width}+{center_height}')
        self.resizable(False, False)
        self.title(f'{APP_TITLE}')        
        
        # create widgets
        version_label = VersionLabel(self, text = VERSION)
        
        # display widgets
        version_label.place(relx = 0.005, rely = 1, anchor = 'sw')
        
        # frame setup
        StartFrame(self).place(relx = 0.5, rely = 0.5, anchor = 'center', 
                               relwidth = 0.94, relheight = 0.91)
    
        # binds
        # self.bind('<F11>', self.toggle_fullscreen)
        self.bind('<Escape>', self.quit_question)
        
        # run
        self.mainloop()
        
    # methods
    def toggle_fullscreen(self, event = None):
        self.state = not self.state
        if self.state:
            self.attributes('-fullscreen', False)
        elif self.state == False:
            self.attributes('-fullscreen', True)
    
    def quit_question(self, event):
        if event.keysym == 'Escape':
            result = messagebox.askquestion('', EXIT)
            if result == 'yes':
                self.destroy()
   
if __name__ == '__main__':
    App()