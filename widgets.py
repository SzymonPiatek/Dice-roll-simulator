# Import data from other files
from settings import *

# Import needed libraries
import tkinter as tk
import customtkinter as ctk
from tkinter import ttk

# Create classes
class FirstLabel(ctk.CTkLabel):
    def __init__(self, parent, text, font_size):
        # setup
        super().__init__(
            master = parent,
            text = text,
            fg_color = COLOR,
            font = (ctk.CTkFont(family = FONT_FAMILY, size = font_size, weight = 'bold')),
            corner_radius = CORNER_RADIUS,
            text_color = TEXT_COLOR3)
        
class ImageLabel(ctk.CTkLabel):
    def __init__(self, parent):
        # setup
        super().__init__(
            master = parent,
            corner_radius = CORNER_RADIUS3,
            fg_color = COLOR3,
            text = '')
        
class TitleLabel(ctk.CTkLabel):
    def __init__(self, parent, text):
        # setup
        super().__init__(
            master = parent,
            corner_radius = CORNER_RADIUS3,
            fg_color = COLOR2,
            font = (ctk.CTkFont(family = FONT_FAMILY, size = FONT_SIZE, weight = 'bold')),
            text = text,
            text_color = TEXT_COLOR)    

class ScoreLabel(ctk.CTkLabel):
    def __init__(self, parent, var, font_size):
        # setup
        super().__init__(
            master = parent,
            textvariable = var,
            fg_color = COLOR,
            font = (ctk.CTkFont(family = FONT_FAMILY, size = font_size, weight = 'bold')),
            corner_radius = CORNER_RADIUS,
            text_color = TEXT_COLOR3)
        
class VersionLabel(ctk.CTkLabel):
    def __init__(self, parent, text):
        # setup
        super().__init__(
            master = parent,
            text = text,
            fg_color = COLOR,
            font = (ctk.CTkFont(family = FONT_FAMILY, size = FONT_SIZE3, weight = 'bold')),
            corner_radius = CORNER_RADIUS,
            justify = 'center',
            text_color = TEXT_COLOR3)
        
class FirstEntry(ctk.CTkEntry):
    def __init__(self, parent, var, command):
        # setup
        super().__init__(
            master = parent,
            fg_color = COLOR2,
            textvariable = var,
            font = (ctk.CTkFont(family = FONT_FAMILY, size = FONT_SIZE, weight = 'bold')),
            corner_radius = CORNER_RADIUS2,
            justify = 'center',
            text_color = TEXT_COLOR,
            validate = 'key',
            validatecommand = (command, "%P"))
        
class FirstButton(ctk.CTkButton):
    def __init__(self, parent, text, func):
        # setup
        super().__init__(
            master = parent,
            fg_color = COLOR2,
            hover_color = COLOR4,
            text = text,
            font = (ctk.CTkFont(family = FONT_FAMILY, size = FONT_SIZE2, weight = 'bold')),
            corner_radius = CORNER_RADIUS2,
            text_color = TEXT_COLOR,
            command = func)
        
class HealthBar(ttk.Progressbar):
    def __init__(self, parent, max):
        # setup
        super().__init__(
            master = parent,
            mode = 'determinate',
            maximum = max)