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
        global name_label_var, name_var, submit_button, avatar_choice_var 
        global avatar_button, avatar_button2, avatar_button3, avatar_button4
        name_var = tk.StringVar(value = '')
        name_var.trace('w', self.update_label)
        name_label_var = tk.StringVar()
        avatar_choice_var = tk.IntVar(value = 0)
        
        # create widgets
        choice_label = FirstLabel(self, text = WELCOME, font_size = FONT_SIZE)
        avatar_label = ImageLabel(self)
        avatar2_label = ImageLabel(self)
        avatar3_label = ImageLabel(self)
        avatar4_label = ImageLabel(self)
        name_ask_label = FirstLabel(self, text = NAME_ASK, font_size = FONT_SIZE2)
        name_entry = FirstEntry(self, var = name_var, command = self.register(self.validate_input))
        submit_button = FirstButton(self, text = SUBMIT, func = self.submit)      
        avatar_button = FirstButton(self, text = CHOOSE[0], func = lambda: self.avatar_choice(1, text = name_label_var.get()))
        avatar_button2 = FirstButton(self, text = CHOOSE[1], func = lambda: self.avatar_choice(2, text = name_label_var.get()))
        avatar_button3 = FirstButton(self, text = CHOOSE[2], func = lambda: self.avatar_choice(3, text = name_label_var.get()))
        avatar_button4 = FirstButton(self, text = CHOOSE[3], func = lambda: self.avatar_choice(4, text = name_label_var.get()))
        
        # images import
        player_ico = Image.open('img/avatars/player/player1.ico')
        player_ico = ctk.CTkImage(player_ico, size = (126, 126))
        
        player_ico2 = Image.open('img/avatars/player/player2.ico')
        player_ico2 = ctk.CTkImage(player_ico2, size = (126, 126))
        
        player_ico3 = Image.open('img/avatars/player/player3.ico')
        player_ico3 = ctk.CTkImage(player_ico3, size = (126, 126))
        
        player_ico4 = Image.open('img/avatars/player/player4.ico')
        player_ico4 = ctk.CTkImage(player_ico4, size = (126, 126))
        
        # label configure
        avatar_label.configure(image = player_ico)
        avatar2_label.configure(image = player_ico2)
        avatar3_label.configure(image = player_ico3)
        avatar4_label.configure(image = player_ico4)
        
        # configure button
        submit_button.configure(state = 'disabled')
          
        # display widgets
        choice_label.place(relx = 0.5, rely = 0.1, anchor = 'center',
                            relwidth = 1, relheight = 0.15)
        avatar_label.place(relx = 0.14, rely = 0.35, anchor = 'center',
                           relwidth = 0.2, relheight = 0.2)
        avatar2_label.place(relx = 0.38, rely = 0.35, anchor = 'center',
                           relwidth = 0.2, relheight = 0.2)
        avatar3_label.place(relx = 0.62, rely = 0.35, anchor = 'center',
                           relwidth = 0.2, relheight = 0.2)
        avatar4_label.place(relx = 0.86, rely = 0.35, anchor = 'center',
                           relwidth = 0.2, relheight = 0.2)
        name_ask_label.place(relx = 0.5, rely = 0.57, anchor = 'center',
                             relwidth = 1, relheight = 0.1)
        name_entry.place(relx = 0.5, rely = 0.7, anchor = 'center',
                         relwidth = 0.6, relheight = 0.15)
        submit_button.place(relx = 0.5, rely = 0.9, anchor = 'center',
                            relwidth = 0.25, relheight = 0.1)
        avatar_button.place(relx = 0.14, rely = 0.5, anchor = 'center',
                            relwidth = 0.2, relheight = 0.07)
        avatar_button2.place(relx = 0.38, rely = 0.5, anchor = 'center',
                            relwidth = 0.2, relheight = 0.07)
        avatar_button3.place(relx = 0.62, rely = 0.5, anchor = 'center',
                            relwidth = 0.2, relheight = 0.07)
        avatar_button4.place(relx = 0.86, rely = 0.5, anchor = 'center',
                            relwidth = 0.2, relheight = 0.07)
        
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
                if (len(text) >= 3) and (avatar_choice_var.get() > 0):
                    submit_button.configure(state = 'normal')
                else:
                    submit_button.configure(state = 'disabled')
                return True
            else:
                return False
        else:
            return False
    
    def avatar_choice(self, number, text):
        avatar_choice_var.set(value = number)
        avatar_button.configure(state = 'disabled')
        avatar_button2.configure(state = 'disabled')
        avatar_button3.configure(state = 'disabled')
        avatar_button4.configure(state = 'disabled')
        
        if number == 1:
            avatar_button.configure(state = 'normal')
        elif number == 2:
            avatar_button2.configure(state = 'normal')
        elif number == 3:
            avatar_button3.configure(state = 'normal')
        elif number == 4:
            avatar_button4.configure(state = 'normal')     
            
        if (len(text) >= 3) and (avatar_choice_var.get() > 0):
            submit_button.configure(state = 'normal')
        else:
            submit_button.configure(state = 'disabled')   
    
