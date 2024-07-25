import tkinter as tk
import time

IDLE_IMAGE = "idle.gif"
RUNNING_IMAGE = "running.gif"

class Pet:
    def __init__(self):
        self.speed = 2
        self.is_moving = False

        self.start_x = 0
        self.start_y = 683 # you must change this value because it depends on your screen size

        self.x = self.start_x
        self.y = self.start_y

        self.window = tk.Tk()
        self.setup_window()

        self.images = self.load_images(IDLE_IMAGE)
        self.frame_index = 0
        self.current_image = self.images[self.frame_index]

        self.label = tk.Label(self.window, bd=0, bg='black')
        self.label.configure(image=self.current_image)
        self.label.pack()

        self.last_update_time = time.time()

        self.window.bind("<Button-1>", self.on_click)

        self.window.after(0, self.update)
        self.window.mainloop()

    def setup_window(self):
        self.window.config(highlightbackground='black')
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
        self.window.wm_attributes('-transparentcolor', 'black')
        self.window.geometry(f'128x128+{self.x}+{self.y}')

    def load_images(self, path):
        return [tk.PhotoImage(file=path, format=f'gif -index {i}') for i in range(4)]

    def on_click(self, event):
        self.is_moving = not self.is_moving
        image_path = RUNNING_IMAGE if self.is_moving else IDLE_IMAGE
        self.images = self.load_images(image_path)
        

    def update(self):
        if self.is_moving:
            self.x += self.speed

        if time.time() - self.last_update_time > 0.12:

            self.last_update_time = time.time()
            self.frame_index = (self.frame_index + 1) % len(self.images)
            self.current_image = self.images[self.frame_index]

        self.window.geometry(f'86x132+{self.x}+{self.y}')
        self.label.configure(image=self.current_image)
        self.label.pack()

        self.window.after(20, self.update)

if __name__ == "__main__":
    Pet()