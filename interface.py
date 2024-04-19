import os
from tkinter import *
from tkinter import filedialog

import cv2
from PIL import ImageTk

from camera_viewer import CameraViewer
from process import ImageProcessor


class AppGUI:
    def __init__(self, master):
        self.panel = None
        self.p_image = None
        self.image = None
        self.blue = None
        self.green = None
        self.red = None

        self.entry_box = None
        self.load_image_button = None

        self.blue_slider = None
        self.green_slider = None
        self.red_slider = None
        self.vibrance_slider = None
        self.sharpness_slider = None
        self.contrast_slider = None
        self.brightness_slider = None

        self.flip_btn = None
        self.flip_window = None
        self.flip_window_status = 0

        self.blur_btn = None
        self.blur_window = None
        self.blur_window_status = 0

        self.camera_btn = None
        self.camera_window = None
        self.camera_window_status = 0
        self.camera_viewer = None

        self.edge_btn = None
        self.edge_window = None
        self.edge_window_status = 0

        self.resize_btn = None
        self.resize_window = None
        self.resize_window_status = 0

        self.crop_btn = None
        self.crop_window = None
        self.crop_window_status = 0
        self.top_left_x = None
        self.top_left_y = None
        self.bottom_right_x = None
        self.bottom_right_y = None

        self.find_edge_btn = None
        self.find_edge_window = None
        self.find_edge_window_status = 0

        self.about_btn = None
        self.about_window = None
        self.about_window_status = 0

        self.save_btn = None

        self.default_image = None
        self.image_stack = list()

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
        self.image = self.image_processor.img
        self.default_image = self.image
        self.image_stack.append(self.default_image)

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
        self.rotate_btn.place(x=1300, y=110)

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
                               command=self.crop, bg="#dddddd")
        self.crop_btn.configure(font=('consolas', 10, 'bold'), foreground='black')
        self.crop_btn.place(x=1300, y=285)

        self.edge_btn = Button(self.master, text='Edge Enhance', width=25,
                               command=self.edge, bg="#dddddd")
        self.edge_btn.configure(font=('consolas', 10, 'bold'), foreground='black')
        self.edge_btn.place(x=1300, y=320)

        self.reset_btn = Button(self.master, text='Reset', width=25,
                               command=self.reset, bg="#dddddd")
        self.reset_btn.configure(font=('consolas', 10, 'bold'), foreground='black')
        self.reset_btn.place(x=1300, y=355)

        self.camera_btn = Button(self.master, text='Camera', width=20,
                                 command=self.camera_window_open, bg="#dddddd")
        self.camera_btn.configure(font=('consolas', 10, 'bold'), foreground='black')
        self.camera_btn.place(x=50, y=680)

        self.load_image_button = Button(self.master, text="Load Image",
                                        command=self.load_image)
        self.load_image_button.place(x=50, y=25)

        self.entry_box = Entry(self.master, font=('consolas', 10, 'normal'), width=75)
        self.entry_box.place(x=130, y=27)

        self.save_btn = Button(self.master, text='Save', width=20,
                               command=self.save_image, bg="#dddddd")
        self.save_btn.configure(font=('consolas', 10, 'bold'), foreground='black')
        self.save_btn.place(x=210, y=680)

        self.about_btn = Button(self.master, text = 'About Us', width = 20,
                                command = self.about_us, bg = "#dddddd")
        self.about_btn.configure(font = ('consolas', 10, 'bold'), foreground = 'black')
        self.about_btn.place(x = 1325, y = 680)

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
            self.reset()
            self.display_image(self.default_image)
            self.image_stack.append(self.default_image)

    def process_brightness(self, position):
        # self.image_processor.img = self.get_top()
        self.image_processor.enhance_brightness(position)
        self.image_stack.append(self.image_processor.output_image)
        self.display_image(self.get_top())

    def process_contrast(self, position):
        # self.image_processor.img = self.get_top()
        self.image_processor.enhance_contrast(position)
        self.image_stack.append(self.image_processor.output_image)
        self.display_image(self.get_top())

    def process_sharpness(self, position):
        if self.image_processor.img:
            self.image_processor.enhance_sharpness(position)
            self.image_stack.append(self.image_processor.output_image)
            self.display_image(self.get_top())

    def process_vibrance(self, position):
        if self.image_processor.img:
            self.image_processor.enhance_vibrance(position)
            self.image_stack.append(self.image_processor.output_image)
            self.display_image(self.get_top())

    def process_red(self, position):
        if self.image_processor.img:
            self.image_processor.enhance_red(position)
            self.image_stack.append(self.image_processor.output_image)
            self.display_image(self.get_top())

    def process_green(self, position):
        if self.image_processor.img:
            self.image_processor.enhance_green(position)
            self.image_stack.append(self.image_processor.output_image)
            self.display_image(self.get_top())

    def process_blue(self, position):
        if self.image_processor.img:
            self.image_processor.enhance_blue(position)
            self.image_stack.append(self.image_processor.output_image)
            self.display_image(self.get_top())

    def rotate(self):
        if self.image_processor.img:
            self.image_processor.img = self.image
            self.image_processor.rotate()
            self.image = self.image_processor.output_image
            self.image_stack.append(self.image_processor.output_image)
            self.display_image(self.get_top())

    def flip_closing(self):
        self.flip_window_status = 0
        self.flip_window.destroy()

    def open_flip_window(self):
        self.flip_window_status += 1
        self.init_flip_window()

    def init_flip_window(self):
        if self.flip_window_status == 1:
            self.flip_window = Toplevel(self.master)
            self.flip_window.title("Flip")
            self.flip_window.resizable(False, False)
            self.flip_window.protocol("WM_DELETE_WINDOW", self.flip_closing)
            self.flip_window.geometry("200x100")

            horizontal_flip_btn = Button(self.flip_window, text="Horizontal Flip",
                                         command=self.flip_horizontal,
                                         width=20, bg="#dddddd")
            horizontal_flip_btn.pack(pady=10)

            vertical_flip_btn = Button(self.flip_window, text="Vertical Flip",
                                       command=self.flip_vertical,
                                       width=20, bg="#dddddd")
            vertical_flip_btn.pack(pady=10)

    def flip_horizontal(self):
        if self.image_processor.img:
            self.image_processor.img = self.image
            self.image_processor.flip_horizontal()
            self.image = self.image_processor.output_image
            self.image_stack.append(self.image_processor.output_image)
            self.display_image(self.get_top())

    def flip_vertical(self):
        if self.image_processor.img:
            self.image_processor.img = self.image
            self.image_processor.flip_vertical()
            self.image = self.image_processor.output_image
            self.image_stack.append(self.image_processor.output_image)
            self.display_image(self.get_top())

    def blur(self):  # call blur
        self.blur_window_status += 1
        self.init_blur_window()

    def blur_closing(self):
        self.blur_window_status = 0
        self.blur_window.destroy()

    def init_blur_window(self):
        if self.blur_window_status == 1:
            self.blur_window = Toplevel(self.master)
            self.blur_window.title("Blur")
            self.blur_window.resizable(False, False)
            self.blur_window.protocol("WM_DELETE_WINDOW", self.blur_closing)
            self.blur_window.geometry("200x225")

            convolution_blur_btn = Button(self.blur_window, text="Simple Blur",
                                          command=self.convolution,
                                          width=20, bg="#dddddd")
            convolution_blur_btn.pack(pady=10)

            box_blur_slider = Scale(self.blur_window, label="Box Blur", from_=0, to=10,
                                    orient=HORIZONTAL, length=200, resolution=1,
                                    command=self.box_blur, bg="#dddddd")
            box_blur_slider.set(0)
            box_blur_slider.pack(pady=10)

            gaussian_blur_slider = Scale(self.blur_window, label="Gaussian Blur", from_=0, to=10,
                                         orient=HORIZONTAL, length=200, resolution=1,
                                         command=self.gaussian_blur, bg="#dddddd")
            gaussian_blur_slider.set(0)
            gaussian_blur_slider.pack(pady=10)

    def convolution(self):
        if self.image_processor.img:
            self.image_processor.blur()
            self.image_stack.append(self.image_processor.output_image)
            self.display_image(self.get_top())

    def box_blur(self, position):
        if self.image_processor.img:
            self.image_processor.box_blur(position)
            self.image_stack.append(self.image_processor.output_image)
            self.display_image(self.get_top())

    def gaussian_blur(self, position):
        if self.image_processor.img:
            self.image_processor.gaussian_blur(position)
            self.image_stack.append(self.image_processor.output_image)
            self.display_image(self.get_top())

    def emboss(self):
        if self.image_processor.img:
            self.image_processor.emboss()
            self.image_stack.append(self.image_processor.output_image)
            self.display_image(self.get_top())

    def resize(self):
        self.resize_window_status += 1
        self.init_resize_window()

    def resize_closing(self):
        self.resize_window_status = 0
        self.resize_window.destroy()

    def init_resize_window(self):
        if self.resize_window_status == 1:
            self.resize_window = Toplevel(self.master)
            self.resize_window.title("Resize")
            self.resize_window.resizable(False, False)
            self.resize_window.protocol("WM_DELETE_WINDOW", self.resize_closing)
            self.resize_window.geometry("250x175")

            default_width, default_height = self.image.size
            self.width_scale = Scale(self.resize_window, label="Width", from_=0,
                                     to=default_width, orient=HORIZONTAL,
                                     command=self.update_width)
            self.height_scale = Scale(self.resize_window, label="Height", from_=0,
                                      to=default_height, orient=HORIZONTAL,
                                      command=self.update_height)

            self.width_scale.set(default_width)
            self.width_scale.pack(pady=10)

            self.height_scale.set(default_height)
            self.height_scale.pack(pady=10)

    def update_width(self, position):
        position = int(position)
        self.image_processor.img = self.image
        self.image_processor.resize_width(position)
        self.image = self.image_processor.output_image
        self.image_stack.append(self.image_processor.output_image)
        self.display_image(self.get_top())

    def update_height(self, position):
        position = int(position)
        self.image_processor.img = self.image
        self.image_processor.resize_height(position)
        self.image = self.image_processor.output_image
        self.image_stack.append(self.image_processor.output_image)
        self.display_image(self.get_top())

    def crop(self):
        self.crop_window_status += 1
        self.init_crop_window()

    def crop_closing(self):
        self.crop_window_status = 0
        self.crop_window.destroy()

    def init_crop_window(self):
        if self.crop_window_status == 1:
            self.crop_window = Toplevel(self.master)
            self.crop_window.title("Crop")
            self.crop_window.resizable(False, False)
            self.crop_window.protocol("WM_DELETE_WINDOW", self.crop_closing)
            self.crop_window.geometry("200x300")

            default_width, default_height = self.image.size
            self.top_left_x = Scale(self.crop_window, from_=0,
                                    to=default_width, orient=HORIZONTAL,
                                    command=self.update_crop)
            self.top_left_y = Scale(self.crop_window, from_=0,
                                    to=default_height, orient=HORIZONTAL,
                                    command=self.update_crop)
            self.bottom_right_x = Scale(self.crop_window, from_=0,
                                        to=default_width, orient=HORIZONTAL,
                                        command=self.update_crop)
            self.bottom_right_y = Scale(self.crop_window, from_=0,
                                        to=default_height, orient=HORIZONTAL,
                                        command=self.update_crop)
            self.top_left_x.set(0)
            self.top_left_x.pack(pady=10)
            self.top_left_y.set(0)
            self.top_left_y.pack(pady=10)
            self.bottom_right_x.set(default_width)
            self.bottom_right_x.pack(pady=10)
            self.bottom_right_y.set(default_height)
            self.bottom_right_y.pack(pady=10)

    def update_crop(self, _=None):
        top_left_x = self.top_left_x.get()
        top_left_y = self.top_left_y.get()
        bottom_right_x = self.bottom_right_x.get()
        bottom_right_y = self.bottom_right_y.get()
        self.image_processor.img = self.image
        self.image_processor.crop(top_left_x, top_left_y, bottom_right_x, bottom_right_y)
        self.image_stack.append(self.image_processor.output_image)
        self.display_image(self.get_top())

    def edge(self):
        self.find_edge_window_status += 1
        self.init_find_edge_window()
    def edge_closing(self):
        self.find_edge_window_status = 0
        self.find_edge_window.destroy()
    def init_find_edge_window(self):
        if self.find_edge_window_status == 1:
            self.find_edge_window = Toplevel(self.master)
            self.find_edge_window.title("Find Edge")
            self.find_edge_window.resizable(False, False)
            self.find_edge_window.protocol("WM_DELETE_WINDOW", self.edge_closing)
            self.find_edge_window.geometry("200x200")

            find_edge_btn = Button(self.find_edge_window, text="Black Background",
                                   command=self.find_edge,
                                   width=20, bg="#dddddd")
            find_edge_btn.pack(pady=10)
            contour_btn = Button(self.find_edge_window, text="White Background",
                                 command=self.contour,
                                 width=20, bg="#dddddd")
            contour_btn.pack(pady=10)

    def find_edge(self):
        self.image_processor.img = self.image
        self.image_processor.find_edge()
        self.image_stack.append(self.image_processor.output_image)
        self.display_image(self.get_top())

    def contour(self):
        self.image_processor.img = self.image
        self.image_processor.contour()
        self.image_stack.append(self.image_processor.output_image)
        self.display_image(self.get_top())

    def camera_window_open(self):
        camera_window = Toplevel(self.master)
        camera_window.title("Camera")
        self.camera_viewer = CameraViewer(camera_window, self)

    def show_captured_image(self, image_path):
        self.reset()
        self.image_processor.load_image('captures/captured_image.jpg')
        self.display_image(self.image_processor.img)
        self.image = self.image_processor.img
        self.default_image = self.image
        self.image_stack.append(self.default_image)
        self.entry_box.insert(END, image_path)

    def reset(self):
        self.brightness_slider.set(1)
        self.contrast_slider.set(1)
        self.sharpness_slider.set(1)
        self.vibrance_slider.set(1)
        self.red_slider.set(255)
        self.green_slider.set(255)
        self.blue_slider.set(255)

        def_width, def_height = self.default_image.size
        if (self.resize_window_status == 1):
            self.width_scale.set(def_width)
            self.height_scale.set(def_height)
            self.resize_window_status = 0
        if (self.crop_window_status == 1):
            self.top_left_x.set(0)
            self.top_left_y.set(0)
            self.bottom_right_x.set(def_width)
            self.bottom_right_y.set(def_height)
            self.crop_window_status = 0
        self.flip_window_status = 0
        self.blur_window_status = 0
        self.find_edge_window_status = 0
        self.image_stack = list()
        self.image_stack.append(self.default_image)
        self.image = self.default_image
        self.display_image(self.image_processor.img)

    def get_top(self):
        return self.image_stack[len(self.image_stack) - 1]

    def about_us(self):
        self.about_window_status += 1
        self.init_about_us_window()
    def about_closing(self):
        self.about_window_status = 0
        self.about_window.destroy()
    def init_about_us_window(self):
        if self.about_window_status == 1:
            self.about_window = Toplevel(self.master)
            self.about_window.title("About Us")
            self.about_window.resizable(False, False)
            self.about_window.protocol("WM_DELETE_WINDOW", self.about_closing)
            self.about_window.geometry("500x400")

            title_label = Label(self.about_window, text = "About Us",
                                font = ('consolas', 20, 'bold'))
            title_label.pack(pady = 10)

            about_text = (
                "Chúng tôi là nhóm 13 lớp 02 XLTTDPT PTIT\n"
                "Image Processor là sản phẩm của nhóm chúng tôi\n"
                "nhằm phục vụ cho bài tập lớp bộ môn Xử lý & truyền thông \nĐa phương tiện\n"
                "\n"
                "Nhóm 13:\n"
                "Nguyễn Đức Anh - B22DCPT009\n"
                "Bùi Hoàng Hải Đăng - B18DCPT057\n"
                "Nguyễn Lâm Vĩ - B20DCPT226\n"
                "Văn Thiên Phúc - B22DCPT237\n"
                "\n"
                "Giảng viên hướng dẫn: thầy Vũ Hữu Tiến\n"
                "\n"
                "Sản phẩm không mang mục đích thương mại\n"
            )
            about_label = Label(self.about_window, text = about_text,
                                font = ('conoslas', 12), justify='left')
            about_label.pack(padx = 20, pady = 10, anchor = 'w')


