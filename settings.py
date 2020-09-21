''' Программа контроля 
рахода семейного бюджета'''
from tkinter import Tk, Menu, Button, Entry, Label, LabelFrame, OptionMenu, StringVar, END, messagebox as mb, Text, Scrollbar,Listbox
import datetime
import widgets
import db

tasks = db.read_file()

def add_type_rashod():
    '''добавляем в спикок словарь с нашими расходами
    '''
    #перехватываем ошибку неправильного ввода
    try:
        result_cost = int(widgets.ent_rashod_dohod.get())

    except ValueError as err:
        mb.showerror('Ошибка','Должно быть введено число!')
        print (err)
    new_task = {
            'cost':result_cost,
            'type_item': '-',
            'type_value': widgets.variable.get(),
            'data_create': datetime.date.today()
            }
    widgets.ent_rashod_dohod.delete(0, END)
    tasks.append(new_task)
    db.write_file() 
 

               
def add_type_dohod():
    '''добавляем в список словарь с нашими доходами
    '''
    #перехватываем ошибку неправильного ввода 
    try:
        result_cost = int(widgets.ent_rashod_dohod.get())

    except ValueError:
        mb.showerror('Ошибка','Должно быть введено число!')
    
    new_task = {
            'cost': result_cost,
            'type_item': '+',
            'type_value': widgets.variable.get(),
            'data_create': datetime.date.today()
            }
    widgets.ent_rashod_dohod.delete(0, END)
    tasks.append(new_task)
    db.write_file()   
    

def print_result():
    
    for task in tasks:
        for key, value in task.items():
            s = '{} --> {}'.format(key, value)
            widgets.text_result.insert(0 ,s)
       


def del_article():
    select = list(widgets.text_result.curselection())
    select.reverse()
    for i in select:
        widgets.text_result.delete(i)


 
 