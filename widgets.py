from tkinter import Tk, Menu, Button, Entry, Label, LabelFrame, OptionMenu, StringVar, END, messagebox as mb, Scrollbar, Listbox,EXTENDED,Frame,TOP
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
    frame_1 = LabelFrame(window, text='Данные', height=300, width=600)
    frame_2 = LabelFrame(window, text='Результаты', height=300, width=700)
    # ширина экрана
    w = window.winfo_screenwidth()
    # высота экрана
    h = window.winfo_screenheight()   
    # значение по умолчанию
    variable.set(options[0])
    select_value = OptionMenu(frame_1, variable, *options)
    btn_rashod = Button(frame_1, text='Добавить расходы', command=add_type_rashod, font = ('Arial', 12))
    btn_dohod = Button(frame_1, text='Добавить доходы', command=add_type_dohod, font = ('Arial', 12))
    btn_result = Button(frame_2, text='Сохраниь результаты', font = ('Arial', 12))
    btn_delete = Button(frame_2, text='Удалить', command=del_article, font = ('Arial', 12))
    ent_rashod_dohod = Entry(frame_1, width=40, font = ('Arial', 12))
    label_text_select = Label(frame_1, text='Выбирите нужный пункт расходов и доходов:', font = ('Arial', 12))
    label_text_select_type = Label(frame_1, text='Введите сумму расходов или доходов:', font = ('Arial', 12))
    label_text_result = Label(frame_1, text='Результаты:', font = ('Arial', 12))
    label_text_dohod = Label(frame_1, text='Сумма доходов', font = ('Arial', 12))
    label_text_summ = Label(frame_1, text='ИТОГО')
    text_result = Listbox(frame_2, width=53, height=13, selectmode=EXTENDED, font = ('Arial', 12))
    scroll = Scrollbar(frame_2, orient="vertical", command=text_result.yview)
    text_result.config(yscrollcommand=scroll.set)

    select_value.place(relx=0.03, rely=0.15)
    btn_rashod.place(relx=0.03, rely=0.70)
    btn_dohod.place(relx=0.33, rely=0.70)
    btn_delete.place(relx=0, rely=0.03)
    btn_result.place(relx=0, rely=0.25)
   # label_text_result.place(relx=0.5, rely=0.05)
    text_result.place(relx=0.27, rely=0.01)
    ent_rashod_dohod.place(relx=0.03, rely=0.55)
    label_text_select.place(relx=0.03, rely=0.03)
    label_text_select_type.place(relx=0.03, rely=0.40)
    scroll.place(relx=0.96, rely=0.01, height=260)
    frame_1.place(relx=0.02, rely=0.02)
    frame_2.place(relx=0.47, rely= 0.02)


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


def update_article_list():
    '''вводим наши все записи
        в окно
    ''' 
    index = 0 
    articles = db.get_articles()
    for article in articles:
        s = '{cost} {type_item} {type_value} {data_create}'.format(**article)
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
    select = list(text_result.curselection())
    select.reverse()
    for i in select:
        text_result.delete(i)

    return i    
