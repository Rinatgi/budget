import db
from tkinter import (Button, Entry, Label, LabelFrame, OptionMenu, 
                    StringVar, END, messagebox as mb, Scrollbar, Listbox,EXTENDED,Frame,TOP, simpledialog, 
                    Toplevel,LEFT, N, Y, X, Menu
                    )
import setting

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
    lbox_var = StringVar(top)
    new_category = StringVar(top)
    lbox = Listbox(top, selectmode=EXTENDED)
    lbox.pack(side=LEFT)
    scroll = Scrollbar(top, command=lbox.yview)
    scroll.pack(side=LEFT, fill=Y)
    lbox.config(yscrollcommand=scroll.set) 
    f = Frame(top)
    f.pack(side=LEFT, padx=10)
    entry = Entry(f)
    entry.pack(anchor=N)
    category_add = Button(f, text="Добавить", command=append_category)
    category_add.pack(fill=X)
    category_del = Button(f, text="Удалить", command=del_category)
    category_del.pack(fill=X)
    update_category_list()


def append_category():
    ''' добавляем в окно с нашим списком новое значение
        расхода или дохода
    '''    
    lbox.insert(END, entry.get())
    new_category = lbox.get(END)
    add_list_category(new_category)




def add_list_category(new_category):
    '''добавляем в наш основной список,новые добавленные
    пользователем значения, которые будут записаны в наш файл  
    '''
    articles_category = db.get_articles_category()
    if new_category not in articles_category:
        articles_category.append(new_category)
    elif new_category == '':
        mb.showerror('Ошибка', 'Вы не ввели значение!')
    else:
        mb.showerror('Ошибка', 'Такая категория уже есть!')            
    db.write_article_category(articles_category)
    update_category_list()
    


def update_category_list():
    '''выводит наши значения пунктов 
    расходов и доходов в окно
    '''
    lbox.delete(0, END)
    articles_category = db.get_articles_category() + setting.CATEGORY
    for article in articles_category:
        lbox.insert(0, article)    


def del_category():
    '''удаляем не нужный пункт расходов или доходов
    '''
    del_category_article = []
    articles_category_write = db.get_articles_category()
    articles_category = db.get_articles_category() + setting.CATEGORY
    select = list(lbox.curselection())
    select.reverse()
    for i in select:
        lbox.delete(i)
        del_category = articles_category.pop(i)
        del_category_article.append(del_category)
    print(del_category_article)    
    for category in del_category_article:
        articles_category_write.remove(category)
    db.write_article_category(articles_category_write)                