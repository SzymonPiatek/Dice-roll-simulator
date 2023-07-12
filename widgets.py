# Import data from other files
from settings import *

# Import needed libraries
import tkinter as tk
import customtkinter as ctk

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
        
class SecondLabel(ctk.CTkLabel):
    def __init__(self, parent, textvariable, fg_color, text_color, font_size):
        # setup
        super().__init__(
            master = parent,
            textvariable = textvariable,
            fg_color = fg_color,
            font = (ctk.CTkFont(family = FONT_FAMILY, size = font_size, weight = 'bold')),
            corner_radius = CORNER_RADIUS,
            justify = 'center',
            text_color = text_color)
        
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
    def __init__(self, parent, var):
        # setup
        super().__init__(
            master = parent,
            fg_color = COLOR2,
            textvariable = var,
            font = (ctk.CTkFont(family = FONT_FAMILY, size = FONT_SIZE, weight = 'bold')),
            corner_radius = CORNER_RADIUS2,
            justify = 'center',
            text_color = TEXT_COLOR)
        
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
            text_color = TEXT_COLOR)