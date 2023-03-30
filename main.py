import tkinter as tk
from tkinter import *
from tkinter import colorchooser
from tkinter import ttk

FONT_SIZE_LIST = (8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32)
FONT_COLOR = 'black'
FONT_SIZE = 16


def enable_text():
    for child in text_editor_frame.winfo_children():
        try:
            child.configure(state='normal')
        except:
            child.configure(state='enable')
    # disable for color preview
    if text_editor_color_preview:
        text_editor_color_preview.configure(state='disabled')

    for child in image_editor_frame.winfo_children():
        child.configure(state='disabled')


def enable_image():
    for child in image_editor_frame.winfo_children():
        try:
            child.configure(state='normal')
        except:
            child.configure(state='enable')
    for child in text_editor_frame.winfo_children():
        child.configure(state='disabled')


def pick_font_size(size):
    global FONT_SIZE
    FONT_SIZE = size


def pick_font_color():
    global FONT_COLOR
    FONT_COLOR = tk.colorchooser.askcolor()[1]
    text_editor_color_preview.configure(bg=FONT_COLOR)


def get_text_watermark():

    pass
    # text_on_image.config(text=text_watermark.get())


def update_watermark_text():
    global FONT_COLOR, FONT_SIZE
    # Check current size of image frame
    image_frame.update()
    w = image_frame.winfo_width()
    h = image_frame.winfo_height()

    image_canvas1 = tk.Canvas(image_frame, height=h, width=w)
    image_canvas1.grid(row=0, column=0, sticky='nw')

    # todolist: add density of the watermark for width and height
    distance = watermark_distance.get()
    for watermark_column_stamp in range(0, w-distance, distance):
        for watermark_row_stamp in range(0, h-distance, distance):
            image_canvas1.create_text(watermark_column_stamp, watermark_row_stamp, text=text_watermark.get(), angle=rotation.get(), anchor="nw", fill=FONT_COLOR,
                                  font=('Arial', FONT_SIZE))

    # image_canvas1.create_text(100, 100, text='xxx', angle=rotation.get(), anchor="w", fill=FONT_COLOR, font=('Arial', FONT_SIZE))
    # image_canvas1.create_text(600, 600, text='xxxx', angle=rotation.get(), anchor="w", fill=FONT_COLOR, font=('Arial', FONT_SIZE))


# Creating a window
window = tk.Tk()
window.title('Watermarking app')
width = window.winfo_screenwidth()
height = window.winfo_screenheight()

window.geometry("%dx%d" % (width, height))

# Creating Title
main_title = tk.Label(window, text='Add a watermark to your image', font=('Arial', 10))

# Creating three frames: management, text editor, image
management_frame = ttk.LabelFrame(window, text='Manage the file')
editor_frame = ttk.LabelFrame(window, text='Edit your watermark')
image_frame = ttk.LabelFrame(window, text='Your image preview')

# Creating subframes in editor frame
options_editor_frame = tk.Frame(editor_frame)
text_editor_frame = ttk.LabelFrame(editor_frame, text='Text watermark')
image_editor_frame = ttk.LabelFrame(editor_frame, text='Image watermark')

# Creating subframe for text editor to make apropriate layout


# Layout of the window
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=98)
window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=8)

# Placing the frames
main_title.grid(row=0, column=0, padx=20, pady=5, sticky=tk.N+tk.S, columnspan=3)
management_frame.grid(row=1, column=0, padx=5, pady=2, sticky='news')
editor_frame.grid(row=1, column=1, padx=5, pady=2, sticky='news')
image_frame.grid(row=1, column=2, padx=5, pady=2, sticky='news')

# Placing the editor frames
options_editor_frame.grid(row=0, column=0, padx=5, pady=10, sticky='news')
text_editor_frame.grid(row=1, column=0, padx=5, pady=10, sticky='news')
image_editor_frame.grid(row=2, column=0, padx=5, pady=2, sticky='news')

# text_editor_font_frame.grid(row=2, column=0, padx=0, pady=0, sticky='nws')

# Making the frames to be sticky in columns (that allows the 'sticky' parameter in every frame to work)
management_frame.grid_columnconfigure(0, weight=1)
management_frame.grid_rowconfigure(0, weight=1)
management_frame.grid_rowconfigure(1, weight=1)
management_frame.grid_rowconfigure(2, weight=1)
management_frame.grid_rowconfigure(3, weight=6) #additional row to make the rest of buttons take 3/9 of space

editor_frame.grid_columnconfigure(0, weight=1)
editor_frame.grid_rowconfigure(0, weight=1)
editor_frame.grid_rowconfigure(1, weight=8)
editor_frame.grid_rowconfigure(2, weight=8)
editor_frame.grid_rowconfigure(3, weight=4)

options_editor_frame.grid_columnconfigure(0, weight=1)
options_editor_frame.grid_rowconfigure(0, weight=1)
options_editor_frame.grid_rowconfigure(1, weight=1)

text_editor_frame.grid_rowconfigure(0, weight=1)
text_editor_frame.grid_rowconfigure(1, weight=1)
text_editor_frame.grid_rowconfigure(2, weight=1)
text_editor_frame.grid_rowconfigure(3, weight=1)
text_editor_frame.grid_rowconfigure(4, weight=1)
text_editor_frame.grid_rowconfigure(5, weight=1)
text_editor_frame.grid_rowconfigure(6, weight=1)
text_editor_frame.grid_rowconfigure(7, weight=1)
text_editor_frame.grid_rowconfigure(8, weight=1)
text_editor_frame.grid_rowconfigure(9, weight=100)
text_editor_frame.grid_columnconfigure(0, weight=1)
text_editor_frame.grid_columnconfigure(1, weight=6)

