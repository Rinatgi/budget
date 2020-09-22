''' Программа контроля 
рахода семейного бюджета'''
from tkinter import  END, messagebox as mb
import datetime
import widgets
import db

tasks = db.get_article()

def add_type_rashod():
    '''добавляем в спикок словарь с нашими расходами
    '''
    #перехватываем ошибку неправильного ввода
    try:
        result_cost = int(widgets.ent_rashod_dohod.get())

    except ValueError as err:
        mb.showerror('Ошибка','Должно быть введено число!')
    new_task = {
            'cost':result_cost,
            'type_item': '-',
            'type_value': widgets.variable.get(),
            'data_create': datetime.datetime.today()
            }
    #widgets.ent_rashod_dohod.delete(0, END)
    tasks.append(new_task)
    db.write_article() 
 

               
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
            'data_create': datetime.datetime.today()
            }
    #widgets.ent_rashod_dohod.delete(0, END)
    tasks.append(new_task)
    db.write_article()   
    

def print_article():
    '''вводим наши все записи
        в окно
    '''
    for task in tasks:
        for key, value in task.items():
            s = '{:30} {}'.format(key, value)
            widgets.text_result.insert(0 ,s)
       


def del_article():
    '''удалаляем в окне не нужный
        пунк дохода или расхода.
    '''
    select = list(widgets.text_result.curselection())
    select.reverse()
    for i in select:
        widgets.text_result.delete(i)
    remaining_articles = widgets.text_result.get(0, END)  
     
    print(remaining_articles)  


 
 