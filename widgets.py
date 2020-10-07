from tkinter import (Tk, Menu, Button, Entry, Label, LabelFrame, OptionMenu, 
                    StringVar, END, messagebox as mb, Scrollbar, Listbox,EXTENDED,Frame,TOP, simpledialog, Toplevel,LEFT, N, Y, X)
import ui
import db
import datetime


ent_rashod_dohod = None
variable = None
options = None
text_result = None


def create_widget(window):
    '''функция создания кнопок и их активация
    '''
    global ent_rashod_dohod, variable, options, text_result

    options = db.get_articles_items()
    variable = StringVar(window)
    frame_1 = LabelFrame(window, text='Данные', height=300, width=600)
    frame_2 = LabelFrame(window, text='Списки расходов и доходов', height=500, width=700)
    frame_3 = LabelFrame(window, text='Результаты', height=300, width=600)
    # ширина экрана
    w = window.winfo_screenwidth()
    # высота экрана
    h = window.winfo_screenheight()   
    # значение по умолчанию
    variable.set(options[0])
    select_value = OptionMenu(frame_1, variable, *options)
    btn_rashod = Button(frame_1, text='Добавить расходы', command=add_type_rashod, font=('Arial', 12))
    btn_dohod = Button(frame_1, text='Добавить доходы', command=add_type_dohod, font=('Arial', 12))
    btn_append_item = Button(frame_1, text='Добавить свой вариант', command=create_mine_item, font=('Arial', 10))
    btn_result = Button(frame_2, text='Сохраниь результаты', font=('Arial', 12))
    btn_delete = Button(frame_2, text='Удалить', command=del_article, font=('Arial', 12))
    ent_rashod_dohod = Entry(frame_1, width=40, font=('Arial', 12))
    label_text_select = Label(frame_1, text='Выбирите нужный пункт расходов и доходов:', font=('Arial', 12))
    label_text_select_type = Label(frame_1, text='Введите сумму расходов или доходов:', font=('Arial', 12))
    label_text_result = Label(frame_1, text='Результаты:', font=('Arial', 12))
    label_text_dohod = Label(frame_1, text='Сумма доходов', font=('Arial', 12))
    label_text_summ = Label(frame_1, text='ИТОГО')
    label_text_mouth = Label(frame_3, text='Расходы за тeкущий месяц:', font=('Arial', 10))
    label_text_today = Label(frame_3, text='Расходы за день:', font=('Arial', 10))
    label_text_year = Label(frame_3, text='Расходы за год:', font=('Arial', 10))
    text_result = Listbox(frame_2, width=65, height=20, selectmode=EXTENDED, font=('Arial', 12))
    scroll = Scrollbar(frame_2, orient="vertical", command=text_result.yview)
    text_result.config(yscrollcommand=scroll.set)
    text_result_mouth = Listbox(frame_3, width=15, height=1, font=('Arial', 10))
    text_result_today = Listbox(frame_3, width=15, height=1, font=('Arial', 10))
    text_result_year = Listbox(frame_3, width=15, height=1, font=('Arial', 10))
    
    select_value.place(relx=0.03, rely=0.15)
    btn_rashod.place(relx=0.03, rely=0.70)
    btn_dohod.place(relx=0.33, rely=0.70)
    btn_delete.place(relx=0.5, rely=0.90)
    btn_append_item.place(relx=0.30,rely=0.15)
    btn_result.place(relx=0.7, rely=0.90)
   #label_text_result.place(relx=0.5, rely=0.05)
    text_result.place(relx=0.10, rely=0.01)
    text_result_mouth.place(relx=0.33, rely=0.03)
    text_result_today.place(relx=0.33, rely=0.12)
    text_result_year.place(relx=0.33, rely=0.21)
    ent_rashod_dohod.place(relx=0.03, rely=0.55)
    label_text_select.place(relx=0.03, rely=0.03)
    label_text_select_type.place(relx=0.03, rely=0.40)
    label_text_mouth.place(relx=0.03,rely=0.03)
    label_text_today.place(relx=0.03,rely=0.12)
    label_text_year.place(relx=0.03,rely=0.21)
    scroll.place(relx=0.96, rely=0.01, height=270)
    frame_1.place(relx=0.02, rely=0.02)
    frame_2.place(relx=0.47, rely= 0.02)
    frame_3.place(relx=0.02, rely= 0.50)


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
    select = list(text_result.curselection())
    select.reverse()
    for i in select:
        print(type(i))
        text_result.delete(i)
        articles.pop(i) 

    db.write_articles(articles)

def create_mine_item():
    '''Создаем окно, где можно
    добавлять свой пукт расходов или доходов
    '''
    global lbox, entry
    top = Toplevel()  
    #фокусируем наше окно
    #top.focus_set()
    #делаем его модальным(чтобы нельзя было переключиться на главное окно)
    #top.grab_set()
    #мы задаем приложению команду, что пока не будет закрыто окно top пользоваться другим окном будет нельзя.
    #top.wait_window()
    lbox = Listbox(top, selectmode=EXTENDED)
    lbox.pack(side=LEFT)
    scroll = Scrollbar(top, command=lbox.yview)
    scroll.pack(side=LEFT, fill=Y)
    lbox.config(yscrollcommand=scroll.set) 
    f = Frame(top)
    f.pack(side=LEFT, padx=10)
    entry = Entry(f)
    entry.pack(anchor=N)
    item_add = Button(f, text="Добавить", command=append_list_item)
    item_add.pack(fill=X)
    item_del = Button(f, text="Удалить", command=del_list_item)
    item_del.pack(fill=X)
    list_save = Button(f, text="Сохранить", command=db.write_article_items)
    list_save.pack(fill=X)
    update_article_option()


def append_list_item():
    '''добавляем в окно с нашим списком новое значение
    расхода или дохода
    '''
    lbox.insert(END, entry.get())
    entry.delete(0, END)


def add_list_item():
    '''добавляем в наш основной список,новые добавленные
    пользователем значения, которые будут записаны в наш файл  
    '''
    articles_items = db.get_articles_items()
    article_item = lbox.get(0, END)
    for item in article_item:
        if (item in articles_items) == False:
            articles_items.append(item)
    return articles_items
1

def update_article_option():
    '''выводит наши значения пуков 
    расходов и доходов в окно
    '''
    lbox.delete(0, END)
    articles = db.get_articles_items()
    for article in articles:
        lbox.insert(0, article)


def del_list_item():
    '''удаляем не нужный пункт расходов или доходов
    '''
    select = list(lbox.curselection())
    select.reverse()
    for i in select:
        lbox.delete(i) 
    db.write_article_items()       
    
    
    
