
import math
from tkinter import simpledialog, messagebox, Tk
import tkinter as tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    kyle=0
    rob = simpledialog.askstring(title='what am I?', prompt='What has cities but no houses forests but no trees and water but no fish?')
    bob = simpledialog.askstring(title='am what I?', prompt='If eleven plus two equals one, what does nine plus five equal?')
    bill = simpledialog.askstring(title='I what am?', prompt='You live in a one story house made entirely of redwood. What color would the stairs be?')
    if bill=='there are no stairs':
        kyle=kyle+1
    if bob=='2':
        kyle=kyle+1
    if rob=='map':
        kyle=kyle+1
    print(kyle)



"""""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
