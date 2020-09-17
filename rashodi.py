''' Программа контроля 
рахода семейного бюджета'''
from tkinter import Tk, Menu, Button, Entry, Label, LabelFrame, OptionMenu, StringVar, END, messagebox as mb, Text, Scrollbar
import json
import os
import datetime
import sys



#переменная названия файла
file_task = 'data_file.txt'
#формат даты
date_format = '%Y.%m.%d '
#список доходов
lst_dohod = []
#список расходов
lst_rashod = []
window = None
ent_rashod = None
ent_dohod = None
dt_start  = datetime.date.today().strftime(date_format)


if os.path.exists(file_task):
    #если файл существует
    #загружаем список расходов
    with open (file_task, encoding='utf-8') as f:
        try:
            #перехватываем ошибки
            tasks = json.load(f)

        except Exception:
            tasks = []        
else:
    tasks =[]


def clear_list():
    lst_rashod.clear()
    lst_dohod.clear()

    
def result():
    '''функция расчета расходов и доходов
    '''
    for task in tasks:
        if '-' in task['type_item']:
            lst_rashod.append(task['cost'])
        else:
            lst_dohod.append(task['cost'])

    print_result()      


def add_type_rashod():
    '''добавляем в спикок словарь с нашими расходами
    '''
    #перехватываем ошибку неправильного ввода
    try:
        new_task = {
            'cost':int(ent_rashod_dohod.get()),
            'type_item': '-',
            'type_value': variable.get(),
            'data_create': dt_start
            }
        ent_rashod_dohod.delete(0, END)
        for task in tasks:
            if new_task['type_value'] in task['type_value']:
                new_task['cost'] += task['cost']
        
        tasks.append(new_task) 
        write_file()  
    except ValueError:
        mb.showerror('Ошибка','Должно быть введено число!')

    
               


def add_type_dohod():
    '''добавляем в список словарь с нашими доходами
    '''
    #перехватываем ошибку неправильного ввода
    try:
        new_task = {
            'cost':int(ent_rashod_dohod.get()),
            'type_item': '+',
            'type_value': variable.get(),
            'data_create': dt_start 
            }
        ent_rashod_dohod.delete(0, END)
        for task in tasks:
            if new_task['type_value'] in task['type_value']:
                new_task['cost'] += task['cost']
        
        tasks.append(new_task)
        write_file()
    
    except ValueError:
        mb.showerror('Ошибка','Должно быть введено число!')

    ent_rashod_dohod.delete(0, END)   


def print_result():
    
    for task in tasks:
        for key in task:
            value = str(task[key])  + ' ' 
            text_result.insert(1.0 ,value)
    
    clear_list()


def create_widget():
    '''функция создания кнопок и их активация
    '''
    global ent_rashod_dohod, variable, options, text_result

    options =[
        'продукты',
        'авто и ГСМ',
        'жкх',
        'одежда',
        'зарплата', 
        'премия или подарок', 
        'мебель', 
        'крупная бытовая техника',
        'кафе, рестораны',
        'прочие расходы'
        ]
    variable = StringVar(window)
    # значение по умолчанию
    variable.set(options[0])
    select_value = OptionMenu(window, variable, *options)
    btn_rashod = Button(window, text='Добавить расходы', command=add_type_rashod)
    btn_dohod = Button(window, text='Добавить доходы', command=add_type_dohod)
    btn_result = Button(window,text='Рассчитать результат', command=print_result)
    ent_rashod_dohod = Entry(window, width=40)
    label_text_select = Label(text='Выбирите нужный пункт расходов и доходов:')
    label_text_select_type = Label(text='Введите сумму расходов или доходов:')
    label_text_result = Label(text='Результаты:',)
    label_text_dohod = Label(text='Сумма доходов')
    label_text_summ = Label(text='ИТОГО')
    text_result = Text(width=50,height=10)
    scroll = Scrollbar(window, orient="vertical",command=text_result.yview)
    text_result.config(yscrollcommand=scroll.set)

    select_value.place(x=1, y=25)
    btn_rashod.place(x=1, y=110)
    btn_dohod.place(x=140, y=110)
    btn_result.place(x=1,y=400)
    label_text_result.place(x=1, y=200)
    text_result.place(x=1, y=230)
    ent_rashod_dohod.place(x=1,y=85)
    label_text_select.place(x=1,y=0)
    label_text_select_type.place(x=1,y=60)
    scroll.place(x=400,y=230)


def write_file():
    '''функция загрузки в файл 
        наших значений 
    '''
    with open (file_task, 'w') as f:
        data = json.dump(tasks, f)

    print_result()     

 
def main():
    global window
    window = Tk()
    window.title('Бюджет семьи')
    window.geometry('600x480')
    
    create_widget()

    window.mainloop()


#frame_1 = tk.Frame(master = window, width = 150 ,height = 150, bg = 'black')
#frame_1.grid(column = 2, row = 2)
#menu = Menu(window)
#new_item = Menu(menu, tearoff = 0)
#new_item_1 = Menu(menu, tearoff = 0)
#menu.add_cascade(label = 'Меню', menu = new_item)
'''Добавляем пункты в Меню'''
#new_item.add_command(label = 'Создать новый бюджет')
#new_item.add_command(label = 'Сохранить файл')
#new_item.add_command(label = 'Открыть файл')
#window.config(menu = menu)
#menu.add_cascade(label = 'Информация',menu = new_item_1)
'''Добавляем пункты в меню "Информация"'''
#new_item_1.add_command(label = 'Состояние расходов за  месяц')
#new_item_1.add_command(label = 'Состояние расходов на год')
    
    
main()

 