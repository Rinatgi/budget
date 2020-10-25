from tkinter import (Button, Entry, Label, StringVar, END, messagebox as mb, Listbox, EXTENDED, Frame, TOP, 
                    Toplevel, LEFT, N, Y, X, Menu
                    )
import widgets
from tkcalendar import Calendar
import sort_article
import datetime




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




    