# Import data from other files
from settings import *
from widgets import *

# Import needed libraries
import tkinter as tk
import customtkinter as ctk
from PIL import Image
import random

class StartFrame(ctk.CTkFrame):
    def __init__(self, master):
        # setup
        super().__init__(master = master, fg_color = COLOR)

        # variable
        global name_label_var, name_var, submit_button
        name_var = tk.StringVar(value = '')
        name_var.trace('w', self.update_label)
        name_label_var = tk.StringVar()
        
        # create widgets
        welcome_label = FirstLabel(self, text = WELCOME, font_size = FONT_SIZE)
        name_ask_label = FirstLabel(self, text = NAME_ASK, font_size = FONT_SIZE2)
        name_entry = FirstEntry(self, var = name_var, command = self.register(self.validate_input))
        submit_button = FirstButton(self, text = SUBMIT, func = self.submit)      
        
        # configure button
        submit_button.configure(state = 'disabled')
          
        # display widgets
        welcome_label.place(relx = 0.5, rely = 0.25, anchor = 'center',
                            relwidth = 1, relheight = 0.15)
        name_ask_label.place(relx = 0.5, rely = 0.5, anchor = 'center',
                             relwidth = 1, relheight = 0.1)
        name_entry.place(relx = 0.5, rely = 0.65, anchor = 'center',
                         relwidth = 0.6, relheight = 0.15)
        submit_button.place(relx = 0.5, rely = 0.85, anchor = 'center',
                            relwidth = 0.25, relheight = 0.1)
        
    # methods
    def update_label(self, *args):
        name_label_var.set(name_var.get().lower().capitalize())
        
    def submit(self):
        MenuFrame(self).place(relx = 0, rely = 0, 
                               relwidth = 1, relheight = 1)
        StartFrame(self).place_forget()
        
    def validate_input(self, text):
        if len(text) <= 10:
            if text.isalpha() or text == '':
                if len(text) >= 3:
                    submit_button.configure(state = 'normal')
                else:
                    submit_button.configure(state = 'disabled')
                return True
            else:
                return False
        else:
            return False
        
class MenuFrame(ctk.CTkFrame):
    def __init__(self, master):
        # setup
        super().__init__(master = master, fg_color = COLOR)
        
        # variables
        self.player_score_var = tk.IntVar(value = 0)
        self.computer_score_var = tk.IntVar(value = 0)
        self.timer_var = tk.IntVar(value = 3)
        
        # create widgets
        name_label = FirstLabel(self, text = name_label_var.get(), font_size = FONT_SIZE4)
        player_ico_label = ImageLabel(self)
        
        computer_label = FirstLabel(self, text = COMPUTER_NAME, font_size = FONT_SIZE4)
        computer_ico_label = ImageLabel(self)
        
        score_title_label = TitleLabel(self, text = SCORE)
        score_label = FirstLabel(self, text = '-', font_size = FONT_SIZE)
        player_score_label = ScoreLabel(self, var = self.player_score_var)
        computer_score_label = ScoreLabel(self, var = self.computer_score_var)
        
        self.timer_label = TimerLabel(self, var = self.timer_var)
        
        self.throw_button = FirstButton(self, text = 'Rzuć kostką', func = self.dice_throw)
        
        # images import
        # random player image
        x = random.randint(0, 0)
        player_ico = Image.open(f'img/player{x}.ico')
        player_ico = ctk.CTkImage(player_ico, size = (126, 126))
        
        # random computer image
        y = random.randint(0, 0)
        computer_ico = Image.open(f'img/computer{y}.ico')
        computer_ico = ctk.CTkImage(computer_ico, size = (126, 126))
        
        # label config
        player_ico_label.configure(image = player_ico)
        computer_ico_label.configure(image = computer_ico)
        
        # display widgets
        name_label.place(relx = 0, rely = 0.2,
                         relwidth = 0.2, relheight = 0.1)
        player_ico_label.place(relx = 0, rely = 0,
                               relwidth = 0.2, relheight = 0.2)
        
        computer_label.place(relx = 1, rely = 0.2, anchor = 'ne',
                             relwidth = 0.2, relheight = 0.1)
        computer_ico_label.place(relx = 1, rely = 0, anchor = 'ne',
                                 relwidth = 0.2, relheight = 0.2)
        
        score_title_label.place(relx = 0.5, rely = 0, anchor = 'n',
                          relwidth = 0.45, relheight = 0.11)
        score_label.place(relx = 0.5, rely = 0.11, anchor = 'n',
                          relwidth = 0.4, relheight = 0.1)
        player_score_label.place(relx = 0.38, rely = 0.11, anchor = 'n',
                               relwidth = 0.1, relheight = 0.1)
        computer_score_label.place(relx = 0.62, rely = 0.11, anchor = 'n',
                               relwidth = 0.1, relheight = 0.1)
        
        self.throw_button.place(relx = 0.5, rely = 0.9, anchor = 'center',
                           relwidth = 0.3, relheight = 0.1)
    
    # methods
    def dice_throw(self):
        self.throw_button.configure(state = 'disabled')
        self.timer_label.place(relx = 0.5, rely = 0.5, anchor = 'center')
        self.update()
        self.after(1000, self.timer_var.set(self.timer_var.get() - 1))
        self.update()
        self.after(1000, self.timer_var.set(self.timer_var.get() - 1))
        self.update()
        self.after(1000, self.throw_and_score)
        
    def throw_and_score(self):
        self.timer_label.place_forget()
        self.timer_var.set(3)
        
        player_throw = random.randint(1, 6)
        computer_throw = random.randint(1, 6)
        
        if player_throw < computer_throw:
            print('Player lose')
            self.computer_score_var.set(self.computer_score_var.get() + 1)
        elif player_throw == computer_throw:
            print('Tie')
        else:
            self.player_score_var.set(self.player_score_var.get() + 1)
            print('Player win')
        
        self.after(1000, self.throw_button.configure(state = 'normal'))