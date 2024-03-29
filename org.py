# importing required modules
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter, ImageEnhance
from tkinter.filedialog import askopenfilename
import os


# processing function

# displaying image
def displayimage(img):
    # display image function, using pillow - ImageTk
    display_image = ImageTk.PhotoImage(img)
    panel.configure(image=display_image)
    panel.image = display_image


# get filepath
def browse_path():
    filename = askopenfilename(filetypes=(("jpg file", "*.jpg"), ("png file", '*.png'), ("All files", " *.* "),))
    entry_box.insert(END, filename)


# get image file
def change_image():
    global img
    img_name = filedialog.askopenfilename(title="Change Image")
    if img_name:
        img = Image.open(img_name)
        img = img.resize((600, 600))
        displayimage(img)


# brightness slider
def brightness_call(position):
    position = float(position)
    global output_image
    enhancer = ImageEnhance.Brightness(img)
    output_image = enhancer.enhance(position)
    displayimage(output_image)


# constrast slider
def constrast_call(position):
    position = float(position)
    global output_image
    enhancer = ImageEnhance.Contrast(img)
    output_image = enhancer.enhance(position)
    displayimage(output_image)


# sharpness slider
def sharpness_call(position):
    position = float(position)
    global output_image
    enhancer = ImageEnhance.Sharpness(img)
    output_image = enhancer.enhance(position)
    displayimage(output_image)


# color slider
def color_call(position):
    position = float(position)
    global output_image
    enhancer = ImageEnhance.Color(img)
    output_image = enhancer.enhance(position)
    displayimage(output_image)


# red color changing
def red_changing(position):
    position = float(position)
    global img
    r, g, b = img.split()
    r = r.point(lambda i: i * position)
    px = Image.merge('RGB', (r, g, b))
    displayimage(px)
    # img = px


# green color changing
def green_changing(position):
    position = float(position)
    global img
    r, g, b = img.split()
    g = g.point(lambda i: i * position)
    px = Image.merge('RGB', (r, g, b))
    displayimage(px)
    # img = px


# blue color changing
def blue_changing(position):
    position = float(position)
    global img
    r, g, b = img.split()
    b = r.point(lambda i: i * position)
    px = Image.merge('RGB', (r, g, b))
    displayimage(px)
    # img = px


# Rotate button
def rotate():
    global img
    img = img.rotate(90)
    displayimage(img)


# Flip button
def flip():
    global img
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    displayimage(img)


# Blur button
def blurr():
    global img
    img = img.filter(ImageFilter.BLUR)
    displayimage(img)


# Emboss button
def emboss():
    global img
    img = img.filter(ImageFilter.EMBOSS)
    displayimage(img)


# Resize button
def resize():
    global img
    img = img.resize((200, 300))
    displayimage(img)


# Crop button
def crop():
    global img
    img = img.crop((100, 100, 400, 400))
    displayimage(img)


# Edge Enhance button
def edge_enhance():
    global img
    img = img.filter(ImageFilter.FIND_EDGES)
    displayimage(img)


# Reset function
def reset():
    mains.destroy()
    os.popen("org.py")


# Save button
def save():
    global img
    savefile = filedialog.asksaveasfile(
        filetypes=(("jpg file", "*.jpg"), ("png file", '*.png'), ("All files", " *.* "),))
    output_image.save(savefile)


# close()
def close():
    mains.destroy()


# creating window
mains = Tk()  # calling tk module
space = " " * 215  # string space
screen_width = mains.winfo_screenwidth()
screen_height = mains.winfo_screenheight()
mains.geometry(f"{screen_width}x{screen_height}")
mains.configure(bg='grey')
mains.title(f"{space}Test test test")

# setting default image
img = Image.open("assets/logo.jpg")
img = img.resize((600, 600))

# creating panel for displaying default image
panel = Label(mains)
panel.grid(row=0, column=0, rowspan=12, padx=50, pady=50)
displayimage(img)

# <drawing filepath>
entry_box = Entry(mains, font=('consolas', 10, 'normal'), width=50)
entry_box.place(x=50, y=750)
button1 = Button(mains, text="Open", font=('consolas', 10, 'normal'), command=browse_path)
button1.place(x=420, y=747)
# drawing path's box

# making buttons
# <<Making Sliders>>
# <Brightness slider>
brightness_slider = Scale(mains, label="Brightness", from_=0, to=2, orient=HORIZONTAL, length=200, resolution=0.1,
                          command=brightness_call, bg="#dddddd")  # create button
brightness_slider.set(1)  # set default
brightness_slider.configure(font=('consolas', 10, 'bold'), foreground='black')  # config button
brightness_slider.place(x=1070, y=15)  # placement
# brightness_slider.grid(row = 0, column = 3)

