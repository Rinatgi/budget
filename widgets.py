from tkinter import (Tk, Menu, Button, Entry, Label, LabelFrame, OptionMenu, 
                    StringVar, END, messagebox as mb, Scrollbar, Listbox,EXTENDED,
                    Frame,TOP, simpledialog, Toplevel,LEFT, N, Y, X
                    )
import ui
import db
import datetime
import category
import setting
import result
from tkinter.ttk import Combobox
import sort_article
import cal
import conftest



ent_rashod_dohod = None
variable = None
options = None
text_result = None
frame_2 = None
label_date_vision = None


def create_widget(window):
    '''функция создания кнопок и их активация
    '''
    global ent_rashod_dohod, variable, options, text_result, select_value, frame_2, label_date_vision, combo_category

    options = db.get_articles_category()
    variable = StringVar(window)
    frame_1 = LabelFrame(window, text='Данные', height=300, width=600)
    frame_2 = LabelFrame(window, text='Списки расходов и доходов', height=500, width=700)
    frame_3 = LabelFrame(window, text='Результаты', height=200, width=700)
    combo_category = Combobox(frame_2, values=options, postcommand=sort_article.refresh_sort_category)
    combo_type = Combobox(frame_2)
    combo_type['values'] = ['Все', 'Расходы', 'Доходы'] 
    combo_category.current(0)
    combo_type.current(0)
    # ширина экрана
    w = window.winfo_screenwidth()
    # высота экрана
    h = window.winfo_screenheight()   
    # значение по умолчанию
    variable.set(options[0])
    select_value = OptionMenu(frame_1, variable, *options)
    btn_rashod = Button(frame_1, text='Добавить расходы', command=add_type_rashod, font=('Arial', 12))
    btn_dohod = Button(frame_1, text='Добавить доходы', command=add_type_dohod, font=('Arial', 12))
    btn_append_item = Button(frame_1, text='Добавить свой вариант', command=category.create_window_category_change, font=('Arial', 10))
    btn_result = Button(frame_2, text='Oтсортировать', font=('Arial', 12), command=sort_article.sort_article_list)
    btn_delete = Button(frame_2, text='Удалить', command=del_article, font=('Arial', 12))
    btn_demo = Button(frame_2, text='Демо', command=conftest.request_user)
    btn_calendar = Button(frame_2, text='Выберите дату', command=cal.create_window_calendar)
    ent_rashod_dohod = Entry(frame_1, width=40, font=('Arial', 12))
    label_text_select = Label(frame_1, text='Выбирите нужный пункт расходов и доходов:', font=('Arial', 12))
    label_text_select_type = Label(frame_1, text='Введите сумму расходов или доходов:', font=('Arial', 12))
    label_text_result = Label(frame_1, text='Результаты:', font=('Arial', 12))
    label_text_dohod = Label(frame_1, text='Сумма доходов', font=('Arial', 12))
    label_text_summ = Label(frame_1, text='ИТОГО')
    label_text_expence = Label(frame_3, text='Расходы', font=('Arial', 12))
    label_text_income = Label(frame_3, text='Доходы', font=('Arial', 12))
    label_text_all = Label(frame_3, text='Итого', font=('Arial', 12))
    label_date_vision = Label(frame_2, text="", font=('Arial', 12))
    text_result = Listbox(frame_2, width=65, height=20, selectmode=EXTENDED, font=('Arial', 12))
    scroll = Scrollbar(frame_2, orient="vertical", command=text_result.yview)
    text_result.config(yscrollcommand=scroll.set)
    text_result_expence = Listbox(frame_3, width=15, height=1, font=('Arial', 13))
    text_result_income = Listbox(frame_3, width=15, height=1, font=('Arial', 13))
    text_result_all = Listbox(frame_3, width=15, height=1, font=('Arial', 13))
    
    select_value.place(relx=0.03, rely=0.15)
    btn_rashod.place(relx=0.03, rely=0.70)
    btn_dohod.place(relx=0.33, rely=0.70)
    btn_delete.place(relx=0.55, rely=0.90)
    btn_append_item.place(relx=0.30,rely=0.15)
    btn_result.place(relx=0.75, rely=0.90)
    btn_demo.place(relx=0.35, rely=0.90)
    btn_calendar.place(relx=0.80, rely=0.02 )
    text_result.place(relx=0.10, rely=0.09)
    text_result_expence.place(relx=0.33, rely=0.03)
    text_result_income.place(relx=0.33, rely=0.18)
    text_result_all.place(relx=0.33, rely=0.33)
    ent_rashod_dohod.place(relx=0.03, rely=0.55)
    label_text_select.place(relx=0.03, rely=0.03)
    label_text_select_type.place(relx=0.03, rely=0.40)
    label_text_expence.place(relx=0.03,rely=0.03)
    label_text_income.place(relx=0.03,rely=0.18)
    label_text_all.place(relx=0.03,rely=0.33)
    label_date_vision.place(relx=0.62, rely=0.02)
    scroll.place(relx=0.95, rely=0.09, height=380)
    frame_1.place(relx=0.02, rely=0.02)
    frame_2.place(relx=0.47, rely= 0.02)
    frame_3.place(relx=0.47, rely= 0.70)
    combo_category.place(relx=0.10, rely=0.02)
    combo_type.place(relx=0.36, rely=0.02)
    result.show_result(text_result_income, text_result_expence, text_result_all)

