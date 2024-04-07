from tkinter import *

from PIL import Image, ImageFilter, ImageEnhance


class ImageProcessor:
    def __init__(self):
        self.img = None
        self.output_image = None

    def save_image(self, filename):
        if self.output_image:
            self.output_image.save(filename)

    def load_image(self, filename):
        self.img = Image.open(filename)
        w, h = self.img.size
        self.img = self.img.resize((int(w * 600 / h), 600))

    def enhance_brightness(self, position):
        position = float(position)
        enhancer = ImageEnhance.Brightness(self.img)
        self.output_image = enhancer.enhance(position)

    def enhance_contrast(self, position):
        position = float(position)
        enhancer = ImageEnhance.Contrast(self.img)
        self.output_image = enhancer.enhance(position)

    def enhance_sharpness(self, position):
        position = float(position)
        enhancer = ImageEnhance.Sharpness(self.img)
        self.output_image = enhancer.enhance(position)

    def enhance_vibrance(self, position):
        position = float(position)
        enhancer = ImageEnhance.Color(self.img)
        self.output_image = enhancer.enhance(position)

    def extract_color(self):
        r, g, b = self.img.split()
        r_data = list(r.getdata())
        g_data = list(g.getdata())
        b_data = list(b.getdata())
        return r_data, g_data, b_data

    def enhance_red(self, position):
        position = int(position)
        r, g, b = self.img.split()
        r = r.point(lambda i: i * (position / 255))
        out = Image.merge('RGB', (r, g, b))
        self.output_image = out

    def enhance_green(self, position):
        position = float(position)
        r, g, b = self.img.split()
        g = g.point(lambda i: i * (position / 255))
        out = Image.merge('RGB', (r, g, b))
        self.output_image = out

    def enhance_blue(self, position):
        position = float(position)
        r, g, b = self.img.split()
        b = b.point(lambda i: i * (position / 255))
        out = Image.merge('RGB', (r, g, b))
        self.output_image = out

    def rotate(self):
        self.img = self.img.rotate(90)
        self.output_image = self.img

    def flip_horizontal(self):
        self.img = self.img.transpose(Image.FLIP_LEFT_RIGHT)
        self.output_image = self.img

    def flip_vertical(self):
        self.img = self.img.transpose(Image.FLIP_TOP_BOTTOM)
        self.output_image = self.img

    def blur(self):
        self.img = self.img.filter(ImageFilter.BLUR)
        self.output_image = self.img
    def box_blur(self, position):
        position = float(position)
        blured = self.img.filter(ImageFilter.BoxBlur(position))
        self.output_image = blured

    def gaussian_blur(self, position):
        position = float(position)
        blured = self.img.filter(ImageFilter.GaussianBlur(position))
        self.output_image = blured

    def emboss(self):
        self.img = self.img.filter(ImageFilter.EMBOSS)
        self.output_image = self.img

    def resize_width(self, position):
        position = float(position)
        w, h = self.img.size
        output_img = self.img.resize((int(w*position/100), h))
        self.output_image = output_img
    def resize_height(self, position):
        position = float(position)
        w, h = self.img.size
        output_img = self.img.resize((w, int(h*position/100)))
        self.output_image = output_img

    def crop(self):
        self.img = self.img.crop((100, 100, 400, 400))
        self.output_image = self.img

    def edge(self):
        self.img = self.img.filter(ImageFilter.FIND_EDGES)
        self.output_image = self.img
