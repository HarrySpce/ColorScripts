import tkinter as tk
from tkinter import colorchooser
import colorsys

def rgb_to_hsl(rgb_color):
    r, g, b = [x / 255.0 for x in rgb_color]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    h = round(h * 360)
    s = round(s * 100)
    l = round(l * 100)
    return (h, s, l)

def open_color_picker():
    color = colorchooser.askcolor(title="Choose a Color")
    if color:
        rgb_color = color[0]
        selected_color_label.config(text=f"Selected Color: {color[1]}")
        canvas.config(bg=color[1])
        hsl_color = rgb_to_hsl(rgb_color)
        hsl_label.config(text=f"HSL: {hsl_color}")

root = tk.Tk()
root.title("Color Picker")

choose_color_button = tk.Button(root, text="Choose Color", command=open_color_picker)
choose_color_button.pack(pady=10)

selected_color_label = tk.Label(root, text="Selected Color: None")
selected_color_label.pack()

hsl_label = tk.Label(root, text="HSL: None")
hsl_label.pack()

canvas = tk.Canvas(root, width=200, height=100, bg="white")
canvas.pack()

root.mainloop()
