from shared_config import SharedConfig

sc = SharedConfig()


def update_color_history_ui():
    # Your existing logic for updating the color history UI
    for i, color in enumerate(sc.color_history):
        # Extract RGB values from the hex color
        R, G, B = int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16)
        
        # Calculate brightness
        brightness = (0.299 * R) + (0.587 * G) + (0.114 * B)
        
        # Decide text color based on brightness
        text_color = "black" if brightness > 128 else "white"

        sc.history_labels[i].config(bg=color, text=color, fg=text_color)