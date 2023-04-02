import tkinter as tk
from tkinter import *
from tkinter import colorchooser, ttk, filedialog, messagebox
from PIL import Image, ImageTk, ImageFont, ImageDraw

global original_image
global image_canvas
ADDITIONAL_MARGIN = 20
watermark_text = []
watermark_image = []
IMGS = []
WATERMARK_IMGS = []
original_image = 0
FONT_SIZE_LIST = (8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32)
FONT_COLOR = 'black'
FONT_SIZE = 16

# --- IMAGE HANDLING ---
def upload_image():
    global original_image, image_canvas

    image_file_path = filedialog.askopenfilename()
    image_to_change = Image.open(image_file_path)
    IMGS.append(ImageTk.PhotoImage(image_to_change))
    try:
        delete_watermark()
    except:
        pass
    if original_image != 0:
        try:
            image_canvas.delete(original_image)
        except:
            pass
    image_frame.update()
    photo_width = IMGS[-1].width()
    photo_height = IMGS[-1].height()
    frame_width = photo_width + ADDITIONAL_MARGIN
    frame_height = photo_height + ADDITIONAL_MARGIN

    image_canvas = tk.Canvas(image_frame, width=frame_width, height=frame_height)
    image_canvas.image = IMGS[-1]
    image_canvas.grid(row=0, column=0)
    original_image = image_canvas.create_image((int(frame_width/2), int(frame_height/2)), anchor='center', image=IMGS[-1])


def delete_image():
    global original_image
    global image_canvas
    try:
        delete_watermark()
        image_canvas.delete('all')
        image_canvas.destroy()
    except NameError:
        show_image_first()


def save_image():
    pass


# --- MESSAGEBOXES ---
def show_image_first():
    messagebox.showinfo('No image uploaded', 'Upload an image first')


# --- WATERMARKS HANDLING ---
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


def delete_watermark():
    if watermark_text:
        for id in watermark_text:
            image_canvas.delete(id)
    if watermark_image:
        for id in watermark_image:
            image_canvas.delete(id)


def update_watermark_text():
    global FONT_COLOR, FONT_SIZE
    global image_canvas, watermark_text

    # Check current size of image frame
    w = image_frame.winfo_width()
    h = image_frame.winfo_height()

    distance = watermark_distance.get()

    #deleting previous watermarks (both image and text)
    try:
        delete_watermark()
    except:
        pass

    watermark_text = []
    try:
        for watermark_column_stamp in range(0, w-distance, distance):
            for watermark_row_stamp in range(0, h-distance, distance):
                # Saving ids of every watermark in case of delete
                watermark_text.append(image_canvas.create_text(watermark_column_stamp, watermark_row_stamp, text=text_watermark.get(), angle=rotation.get(), anchor="nw", fill=FONT_COLOR,
                                  font=('Arial', FONT_SIZE)))
    except:
        show_image_first()


def update_watermark_image():
    global FONT_COLOR, FONT_SIZE
    global image_canvas, watermark_image

    # Check current size of image frame
    w = image_frame.winfo_width()
    h = image_frame.winfo_height()

    distance = image_watermark_distance.get()

    # deleting previous watermarks (both image and text)
    try:
        delete_watermark()
    except:
        pass

    watermark_image = []
    try:
        for watermark_column_stamp in range(0, w - distance, distance):
            for watermark_row_stamp in range(0, h - distance, distance):
                watermark_image.append(
                image_canvas.create_image(watermark_column_stamp, watermark_row_stamp, anchor='nw', image=WATERMARK_IMGS[-1]))
    except:
        show_image_first()


def upload_watermark_image():
    global FONT_COLOR, FONT_SIZE
    global image_canvas, watermark_image

    image_file_path = filedialog.askopenfilename()
    image_to_change = Image.open(image_file_path)
    WATERMARK_IMGS.append(ImageTk.PhotoImage(image_to_change))

    update_watermark_image()

# --- WINDOW LAYOUT ---
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

# Layout of the window
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=98)
window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=15)

# Placing the frames
main_title.grid(row=0, column=0, padx=20, pady=5, sticky=tk.N+tk.S, columnspan=3)
management_frame.grid(row=1, column=0, padx=5, pady=2, sticky='news')
editor_frame.grid(row=1, column=1, padx=5, pady=2, sticky='news')
image_frame.grid(row=1, column=2, padx=5, pady=2, sticky='news')

# Placing the editor frames
options_editor_frame.grid(row=0, column=0, padx=5, pady=10, sticky='news')
text_editor_frame.grid(row=1, column=0, padx=5, pady=10, sticky='news')
image_editor_frame.grid(row=2, column=0, padx=5, pady=2, sticky='news')

# management frame editor layout
management_frame.grid_columnconfigure(0, weight=1)
management_frame.grid_rowconfigure(0, weight=1)
management_frame.grid_rowconfigure(1, weight=1)
management_frame.grid_rowconfigure(2, weight=1)
management_frame.grid_rowconfigure(3, weight=6)