# <Constrast slider>
contrast_slider = Scale(mains, label="Contrast", from_=0, to=2, orient=HORIZONTAL, length=200, resolution=0.1,
                        command=constrast_call, bg="#dddddd")  # create button
contrast_slider.set(1)  # set default
contrast_slider.configure(font=('consolas', 10, 'bold'), foreground='black')  # config button
contrast_slider.place(x=1070, y=90)  # placement

# <Sharpness slider>
sharpness_slider = Scale(mains, label="Sharpness", from_=0, to=2, orient=HORIZONTAL, length=200, resolution=0.1,
                         command=sharpness_call, bg="#dddddd")  # create button
sharpness_slider.set(1)  # set default
sharpness_slider.configure(font=('consolas', 10, 'bold'), foreground='black')  # config button
sharpness_slider.place(x=1070, y=165)  # placement

# <Color slider>
# vibration ??
color_slider = Scale(mains, label="Color", from_=0, to=2, orient=HORIZONTAL, length=200, resolution=0.1,
                     command=color_call, bg="#dddddd")  # create button
color_slider.set(1)  # set default
color_slider.configure(font=('consolas', 10, 'bold'), foreground='black')  # config button
color_slider.place(x=1070, y=240)  # placement

# <Color slider>
# vibration ??
R_slider = Scale(mains, label="Red", from_=0, to=1, orient=HORIZONTAL, length=200, resolution=0.1,
                 command=red_changing, bg="#dddddd")  # create button
R_slider.set(1)  # set default
R_slider.configure(font=('consolas', 10, 'bold'), foreground='black')  # config button
R_slider.place(x=1070, y=315)  # placement

G_slider = Scale(mains, label="Green", from_=0, to=1, orient=HORIZONTAL, length=200, resolution=0.1,
                 command=green_changing, bg="#dddddd")  # create button
G_slider.set(1)  # set default
G_slider.configure(font=('consolas', 10, 'bold'), foreground='black')  # config button
G_slider.place(x=1070, y=390)  # placement

B_slider = Scale(mains, label="Blue", from_=0, to=1, orient=HORIZONTAL, length=200, resolution=0.1,
                 command=blue_changing, bg="#dddddd")  # create button
B_slider.set(1)  # set default
B_slider.configure(font=('consolas', 10, 'bold'), foreground='black')  # config button
B_slider.place(x=1070, y=465)  # placement
# <<Making buttons>>
# <Change button>
change_button = Button(mains, text='Change', width=25, command=change_image, bg="#dddddd")
change_button.configure(font=('consolas', 10, 'bold'), foreground='black')
change_button.place(x=805, y=35)

# <Reset button>
reset_button = Button(mains, text='Reset', width=25, command=reset, bg="#dddddd")
reset_button.configure(font=('consolas', 10, 'bold'), foreground='black')
reset_button.place(x=805, y=72)

# <Rotate button>
rotate_button = Button(mains, text='Rotate', width=25, command=rotate, bg="#dddddd")
rotate_button.configure(font=('consolas', 10, 'bold'), foreground='black')
rotate_button.place(x=805, y=110)

# <Flip button>
crop_button = Button(mains, text='Crop', width=25, command=crop, bg="#dddddd")
crop_button.configure(font=('consolas', 10, 'bold'), foreground='black')
crop_button.place(x=805, y=147)

# <Blur button>
blur_button = Button(mains, text='Blur', width=25, command=blurr, bg="#dddddd")
blur_button.configure(font=('consolas', 10, 'bold'), foreground='black')
blur_button.place(x=805, y=185)

# <Resize button>
resize_button = Button(mains, text='Resize', width=25, command=resize, bg="#dddddd")
resize_button.configure(font=('consolas', 10, 'bold'), foreground='black')
resize_button.place(x=805, y=222)

# <Emboss button>
emboss_button = Button(mains, text='Emboss', width=25, command=emboss, bg="#dddddd")
emboss_button.configure(font=('consolas', 10, 'bold'), foreground='black')
emboss_button.place(x=805, y=260)

# <Edge enhance button>
edup_button = Button(mains, text='Edge Enhance', width=25, command=edge_enhance, bg="#dddddd")
edup_button.configure(font=('consolas', 10, 'bold'), foreground='black')
edup_button.place(x=805, y=297)

# <Save button>
save_button = Button(mains, text='Save', width=25, command=save, bg="#dddddd")
save_button.configure(font=('consolas', 10, 'bold'), foreground='black')
save_button.place(x=805, y=333)

# <Close button>
close_button = Button(mains, text='Close', width=25, command=close, bg="#dddddd")
close_button.configure(font=('consolas', 10, 'bold'), foreground='black')
close_button.place(x=805, y=370)

# call
mains.mainloop()
