import math
from tkinter import simpledialog, messagebox, Tk
import tkinter as tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    billy = 0
    for i in range(13):
        billy=billy+1
        messagebox.showinfo(title='age', message=billy)
