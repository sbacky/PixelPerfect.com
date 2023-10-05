from typing import List, Union, Type, Any
from tkinter import font
import tkinter as tk
from PIL import Image

class SharedConfig:
    _instance: Union[Type['SharedConfig'], None] = None

    def __new__(cls: Type['SharedConfig']) -> 'SharedConfig':
        if cls._instance is None:
            cls._instance = super(SharedConfig, cls).__new__(cls)
            cls._instance.color_history = []
            cls._instance.history_labels = []
            cls._instance.orig_img = Image.new('RGB', (1, 1))
            cls._instance.x_scale = 1
            cls._instance.y_scale = 1
            cls._instance.image_loaded = False
            cls._instance.custom_font = None
            cls._instance.canvas = None
        return cls._instance
    
    def __init__(self):
        """This __init__ method is for IDE support and is not intended to be called at runtime."""
        self.color_history: List[str] = []
        self.history_labels: List[tk.Label] = []
        self.orig_img: Union[Image.Image, None] = None
        self.x_scale: float = 1
        self.y_scale: float = 1
        self.image_loaded: bool = False
        self.custom_font: Union[font.Font, None] = None
        self.canvas: Union[tk.Canvas, None] = None
