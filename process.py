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
        rotate_img = self.img.rotate(90)
        self.output_image = rotate_img

    def flip_horizontal(self):
        flip_img = self.img.transpose(Image.FLIP_LEFT_RIGHT)
        self.output_image = flip_img

    def flip_vertical(self):
        flip_img = self.img.transpose(Image.FLIP_TOP_BOTTOM)
        self.output_image = flip_img

    def blur(self):
        blur_img = self.img.filter(ImageFilter.BLUR)
        self.output_image = blur_img
    def box_blur(self, position):
        position = float(position)
        blured = self.img.filter(ImageFilter.BoxBlur(position))
        self.output_image = blured

    def gaussian_blur(self, position):
        position = float(position)
        blured = self.img.filter(ImageFilter.GaussianBlur(position))
        self.output_image = blured

    def emboss(self):
        emboss_img = self.img.filter(ImageFilter.EMBOSS)
        self.output_image = emboss_img

    def resize_width(self, position):
        width, height = self.img.size
        resized_image = self.img.resize((position, height), Image.LANCZOS)
        self.output_image = resized_image
    def resize_height(self, position):
        width, height = self.img.size
        resized_image = self.img.resize((width, position), Image.LANCZOS)
        self.output_image = resized_image

    def crop(self, x1, y1, x2, y2):
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        crop_img = self.img.crop((x1, y1, x2, y2))
        self.output_image = crop_img

    def find_edge(self):
        find_edge_img = self.img.filter(ImageFilter.FIND_EDGES)
        self.output_image = find_edge_img
    def contour(self):
        contour_img = self.img.filter(ImageFilter.CONTOUR)
        self.output_image = contour_img
