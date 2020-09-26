''' Программа контроля 
рахода семейного бюджета'''
from tkinter import Tk
 
def create_window():  
    window = Tk()
    # ширина экрана
    w = window.winfo_screenwidth()
    # высота экрана
    h = window.winfo_screenheight() 
    window.title('Бюджет семьи')
    window.geometry('{}x{}'.format(w, h))
    return window
 