# editor frame editor layout
editor_frame.grid_columnconfigure(0, weight=1)
editor_frame.grid_rowconfigure(0, weight=1)
editor_frame.grid_rowconfigure(1, weight=8)
editor_frame.grid_rowconfigure(2, weight=8)
editor_frame.grid_rowconfigure(3, weight=4)

# options editor layout
options_editor_frame.grid_columnconfigure(0, weight=1)
options_editor_frame.grid_rowconfigure(0, weight=1)
options_editor_frame.grid_rowconfigure(1, weight=1)

# text editor layout
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

# image editor layout
image_editor_frame.grid_rowconfigure(0, weight=10)
image_editor_frame.grid_rowconfigure(1, weight=1)
image_editor_frame.grid_rowconfigure(2, weight=1)
image_editor_frame.grid_rowconfigure(3, weight=1)
image_editor_frame.grid_rowconfigure(4, weight=1)
image_editor_frame.grid_rowconfigure(5, weight=1)
image_editor_frame.grid_rowconfigure(6, weight=100)
image_editor_frame.grid_columnconfigure(0, weight=1)

# image frame editor layout
image_frame.grid_columnconfigure(0, weight=1)
image_frame.grid_rowconfigure(0, weight=1)

### Setting the management elements ###
# Creating management buttons
management_button_1 = tk.Button(management_frame, text='Upload an image', command=upload_image)
management_button_2 = tk.Button(management_frame, text='Delete image', command=delete_image)
management_button_3 = tk.Button(management_frame, text='Save image', command=save_image)

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

# text watermark
text_editor_label = tk.Label(text_editor_frame, text="Write a text for your watermark:", state='disabled')
text_editor_entry = tk.Entry(text_editor_frame, textvariable=text_watermark, state='disabled')

# font options
text_editor_fonts_label = tk.Label(text_editor_frame, text="Select font size:", state='disabled')
text_editor_fonts_menu = tk.OptionMenu(text_editor_frame, chosen_font, *FONT_SIZE_LIST, command=pick_font_size)
text_editor_fonts_menu.configure(state="disabled")

# color picker
text_editor_color_picker = tk.Button(text_editor_frame, text='Pick a text color', state='disabled', command=pick_font_color)
text_editor_color_preview = tk.Button(text_editor_frame, text='            ', state='disabled', relief='groove')

# text rotation
text_editor_rotation_label = tk.Label(text_editor_frame, text="Rotate the text:", state='disabled')
text_editor_rotation_scale = tk.Scale(text_editor_frame, variable=rotation, from_=-90, to=90, orient='horizontal', state='disabled')

# additional text functions
text_editor_watermark_distance_label = tk.Label(text_editor_frame, text="Density of the watermark [px]:", state='disabled')
text_editor_watermark_distance = tk.Scale(text_editor_frame, variable=watermark_distance, from_=50, to=200, orient='horizontal', state='disabled')
text_editor_show_button = tk.Button(text_editor_frame, text='Show watermark', state='disabled', command=update_watermark_text)

# text editor layout
text_editor_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='nw')
text_editor_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='new')
text_editor_fonts_label.grid(row=2, column=0, padx=5, pady=10, sticky='nw')
text_editor_fonts_menu.grid(row=2, column=1, padx=5, pady=5, sticky='nw')
text_editor_color_picker.grid(row=3, column=0, padx=5, pady=10, sticky='nw')
text_editor_color_preview.grid(row=3, column=1, padx=7, pady=10, sticky='nw')
text_editor_rotation_label.grid(row=4, column=0, padx=2, pady=(10,5), sticky='nw')
text_editor_rotation_scale.grid(row=5, column=0,columnspan=2, padx=2, pady=5, sticky='new')
text_editor_watermark_distance_label.grid(row=6, column=0, padx=2, pady=(10,5), sticky='nw')
text_editor_watermark_distance.grid(row=7, column=0,columnspan=2, padx=2, pady=5, sticky='new')
text_editor_show_button.grid(row=8, column=0, columnspan=2, padx=5, pady=10, sticky='news')

# Creating image editor elements
image_watermark_distance = tk.IntVar(value=100)
image_editor_upload_watermark_button = tk.Button(image_editor_frame, text="Upload image watermark", state='disabled', command=upload_watermark_image)
image_editor_watermark_distance_label = tk.Label(image_editor_frame, text="Density of the watermark [px]:", state='disabled')
image_editor_watermark_distance = tk.Scale(image_editor_frame, variable=image_watermark_distance, from_=50, to=200, orient='horizontal', state='disabled')
image_editor_show_button = tk.Button(image_editor_frame, text='Show watermark', state='disabled', command=update_watermark_image)

# image editor layout
image_editor_upload_watermark_button.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='news')
image_editor_watermark_distance_label.grid(row=1, column=0, padx=2, pady=(10,5), sticky='nw')
image_editor_watermark_distance.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='new')
image_editor_show_button.grid(row=3, column=0, columnspan=2, padx=7, pady=5, sticky='news')


window.mainloop()