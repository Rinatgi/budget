''' Программа контроля 
рахода семейного бюджета'''
from tkinter import  END, messagebox as mb
import datetime
import widgets
import db

db.get_articles()
     
def print_article():
    '''вводим наши все записи
        в окно
    '''
    articles = db.get_articles()
    for article in articles:
        for key, value in article.items():
            s = '{} {}'.format(key, value)
            widgets.text_result.insert(0, s)
       


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


 
 