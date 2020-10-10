import db
from tkinter import (Button, Entry, Label, LabelFrame, OptionMenu, 
                    StringVar, END, messagebox as mb, Scrollbar, Listbox,EXTENDED,Frame,TOP, simpledialog, Toplevel,LEFT, N, Y, X)


def create_window_category_change():
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
    item_add = Button(f, text="Добавить", command=append_category)
    item_add.pack(fill=X)
    item_del = Button(f, text="Удалить", command=del_list_item)
    item_del.pack(fill=X)
    list_save = Button(f, text="Сохранить", command=db.write_article_items)
    list_save.pack(fill=X)
    update_category_list()


def append_category():
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
    articles_items.clear()
    article_item = lbox.get(0, END)
    for item in article_item:
        if (item in articles_items) == False:
            articles_items.append(item)
    return articles_items
    update_category_list()

def update_category_list():
    '''выводит наши значения пунктов 
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