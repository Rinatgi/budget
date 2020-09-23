from tkinter import Tk, Menu, Button, Entry, Label, LabelFrame, OptionMenu, StringVar, END, messagebox as mb, Scrollbar, Listbox,EXTENDED
import ui
import article
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
    btn_result = Button(window,text='Сохраниь результаты')
    btn_delete = Button(window,text='Удалить',command=article.del_article)
    ent_rashod_dohod = Entry(window, width=40)
    label_text_select = Label(text='Выбирите нужный пункт расходов и доходов:')
    label_text_select_type = Label(text='Введите сумму расходов или доходов:')
    label_text_result = Label(text='Результаты:',)
    label_text_dohod = Label(text='Сумма доходов')
    label_text_summ = Label(text='ИТОГО')
    text_result = Listbox(width=50,height=10,selectmode=EXTENDED)
    scroll = Scrollbar(window, orient="vertical", command=text_result.yview)
    text_result.config(yscrollcommand=scroll.set)

    select_value.place(x=1, y=25)
    btn_rashod.place(x=1, y=110)
    btn_dohod.place(x=140, y=110)
    btn_delete.place(x=140,y=400)
    btn_result.place(x=1,y=400)
    label_text_result.place(x=1, y=200)
    text_result.place(x=1, y=230)
    ent_rashod_dohod.place(x=1,y=85)
    label_text_select.place(x=1,y=0)
    label_text_select_type.place(x=1,y=60)
    scroll.place(x=400,y=230,height=180)



def add_type_rashod():
    '''добавляем в спикок словарь с нашими расходами
    '''
    db.get_articles()
    articles = db.get_articles()
    #перехватываем ошибку неправильного ввода
    try:
        result_cost = int(ent_rashod_dohod.get())

    except ValueError as err:
        mb.showerror('Ошибка','Должно быть введено число!')
    new_article = {
            'cost':result_cost,
            'type_item': '-',
            'type_value': variable.get(),
            'data_create': datetime.datetime.today()
            }
    #widgets.ent_rashod_dohod.delete(0, END)
    articles.append(new_article)
    print (articles)
    db.write_articles() 
    

def add_type_dohod():
    '''добавляем в список словарь с нашими доходами
    '''
    db.get_articles()
    articles = db.get_articles()
    #перехватываем ошибку неправильного ввода 
    try:
        result_cost = int(ent_rashod_dohod.get())

    except ValueError:
        mb.showerror('Ошибка','Должно быть введено число!')
    
    new_article = {
            'cost': result_cost,
            'type_item': '+',
            'type_value': variable.get(),
            'data_create': datetime.datetime.today()
            }
    #widgets.ent_rashod_dohod.delete(0, END)
    articles.append(new_article)
    print (articles)
    db.write_articles()   
    