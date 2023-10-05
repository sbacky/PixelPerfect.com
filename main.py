from PIL import Image
import tkinter as tk
from tkinter import font
from tkinterdnd2 import DND_FILES, TkinterDnD

# Importing functions from other files
from shared_config import SharedConfig
from ui_initialization import initialize_ui
from image_handling import display_instructions, open_image


sc = SharedConfig()

root = TkinterDnD.Tk()
root.drop_target_register(DND_FILES)
root.title("Pixel Perfect")

sc.custom_font = font.Font(family="Helvetica", size=16)

left_frame, open_button, color_frame, color_label, color_preview, color_history_frame, header_label = initialize_ui(root)

# Function to handle drag and drop
def drop(event):
    file_path = event.data.strip().replace('{', '').replace('}', '').replace('"', '')
    sc.canvas = open_image(file_path)

root.dnd_bind('<<Drop>>', drop)

for i in range(1, 6):
    label = tk.Label(color_history_frame, width=10, height=2, bg='white')
    label.grid(row=i, column=0)
    sc.history_labels.append(label)

# Call the function to display instructions
def on_first_configure(event):
    if not sc.image_loaded:
        root.after(100, display_instructions)
        root.unbind('<Configure>', configure_id)

configure_id = root.bind('<Configure>', on_first_configure)

root.mainloop()