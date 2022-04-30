import math
from tkinter import simpledialog, messagebox, Tk
import tkinter as tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    rob = simpledialog.askstring(title='birthday', prompt='what date is your birthday? mm/dd')

    if rob=='04/29':
        messagebox.showinfo(title='birthday', message='happy birthday!')
    else:
        messagebox.showinfo(title='Unbirtday', message='Have a merry UNbirthday')
