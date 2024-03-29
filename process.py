import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter, ImageEnhance
from tkinter.filedialog import askopenfilename
import os
class ImageProcessor:
    def __init__(self):
        self.img = None
        self.output_image = None

    def load_image(self, filename):
        self.img = Image.open(filename)
        w, h = self.img.size
        self.img = self.img.resize((int(w*600/h), 600))

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
        r = r.point(lambda i: i*(position/255))
        out = Image.merge('RGB', (r,g,b))
        self.output_image = out

    def enhance_green(self, position):
        position = float(position)
        r, g, b = self.img.split()
        g = g.point(lambda i: i*(position/255))
        out = Image.merge('RGB', (r, g, b))
        self.output_image = out

    def enhance_blue(self, position):
        position = float(position)
        r, g, b = self.img.split()
        b = b.point(lambda i: i*(position/255))
        out = Image.merge('RGB', (r, g, b))
        self.output_image = out

    def rotate(self):
        self.img = self.img.rotate(90)
        self.output_image = self.img

    def flip(self):
        self.img = self.img.transpose(Image.FLIP_LEFT_RIGHT)
        self.output_image = self.img

    def blur(self):
        self.img = self.img.filter(ImageFilter.BLUR)
        self.output_image = self.img

    def emboss(self):
        self.img = self.img.filter(ImageFilter.EMBOSS)
        self.output_image = self.img

    def resize(self):
        self.img = self.img.resize((300, 300))
        self.output_image = self.img

    def crop(self):
        self.img = self.img.crop((100, 100, 400, 400))
        self.output_image = self.img

    def edge(self):
        self.img = self.img.filter(ImageFilter.FIND_EDGES)
        self.output_image = self.img
