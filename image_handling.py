import tkinter as tk
from typing import Union
from PIL import Image, ImageTk
from tkinter import filedialog

from shared_config import SharedConfig

sc = SharedConfig()


# Function to display instructions on the canvas
def display_instructions():
    print(f"Canvas dimensions: {sc.canvas.winfo_width()}x{sc.canvas.winfo_height()}") # Debug
    if not sc.image_loaded:
        canvas_width = sc.canvas.winfo_width()
        canvas_height = sc.canvas.winfo_height()

        box_width, box_height = 300, 300  # Dimensions of the instruction box
        x1 = (canvas_width - box_width) // 2
        y1 = (canvas_height - box_height) // 2
        x2 = x1 + box_width
        y2 = y1 + box_height

    sc.canvas.create_rectangle(x1, y1, x2, y2, dash=(4, 4))
    sc.canvas.create_text(canvas_width // 2, canvas_height // 2, text="Drag and drop a file\n\tor\nSelect Open Image below", anchor=tk.CENTER, font=("Helvetica", 16))

def open_image(file_path: Union[str, None]=None):
    # Your existing logic for opening and processing the image
    # This function will return the opened and processed image, and possibly other metadata like scale factors

    # Clear instructions
    sc.canvas.delete("all")
    
    if file_path is None:
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")])
        if not file_path:
            image_loaded = False
            display_instructions(sc.canvas, image_loaded)
            return  # User cancelled the file dialog, do nothing
        
    try:
        sc.orig_img = Image.open(file_path)
        sc.orig_img = sc.orig_img.convert("RGB")
    except FileNotFoundError:
        print("The specified file was not found.")
    except IOError:
        print("The file could not be opened or is not an image.")

    # Scale the image
    max_size = (1024, 768)
    sc.orig_img.thumbnail(max_size)

    tk_img = ImageTk.PhotoImage(sc.orig_img)

    # Calculate scale factors
    sc.x_scale = sc.orig_img.width / tk_img.width()
    sc.y_scale = sc.orig_img.height / tk_img.height()

    sc.canvas.config(width=tk_img.width(), height=tk_img.height())
    sc.canvas.create_image(0, 0, anchor=tk.NW, image=tk_img)
    sc.canvas.image = tk_img

    sc.image_loaded = True