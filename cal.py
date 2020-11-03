from tkinter import (Button, Entry, Label, StringVar, END, messagebox, Listbox, EXTENDED, Frame, TOP, 
                    Toplevel, LEFT, N, Y, X, Menu
                    )
import widgets
from tkcalendar import Calendar
import sort_article
import datetime
import setting




def create_window_calendar():
    '''создаем окно для календаря
    '''
    global cal, top_widget
    date_today = datetime.date.today()
    top_widget = Toplevel()  
    #фокусируем наше окно
    #top.focus_set()
    #делаем его модальным(чтобы нельзя было переключиться на главное окно)
    top_widget.grab_set()
    #мы задаем приложению команду, что пока не будет закрыто окно top пользоваться другим окном будет нельзя. 
    frame = Frame(top_widget)
    frame.pack(side=LEFT, padx=10)
    select_date_calendar = Button(frame, text="Выбрать", command=set_date)
    select_date_calendar.pack(fill=X)
    cal = Calendar(
                frame, selectmode="day", 
                year=date_today.year, 
                month=date_today.month, 
                day=date_today.day
            )
    cal.pack()


def set_date():
    '''выбираем дату
    '''
    select_date = cal.selection_get()
    sort_article.sort_article_list(select_date)
    widgets.show_date(select_date)
    top_widget.destroy()
 



def create_window_range_date():

    global date_start, date_end, top_widget
    top_widget = Toplevel()
    top_widget.geometry('300x130')
    top_widget.title('Введите период')  
    #фокусируем наше окно
    #top.focus_set()
    #делаем его модальным(чтобы нельзя было переключиться на главное окно)
    top_widget.grab_set()
    #мы задаем приложению команду, что пока не будет закрыто окно top пользоваться другим окном будет нельзя. 
    frame = Frame(top_widget)
    frame.pack(side=TOP, padx=10)
    user_confirmation = Button(top_widget, text="Выбрать", command=check_user_enter_date)
    user_confirmation.place(relx=0.45, rely=0.55)
    date_start = Entry(top_widget, width=10, font=('Arial', 10))
    date_end = Entry(top_widget, width=10, font=('Arial', 10))
    label_date_format = Label(top_widget, text='Введите дату в формате: "ГОД.МЕСЯЦ.ДЕНЬ"', font=('Arial', 10))
    label_from = Label(top_widget, text='От:')
    label_before = Label(top_widget, text='До:')
    date_start.place(relx=0.1, rely=0.3)
    date_end.place(relx= 0.50, rely=0.3)
    label_date_format.place(relx=0.03, rely=0.10)
    label_from.place(relx=0.02, rely=0.3)
    label_before.place(relx=0.38, rely=0.3)


def check_user_enter_date():

    try:
        # с помощью функции datetime преобразуем полученные строки 
        # в необходимый нам формат даты
        # получаем дату начала задачи
        dt_start = datetime.datetime.strptime(date_start.get(), setting.DATE_FORMAT).date()
        dt_end = datetime.datetime.strptime(date_end.get(), setting.DATE_FORMAT).date()
        sort_article.sort_article_range_date(dt_start, dt_end)
        top_widget.destroy()
    except ValueError:
        # перехватываем ошибку,если не правильный ввод 
        # возвращаемся в начало запроса даты  
        messagebox.showerror('Ошибка!','Вы ввели неверный формат даты!Повторите ввод.')
        #если дата введена правильно продолжаем дальше    
    