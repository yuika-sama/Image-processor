import os
from tkinter import *
from tkinter import filedialog
import cv2
import numpy as np
from PIL import Image, ImageTk
from process import ImageProcessor
from camera_viewer import CameraViewer

class AppGUI:
    def __init__(self, master):
        self.master = master
        self.image_processor = ImageProcessor()

        self.video_stream = cv2.VideoCapture(0)

        self.setup_gui()

    def setup_gui(self):
        self.master.geometry("1500x800")
        self.master.configure(bg='grey')
        self.master.title("Image Processor")

        self.panel = Label(self.master)
        self.panel.grid(row=0, column=0, rowspan=12, padx=50, pady=60)

        self.image_processor.load_image('assets/logo.jpg')
        self.display_image(self.image_processor.img)

        self.brightness_slider = Scale(self.master, label="Brightness", from_=0, to=2,
                                       orient=HORIZONTAL, length=200, resolution=0.1,
                                       command=self.process_brightness, bg="#dddddd")
        self.brightness_slider.set(1)
        self.brightness_slider.configure(font=('consolas', 10, 'bold'), foreground='black')
        self.brightness_slider.place(x=1070, y=15)

        self.contrast_slider = Scale(self.master, label="Contrast", from_=0, to=2,
                                       orient=HORIZONTAL, length=200, resolution=0.1,
                                       command=self.process_contrast, bg="#dddddd")
        self.contrast_slider.set(1)
        self.contrast_slider.configure(font=('consolas', 10, 'bold'), foreground='black')
        self.contrast_slider.place(x=1070, y=90)

        self.sharpness_slider = Scale(self.master, label="Sharpness", from_=0, to=2,
                                     orient=HORIZONTAL, length=200, resolution=0.1,
                                     command=self.process_sharpness, bg="#dddddd")
        self.sharpness_slider.set(1)
        self.sharpness_slider.configure(font=('consolas', 10, 'bold'), foreground='black')
        self.sharpness_slider.place(x=1070, y=165)

        self.vibrance_slider = Scale(self.master, label="Vibrance", from_=0, to=2,
                                      orient=HORIZONTAL, length=200, resolution=0.1,
                                      command=self.process_vibrance, bg="#dddddd")
        self.vibrance_slider.set(1)
        self.vibrance_slider.configure(font=('consolas', 10, 'bold'), foreground='black')
        self.vibrance_slider.place(x=1070, y=240)

        # self.get_channel()
        self.red_slider = Scale(self.master, label="Red", from_=0, to=255,
                                     orient=HORIZONTAL, length=200, resolution=1,
                                     command=self.process_red, bg="#dddddd")
        self.red_slider.set(255)
        self.red_slider.configure(font=('consolas', 10, 'bold'), foreground='black')
        self.red_slider.place(x=1070, y=315)

        self.green_slider = Scale(self.master, label="Green", from_=0, to=255,
                                orient=HORIZONTAL, length=200, resolution=1,
                                command=self.process_green, bg="#dddddd")
        self.green_slider.set(255)
        self.green_slider.configure(font=('consolas', 10, 'bold'), foreground='black')
        self.green_slider.place(x=1070, y=390)

        self.blue_slider = Scale(self.master, label="Blue", from_=0, to=255,
                                orient=HORIZONTAL, length=200, resolution=1,
                                command=self.process_blue, bg="#dddddd")
        self.blue_slider.set(255)
        self.blue_slider.configure(font=('consolas', 10, 'bold'), foreground='black')
        self.blue_slider.place(x=1070, y=465)



        self.rotate_btn = Button(self.master, text='Rotate', width=25,
                                 command=self.rotate, bg="#dddddd")
        self.rotate_btn.configure(font=('consolas', 10, 'bold'), foreground='black')
        self.rotate_btn.place(x = 1300, y = 110)

        self.flip_btn = Button(self.master, text='Flip', width=25,
                                 command=self.open_flip_window, bg="#dddddd")
        self.flip_btn.configure(font=('consolas', 10, 'bold'), foreground='black')
        self.flip_btn.place(x=1300, y=145)

        self.blur_btn = Button(self.master, text='Blur', width=25,
                               command=self.blur, bg="#dddddd")
        self.blur_btn.configure(font=('consolas', 10, 'bold'), foreground='black')
        self.blur_btn.place(x=1300, y=180)

        self.emboss_btn = Button(self.master, text='Emboss', width=25,
                               command=self.emboss, bg="#dddddd")
        self.emboss_btn.configure(font=('consolas', 10, 'bold'), foreground='black')
        self.emboss_btn.place(x=1300, y=215)

        self.resize_btn = Button(self.master, text='Resize', width=25,
                                 command=self.resize, bg="#dddddd")
        self.resize_btn.configure(font=('consolas', 10, 'bold'), foreground='black')
        self.resize_btn.place(x=1300, y=250)

        self.crop_btn = Button(self.master, text='Crop', width=25,
                                 command=self.resize, bg="#dddddd")
        self.crop_btn.configure(font=('consolas', 10, 'bold'), foreground='black')
        self.crop_btn.place(x=1300, y=285)

        self.edge_btn = Button(self.master, text='Edge Enhance', width=25,
                                 command=self.resize, bg="#dddddd")
        self.edge_btn.configure(font=('consolas', 10, 'bold'), foreground='black')
        self.edge_btn.place(x=1300, y=320)

        self.camera_btn = Button(self.master, text = 'Camera', width = 20,
                                     command = self.camera_window_open, bg = "#dddddd")
        self.camera_btn.configure(font=('consolas', 10, 'bold'), foreground='black')
        self.camera_btn.place(x = 50, y = 680)


        self.load_image_button = Button(self.master, text="Load Image",
                                        command=self.load_image)
        self.load_image_button.place(x=50, y=25)

        self.entry_box = Entry(self.master, font=('consolas', 10, 'normal'), width=75)
        self.entry_box.place(x = 130, y = 27)

        self.save_btn = Button(self.master, text='Save', width=20,
                                 command=self.save_image, bg="#dddddd")
        self.save_btn.configure(font=('consolas', 10, 'bold'), foreground='black')
        self.save_btn.place(x=210, y=680)

    def display_image(self, img):
        display_image = ImageTk.PhotoImage(img)
        self.panel.configure(image=display_image)
        self.panel.image = display_image

    def save_image(self):
        filename = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
        if filename:
            self.image_processor.save_image(filename)
    def load_image(self):
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image",
                                              filetypes=(("JPEG files", "*.jpg"), ("All files", "*.*")))
        if filename:
            self.entry_box.insert(END, filename)
            self.image_processor.load_image(filename)
            self.get_channel()
            self.red_slider.set(255)
            self.green_slider.set(255)
            self.blue_slider.set(255)
            self.display_image(self.image_processor.img)

    def process_brightness(self, position):
        if self.image_processor.img:
            self.image_processor.enhance_brightness(position)
            self.display_image(self.image_processor.output_image)

    def process_contrast(self, position):
        if self.image_processor.img:
            self.image_processor.enhance_contrast(position)
            self.display_image(self.image_processor.output_image)

    def process_sharpness(self, position):
        if self.image_processor.img:
            self.image_processor.enhance_sharpness(position)
            self.display_image(self.image_processor.output_image)

    def process_vibrance(self, position):
        if self.image_processor.img:
            self.image_processor.enhance_vibrance(position)
            self.display_image(self.image_processor.output_image)

    def get_channel(self):
        if self.image_processor.img:
            red, green, blue = self.image_processor.extract_color()
            self.red = sum(red) // len(red)
            self.green = sum(green) // len(green)
            self.blue = sum(blue) // len(blue)

    def process_red(self, position):
        if self.image_processor.img:
            self.image_processor.enhance_red(position)
            self.display_image(self.image_processor.output_image)

    def process_green(self, position):
        if self.image_processor.img:
            self.image_processor.enhance_green(position)
            self.display_image(self.image_processor.output_image)

    def process_blue(self, position):
        if self.image_processor.img:
            self.image_processor.enhance_blue(position)
            self.display_image(self.image_processor.output_image)

    def rotate(self):
        if self.image_processor.img:
            self.image_processor.rotate()
            self.display_image(self.image_processor.output_image)

    def open_flip_window(self):
        flip_window = Toplevel(self.master)
        flip_window.title("Camera")

        horizontal_flip_btn = Button(flip_window, text = "Horizontal Flip",
                                     command = self.flip_horizontal,
                                     width = 20, bg = "#dddddd")
        horizontal_flip_btn.pack(pady = 10)

        vertical_flip_btn = Button(flip_window, text="Vertical Flip",
                                     command=self.flip_vertical,
                                     width=20, bg="#dddddd")
        vertical_flip_btn.pack(pady=10)

    def flip_horizontal(self):
        if self.image_processor.img:
            self.image_processor.flip_horizontal()
            self.display_image(self.image_processor.output_image)

    def flip_vertical(self):
        if self.image_processora.img:
            self.image_processor.flip_vertical()
            self.display_image(self.image_processor.output_image)
    def blur(self):
        if self.image_processor.img:
            self.image_processor.blur()
            self.display_image(self.image_processor.output_image)

    def emboss(self):
        if self.image_processor.img:
            self.image_processor.emboss()
            self.display_image(self.image_processor.output_image)

    def resize(self):
        if self.image_processor.img:
            self.image_processor.resize()
            self.display_image(self.image_processor.output_image)

    def crop(self):
        if self.image_processor.img:
            self.image_processor.crop()
            self.display_image(self.image_processor.output_image)

    def edge(self):
        if self.image_processor.img:
            self.image_processor.edge()
            self.display_image(self.image_processor.output_image)

    def camera_window_open(self):
        camera_window = Toplevel(self.master)
        camera_window.title("Camera")

        self.camera_viewer = CameraViewer(camera_window, self)


    def show_captured_image(self, image_path):
        self.image_processor.load_image('captures/captured_image.jpg')
        self.display_image(self.image_processor.img)
        self.entry_box.insert(END, image_path)