# Import data from other files
from settings import *
from widgets import *

# Import needed libraries
import tkinter as tk
import customtkinter as ctk
from PIL import Image
import random

class Player():
    def __init__(self, health):
        self.health = health
    
    def attack(self, damage):
        self.player_attack = damage
    
    def damage(self, damage):
        self.health = self.health - damage
        return self.health

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
        self.who_win_var = tk.StringVar()
        
        # players
        self.player = Player(HEALTH)
        self.computer = Player(HEALTH)
        
        # images import
        # random player image
        x = random.randint(0, 0)
        player_ico = Image.open(f'img/avatars/player/player{x}.ico')
        player_ico = ctk.CTkImage(player_ico, size = (126, 126))
        
        # random computer image
        y = random.choice(COMPUTER_NAME_SOURCE)
        y_index = COMPUTER_NAME_SOURCE.index(y)
        
        computer_ico = Image.open(f'img/avatars/computer/{y}.ico')
        computer_ico = ctk.CTkImage(computer_ico, size = (126, 126))
        
        # create widgets
        name_label = FirstLabel(self, text = name_label_var.get(), font_size = FONT_SIZE4)
        player_ico_label = ImageLabel(self)
        self.player_health_bar = HealthBar(self, max = HEALTH)
        self.player_health_label = FirstLabel(self, text = f'{self.player.health} / {HEALTH}', font_size = FONT_SIZE2)
        computer_label = FirstLabel(self, text = COMPUTER_NAME[y_index], font_size = FONT_SIZE4)
        computer_ico_label = ImageLabel(self)
        self.computer_health_bar = HealthBar(self, max = HEALTH)
        self.computer_health_label = FirstLabel(self, text = f'{self.computer.health} / {HEALTH}', font_size = FONT_SIZE2)
        
        score_title_label = TitleLabel(self, text = SCORE)
        score_label = FirstLabel(self, text = '-', font_size = FONT_SIZE)
        player_score_label = ScoreLabel(self, var = self.player_score_var, font_size = FONT_SIZE)
        computer_score_label = ScoreLabel(self, var = self.computer_score_var, font_size = FONT_SIZE)
        
        self.timer_label = ScoreLabel(self, var = self.timer_var, font_size = FONT_SIZE5)
        self.throw_button = FirstButton(self, text = 'Rzuć kostką', func = self.dice_throw)
        self.who_win_label = ScoreLabel(self, var = self.who_win_var, font_size = FONT_SIZE)
        
        # label config
        player_ico_label.configure(image = player_ico)
        computer_ico_label.configure(image = computer_ico)
        self.player_health_bar.configure(value = self.player.health)
        self.computer_health_bar.configure(value = self.computer.health)
        
        # display widgets
        name_label.place(relx = 0, rely = 0.2,
                         relwidth = 0.2, relheight = 0.1)
        player_ico_label.place(relx = 0, rely = 0,
                               relwidth = 0.2, relheight = 0.2)
        self.player_health_bar.place(relx = 0, rely = 0.3,
                                relwidth = 0.2, relheight = 0.05)
        self.player_health_label.place(relx = 0, rely = 0.35,
                                       relwidth = 0.2, relheight = 0.05)
        computer_label.place(relx = 1, rely = 0.2, anchor = 'ne',
                             relwidth = 0.2, relheight = 0.1)
        computer_ico_label.place(relx = 1, rely = 0, anchor = 'ne',
                                 relwidth = 0.2, relheight = 0.2)
        self.computer_health_bar.place(relx = 1, rely = 0.3, anchor = 'ne',
                                  relwidth = 0.2, relheight = 0.05)
        self.computer_health_label.place(relx = 1, rely = 0.35, anchor = 'ne',
                                         relwidth = 0.2, relheight = 0.05)
        
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
        # 3
        self.after(1000, self.timer_var.set(self.timer_var.get() - 1))
        self.update()
        # 2
        self.after(1000, self.timer_var.set(self.timer_var.get() - 1))
        self.update()
        # 1
        self.after(1000, self.throw_and_score)
        
    def throw_and_score(self):
        self.timer_label.place_forget()
        self.timer_var.set(3)
        
        self.player_throw = random.randint(1, 6)
        self.computer_throw = random.randint(1, 6)
        
        if self.player_throw < self.computer_throw:
            self.update()
            self.who_win_var.set('Wygrał przeciwnik!')
            self.who_win_label.place(relx = 0.5, rely = 0.5, anchor = 'center')
            self.update()
            self.computer_win()
            self.computer_score_var.set(self.computer_score_var.get() + 1)
            self.after(1000, self.who_win_label.place_forget())
            self.after(0, self.throw_button.configure(state = 'normal'))
            
        elif self.player_throw == self.computer_throw:
            self.update()
            self.who_win_var.set('Remis!')
            self.who_win_label.place(relx = 0.5, rely = 0.5, anchor = 'center')
            self.update()
            self.after(1000, self.who_win_label.place_forget())
            self.after(0, self.throw_button.configure(state = 'normal'))
            
        else:
            self.update()
            self.who_win_var.set('Wygrałeś!')
            self.who_win_label.place(relx = 0.5, rely = 0.5, anchor = 'center')
            self.update()
            self.player_win()
            self.player_score_var.set(self.player_score_var.get() + 1)
            self.after(1000, self.who_win_label.place_forget())
            self.after(0, self.throw_button.configure(state = 'normal'))
            
    def player_win(self):
        damage = self.player_throw - self.computer_throw
        self.player.attack(damage)
        self.health = self.computer.damage(damage)
        self.computer_health_bar.configure(value = self.health)
        self.computer_health_label.configure(text = f'{self.health} / {HEALTH}')
        self.update()
        
    def computer_win(self):
        damage = self.computer_throw - self.player_throw
        self.computer.attack(damage)
        self.health = self.player.damage(damage)
        self.player_health_bar.configure(value = self.health)
        self.player_health_label.configure(text = f'{self.health} / {HEALTH}')
        self.update()
        