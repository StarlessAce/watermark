import tkinter as tk
from tkinter import ttk


def enable_text():
    for child in text_editor_frame.winfo_children():
        child.configure(state='normal')
    for child in image_editor_frame.winfo_children():
        child.configure(state='disabled')


def enable_image():
    for child in image_editor_frame.winfo_children():
        child.configure(state='normal')
    for child in text_editor_frame.winfo_children():
        child.configure(state='disabled')


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

# editor_frame.grid_rowconfigure(3, weight=28) #additional row to make the rest of space take 3/9

image_frame.grid_columnconfigure(0, weight=1)

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
text_var = tk.StringVar()
text_editor_button = tk.Button(text_editor_frame, text="Text_Button_Example", relief='groove', state='disabled')
text_editor_entry = tk.Entry(text_editor_frame, textvariable=text_var, state='disabled')

text_editor_button.grid(row=0, column=0)
text_editor_entry.grid(row=1, column=0)
# Creating image editor elements
image_var = tk.StringVar()
image_editor_button = tk.Button(image_editor_frame, text="Editor_Button_Example", relief='groove', state='disabled')
image_editor_entry = tk.Entry(image_editor_frame, textvariable=image_var, state='disabled')


image_editor_button.grid(row=0, column=0)
image_editor_entry.grid(row=1, column=0)

# management_frame.pack(side="left", padx=10, pady=10, fill=tk.BOTH)
# editor_frame.pack(side="left", padx=10, pady=10, fill=tk.BOTH)
# image_frame.pack(side="left", padx=10, pady=10, fill=tk.BOTH)
button_1 = tk.Button(management_frame, text='Upload an image')
button_2 = tk.Button(editor_frame, text='Edit text')
button_3 = tk.Button(image_frame, text='picturx')