# text_editor_frame.grid_columnconfigure(1, weight=3)
# text_editor_frame.grid_columnconfigure(1, weight=100)
# text_editor_font_frame.grid_columnconfigure(0, weight=1)
# text_editor_font_frame.grid_columnconfigure(1, weight=1)


# editor_frame.grid_rowconfigure(3, weight=28) #additional row to make the rest of space take 3/9

image_frame.grid_columnconfigure(0, weight=1)
image_frame.grid_rowconfigure(0, weight=1)
### Setting the management elements ###
# Creating management buttons
management_button_1 = tk.Button(management_frame, text='Upload an image')
management_button_2 = tk.Button(management_frame, text='Delete image')
management_button_3 = tk.Button(management_frame, text='Save image')

# Placing the management buttons
management_button_1.grid(row=0, column=0, padx=5, pady=5, sticky='news')
management_button_2.grid(row=1, column=0, padx=5, pady=5, sticky='news')
management_button_3.grid(row=2, column=0, padx=5, pady=5, sticky='news')

### Setting the editor elements ###
# Creating radio buttons to choose between image or text watermark
choice = tk.StringVar()
watermark_option_1 = ttk.Radiobutton(options_editor_frame, text='Text', variable=choice, value='watermark_option_1', command=enable_text)
watermark_option_2 = ttk.Radiobutton(options_editor_frame, text='Image', variable=choice, value='watermark_option_2', command=enable_image)

# Placing the editor radio buttons
watermark_option_1.grid(row=0, column=0, padx=15, pady=0, sticky='news')
watermark_option_2.grid(row=1, column=0, padx=15, pady=0, sticky='news')

# Creating text editor elements
text_watermark = tk.StringVar()
chosen_font = tk.IntVar(text_editor_frame)
chosen_font.set(FONT_SIZE)
rotation = tk.DoubleVar(value=0)
watermark_distance = tk.IntVar(value=100)
# text_editor_button = tk.Button(text_editor_frame, text="Text_Button_Example", relief='groove', state='disabled')
text_editor_label = tk.Label(text_editor_frame, text="Write a text for your watermark:", state='disabled')
text_editor_entry = tk.Entry(text_editor_frame, textvariable=text_watermark, state='disabled')
# text_editor_entry_button = tk.Button(text_editor_frame, text='OK', state='disabled', command=get_text_watermark)
text_editor_fonts_label = tk.Label(text_editor_frame, text="Select font size:", state='disabled')
text_editor_fonts_menu = tk.OptionMenu(text_editor_frame, chosen_font, *FONT_SIZE_LIST, command=pick_font_size)
text_editor_fonts_menu.configure(state="disabled")
text_editor_color_picker = tk.Button(text_editor_frame, text='Pick a text color', state='disabled', command=pick_font_color)
text_editor_color_preview = tk.Button(text_editor_frame, text='            ', state='disabled', relief='groove')
text_editor_rotation_label = tk.Label(text_editor_frame, text="Rotate the text:", state='disabled')
text_editor_rotation_scale = tk.Scale(text_editor_frame, variable=rotation, from_=-90, to=90, orient='horizontal', state='disabled')
text_editor_watermark_distance = tk.Scale(text_editor_frame, variable=watermark_distance, from_=50, to=200, orient='horizontal', state='disabled')
text_editor_rotation_scale_button = tk.Button(text_editor_frame, text='Show watermark', state='disabled', command=update_watermark_text)




text_editor_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='nw')
text_editor_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='new')
# text_editor_entry_button.grid(row=1, column=1, padx=7, pady=5, sticky='nw')
text_editor_fonts_label.grid(row=2, column=0, padx=5, pady=10, sticky='nw')
text_editor_fonts_menu.grid(row=2, column=1, padx=5, pady=5, sticky='nw')
text_editor_color_picker.grid(row=3, column=0, padx=5, pady=10, sticky='nw')
text_editor_color_preview.grid(row=3, column=1, padx=7, pady=10, sticky='nw')
text_editor_rotation_label.grid(row=4, column=0, padx=2, pady=(10,5), sticky='nw')
text_editor_rotation_scale.grid(row=5, column=0,columnspan=2, padx=2, pady=5, sticky='new')
text_editor_watermark_distance.grid(row=6, column=0,columnspan=2, padx=2, pady=5, sticky='new')
text_editor_rotation_scale_button.grid(row=7, column=0, columnspan=2, padx=2, pady=10, sticky='new')





# Creating image editor elements
image_var = tk.StringVar()
image_editor_button = tk.Button(image_editor_frame, text="Editor_Button_Example", relief='groove', state='disabled')
image_editor_entry = tk.Entry(image_editor_frame, textvariable=image_var, state='disabled')






image_editor_button.grid(row=0, column=0)
image_editor_entry.grid(row=1, column=0)

# management_frame.pack(side="left", padx=10, pady=10, fill=tk.BOTH)
# editor_frame.pack(side="left", padx=10, pady=10, fill=tk.BOTH)
# image_frame.pack(side="left", padx=10, pady=10, fill=tk.BOTH)
# button_1 = tk.Button(management_frame, text='Upload an image')
# button_2 = tk.Button(editor_frame, text='Edit text')
# button_3 = tk.Button(image_frame, text='picturx')




### Setting the image elements ###
# text_on_image = tk.Label(image_frame, text='test')
# text_on_image.grid(row=0, column=0, sticky='news')



window.mainloop()