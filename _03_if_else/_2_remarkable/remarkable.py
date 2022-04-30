import math
from tkinter import simpledialog, messagebox, Tk
import tkinter as tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    rob=simpledialog.askstring(title='yes', prompt='what is your name?')
    if rob=='James':
        messagebox.showinfo(title='coolio', message='you are strong')
    if rob=='Will':
        messagebox.showinfo(title='cooli', message='you have cool glasses')
    if rob=='Jeremy':
        messagebox.showinfo(title='not cool', message='you are not cool')