class MenuFrame(ctk.CTkFrame):
    def __init__(self, master):
        # setup
        super().__init__(master = master, fg_color = COLOR)
        
        # variables
        global player_dice_label, computer_dice_label
        global dice1_ico, dice2_ico, dice3_ico, dice4_ico, dice5_ico, dice6_ico
        self.player_score_var = tk.IntVar(value = 0)
        self.computer_score_var = tk.IntVar(value = 0)
        self.timer_var = tk.IntVar(value = 3)
        self.who_win_var = tk.StringVar()  
        size1 = 126   
        
        # players
        self.player = Player(HEALTH)
        self.computer = Player(HEALTH)
        
        # player image
        player_ico = Image.open(f'img/avatars/player/player{avatar_choice_var.get()}.ico')
        player_ico = ctk.CTkImage(player_ico, size = (size1, size1))
        
        # random computer image
        y = random.choice(COMPUTER_NAME_SOURCE)
        y_index = COMPUTER_NAME_SOURCE.index(y)
        
        computer_ico = Image.open(f'img/avatars/computer/{y}.ico')
        computer_ico = ctk.CTkImage(computer_ico, size = (size1, size1))
         
        dice1_ico = Image.open('img/dices/dice1.ico')
        dice1_ico = ctk.CTkImage(dice1_ico, size = (size1, size1))
        
        dice2_ico = Image.open('img/dices/dice2.ico')
        dice2_ico = ctk.CTkImage(dice2_ico, size = (size1, size1))
        
        dice3_ico = Image.open('img/dices/dice3.ico')
        dice3_ico = ctk.CTkImage(dice3_ico, size = (size1, size1))
        
        dice4_ico = Image.open('img/dices/dice4.ico')
        dice4_ico = ctk.CTkImage(dice4_ico, size = (size1, size1))
        
        dice5_ico = Image.open('img/dices/dice5.ico')
        dice5_ico = ctk.CTkImage(dice5_ico, size = (size1, size1))
        
        dice6_ico = Image.open('img/dices/dice6.ico')
        dice6_ico = ctk.CTkImage(dice6_ico, size = (size1, size1))
        
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
        
        player_dice_label = ImageLabel(self)
        computer_dice_label = ImageLabel(self)
        
        self.winner = TitleLabel(self, text = '')
        
        self.damage_label = FirstLabel(self, text = '', font_size = FONT_SIZE2)
        
        # label config
        player_ico_label.configure(image = player_ico)
        computer_ico_label.configure(image = computer_ico)
        self.player_health_bar.configure(value = self.player.health)
        self.computer_health_bar.configure(value = self.computer.health)
        player_dice_label.configure(fg_color = COLOR)
        computer_dice_label.configure(fg_color = COLOR)
        
        x = random.randint(1, 6)
        x2 = random.randint(1, 6)
        self.match_dice(x, x2)
        player_dice_label.configure(image = dice6_ico)
            
        x2 = random.randint(1, 6)
        if x2 == 1:
            computer_dice_label.configure(image = dice1_ico)
        elif x2 == 2:
            computer_dice_label.configure(image = dice2_ico)
        elif x2 == 3:
            computer_dice_label.configure(image = dice3_ico)
        elif x2 == 4:
            computer_dice_label.configure(image = dice4_ico)
        elif x2 == 5:
            computer_dice_label.configure(image = dice5_ico)
        elif x2 == 6:
            computer_dice_label.configure(image = dice6_ico)
            
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
        
        player_dice_label.place(relx = 0.1, rely = 0.6, anchor = 'center')
        computer_dice_label.place(relx = 0.9, rely = 0.6, anchor = 'center')
    
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
        
        damage = self.player_throw - self.computer_throw
        
        self.match_dice(self.player_throw, self.computer_throw)
        
        wait = 500
        wait2 = 1000
        
        if self.player_throw < self.computer_throw:
            self.update()
            self.after(wait, self.who_win_var.set('Przegrałeś!'))
            self.damage_show(-damage)
            self.label_placing() 
            self.update()
            self.computer_win()
            self.computer_score_var.set(self.computer_score_var.get() + 1)
            self.after(wait2, self.label_forget)
            self.after(wait2, self.check_winner())
            self.after(0, self.throw_button.configure(state = 'normal'))
        elif self.player_throw == self.computer_throw:
            self.update()
            self.after(wait, self.who_win_var.set('Remis!'))
            self.damage_show(damage)
            self.label_placing()
            self.update()
            self.after(wait2, self.label_forget)
            self.after(wait2, self.check_winner())
            self.after(0, self.throw_button.configure(state = 'normal'))
        else:
            self.update()
            self.after(wait, self.who_win_var.set('Wygrałeś!'))
            self.damage_show(damage)
            self.label_placing() 
            self.update()
            self.player_win()
            self.player_score_var.set(self.player_score_var.get() + 1)
            self.after(wait2, self.label_forget)
            self.after(wait2, self.check_winner())
            self.after(0, self.throw_button.configure(state = 'normal'))
         
    def label_placing(self):
        self.damage_label.place(relx = 0.5, rely = 0.6, anchor = 'center')
        self.who_win_label.place(relx = 0.5, rely = 0.5, anchor = 'center')
    
    def label_forget(self):
        self.who_win_label.place_forget()
        self.damage_label.place_forget()
         
    def damage_show(self, damage):
        if damage == 0:
            self.damage_label.configure(text = 'Nie zadano obrażeń')
        elif damage == 1:
            self.damage_label.configure(text = f'Zadano {damage} obrażenie')
        elif damage >= 2 and damage < 5:
            self.damage_label.configure(text = f'Zadano {damage} obrażenia')
        elif damage >= 5:
            self.damage_label.configure(text = f'Zadano {damage} obrażeń')            
            
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
        
    def match_dice(self, x, x2):
        # player
        if x == 1:
            player_dice_label.configure(image = dice1_ico)
        elif x == 2:
            player_dice_label.configure(image = dice2_ico)
        elif x == 3:
            player_dice_label.configure(image = dice3_ico)
        elif x == 4:
            player_dice_label.configure(image = dice4_ico)
        elif x == 5:
            player_dice_label.configure(image = dice5_ico)
        elif x == 6:
            player_dice_label.configure(image = dice6_ico)
            
        # computer
        if x2 == 1:
            computer_dice_label.configure(image = dice1_ico)
        elif x2 == 2:
            computer_dice_label.configure(image = dice2_ico)
        elif x2 == 3:
            computer_dice_label.configure(image = dice3_ico)
        elif x2 == 4:
            computer_dice_label.configure(image = dice4_ico)
        elif x2 == 5:
            computer_dice_label.configure(image = dice5_ico)
        elif x2 == 6:
            computer_dice_label.configure(image = dice6_ico)
            
    def check_winner(self):
        wait = 500
        if self.player_score_var.get() == 10 or self.computer.health <= 0:
            self.winner.configure(text = 'Wygrałeś!!!')
            self.after(wait, self.winner.place(relx = 0.5, rely = 0.5, anchor = 'center',
                                               relheight = 0.15))
            self.throw_button.place_forget()
        elif self.computer_score_var.get() == 10 or self.player.health <= 0:
            self.winner.configure(text = 'Przegrałeś!!!')
            self.after(wait, self.winner.place(relx = 0.5, rely = 0.5, anchor = 'center',
                                               relheight = 0.15))
            self.throw_button.place_forget()
        else:
            pass