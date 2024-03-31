import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import cv2
import os

class CameraViewer:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.master.geometry("1300x600")
        self.master.configure(bg='grey')
        self.master.title("Camera Viewer")
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)  # Handle window close event

        self.panel = Label(self.master)
        self.panel.pack(padx=10, pady=10, side=LEFT)

        self.captured_image_label = Label(self.master)
        self.captured_image_label.pack(padx=10, pady=10, side = RIGHT)

        self.capture_button = Button(self.master, text="Capture", command=self.capture_image)
        self.capture_button.place(x = 675, y = 20)

        self.confirm_button = Button(self.master, text="Confirm", command=self.confirm_image)
        self.confirm_button.pack_forget()  # Initially hidden
        self.captured_image = None

        self.video_stream = cv2.VideoCapture(0)  # Open the camera
        self.update_camera()

    def update_camera(self):
        ret, frame = self.video_stream.read()  # Read a frame from the camera
        if ret:
            # Convert frame from BGR to RGB format
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convert frame to PIL Image
            img = Image.fromarray(frame)
            # Convert PIL Image to PhotoImage
            imgtk = ImageTk.PhotoImage(image=img)
            # Display the image
            self.panel.imgtk = imgtk
            self.panel.config(image=imgtk)
        # Schedule the next update after 10 ms
        self.master.after(10, self.update_camera)

    def capture_image(self):
        ret, frame = self.video_stream.read()  # Read a frame from the camera
        if ret:
            # Convert frame from BGR to RGB format
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Convert frame to PIL Image
            self.captured_image = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=self.captured_image)
            # Display the captured image
            self.captured_image_label.config(image=imgtk)
            self.captured_image_label.image = imgtk
            # Enable the confirm button
            self.confirm_button.place(x = 605, y =20)

    def confirm_image(self):
        self.save_and_close_window()

    def on_closing(self):
        self.save_and_close_window()

    def save_and_close_window(self):
        if self.captured_image:
            # Save the captured image
            self.captured_image_path = "captures/captured_image.jpg"
            os.makedirs("captures", exist_ok=True)  # Create the "captures" directory if it doesn't exist
            self.captured_image.save(self.captured_image_path)
            # Show the captured image in the main window
            self.app.show_captured_image(self.captured_image_path)
        self.video_stream.release()  # Release the camera
        self.master.destroy()  # Close the camera window