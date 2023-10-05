import tkinter as tk
from PIL import Image

from color_history import update_color_history_ui
from shared_config import SharedConfig

sc = SharedConfig()


def get_hex_color(image: Image.Image, x: int, y: int):
    r, g, b = image.getpixel((x, y))
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def canvas_click(event: tk.Event, color_preview: tk.Label, color_label: tk.Label):
    # Your existing logic for handling canvas clicks and color picking
    canvas_x, canvas_y = event.x, event.y
    img_x, img_y = int(canvas_x / sc.x_scale), int(canvas_y / sc.y_scale)
    hex_color = get_hex_color(sc.orig_img, img_x, img_y)
    
    color_preview.config(bg=hex_color)
    color_label.config(text=f"Color: {hex_color}")

    # Update color history
    if len(sc.color_history) >= 5:
        sc.color_history.pop(0)
    sc.color_history.append(hex_color)
    
    # Call the function to update the UI
    update_color_history_ui()