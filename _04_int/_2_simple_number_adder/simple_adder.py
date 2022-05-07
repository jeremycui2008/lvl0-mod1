

"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
import math
from tkinter import simpledialog, messagebox, Tk
import tkinter as tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    rob = simpledialog.askinteger(title='first', prompt='select a first number')
    bob = simpledialog.askinteger(title='second', prompt='select a second number')
    bill=rob+bob
    print(bill)
