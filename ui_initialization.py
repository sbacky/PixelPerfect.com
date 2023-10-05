
import tkinter as tk

from color_picking import canvas_click
from image_handling import open_image
from shared_config import SharedConfig

sc = SharedConfig()

def initialize_ui(root):
    # Create a frame to contain the canvas, open button, and color information
    left_frame = tk.Frame(root)
    left_frame.pack(side=tk.LEFT, padx=10, pady=10)

    # Create canvas and attach click event
    sc.canvas = tk.Canvas(left_frame, bg='white', width=512, height=512)
    sc.canvas.bind("<Button-1>", lambda event: canvas_click(event, color_preview, color_label))
    sc.canvas.pack()

    # Create open button
    open_button = tk.Button(left_frame, text="Open Image", command=open_image, font=sc.custom_font)
    open_button.pack(pady=5)

    # Create a frame to hold the color information
    color_frame = tk.Frame(left_frame)
    color_frame.pack()

    # Create labels for color information
    color_label = tk.Label(color_frame, text="Color: N/A", font=sc.custom_font)
    color_label.pack(side=tk.LEFT, pady=5)

    color_preview = tk.Label(color_frame, text="     ", bg="white", font=sc.custom_font)
    color_preview.pack(side=tk.LEFT, padx=2, pady=5)

    # Create a frame to hold the color history labels
    color_history_frame = tk.Frame(root)
    color_history_frame.pack(side=tk.RIGHT, anchor='n', padx=10, pady=10)

    header_label = tk.Label(color_history_frame, text="Color History", font=("Arial", 16))
    header_label.grid(row=0, column=0)

    return left_frame, open_button, color_frame, color_label, color_preview, color_history_frame, header_label