def add_type_rashod():
    '''добавляем в спикок словарь с нашими расходами
    '''
    articles = db.get_articles()
    #перехватываем ошибку неправильного ввода
    try:
        result_cost = int(ent_rashod_dohod.get())

    except ValueError as err:
        mb.showerror('Ошибка', 'Должно быть введено число!')
    new_article = {
            'cost':result_cost,
            'type_item': '-',
            'type_value': variable.get(),
            'data_create': datetime.datetime.today()
            }
    #widgets.ent_rashod_dohod.delete(0, END)
    articles.append(new_article)
    db.write_articles(articles)
    update_article_list() 
    

def add_type_dohod():
    '''добавляем в список словарь с нашими доходами
    '''
    articles = db.get_articles()
    #перехватываем ошибку неправильного ввода 
    try:
        result_cost = int(ent_rashod_dohod.get())

    except ValueError:
        mb.showerror('Ошибка', 'Должно быть введено число!')
    
    new_article = {
            'cost': result_cost,
            'type_item': '+',
            'type_value': variable.get(),
            'data_create': datetime.datetime.today()
            }
    #widgets.ent_rashod_dohod.delete(0, END)
    articles.append(new_article)
    db.write_articles(articles)   
    update_article_list()


def update_article_list():
    '''выводим наши все записи
        в окно
    ''' 
    text_result.delete(0, END)
    index = 0 
    articles = db.get_articles()
    for article in articles:
        s = '{cost} руб. {type_item} {type_value} {data_create}'.format(**article)
        text_result.insert(0, s)
        if article['type_item'] == '-':
            text_result.itemconfig(index, bg='red')
            
        else:
            text_result.itemconfig(index, bg='green')                
    index += 1


def del_article():
    '''удалаляем в окне не нужный
        пунк дохода или расхода.
    '''
    articles = db.get_articles()
    select = list(text_result.get())
    select.reverse()
    for i in select:
        text_result.delete(i)
        articles.pop(i) 

    db.write_articles(articles) 


def update_option_category_list(write_articles):
    '''обновляет список выбора значений расхода и дохода
    '''
    select_value['menu'].delete(0 , END)
    
    for _category in write_articles:
        select_value.children["menu"].add_command(
            label=_category,command=lambda veh=_category: options.set(veh)
        )


def show_date(select_date):
    '''показывает выбранную дату для сортировки
    '''
    label_date_vision.config(text=select_date.strftime(setting.DATE_FORMAT))
