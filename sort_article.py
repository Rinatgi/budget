import db
import datetime
import widgets
import cal
from tkinter import END
import setting


def refresh_sort_category():
    widgets.combo_category['values'] = db.get_articles_category()



def sort_article_list(select_date):
    '''функция сотировки по дате
    '''
    articles = db.get_articles()
    sorted_articles = []
    for article in articles:
        if article['data_create'] == select_date:
            sorted_articles.append(article)
    update_article_list(sorted_articles)

def update_article_list(sorted_articles):
    '''выводим отсортированный список на экран
    '''    
    widgets.text_result.delete(0, END)
    index = 0 
    for article in sorted_articles:
        s = '{cost} руб. {type_item} {type_value} {data_create}'.format(**article)
        widgets.text_result.insert(0, s)
        if article['type_item'] == '-':
            widgets.text_result.itemconfig(index, bg='red')
            
        else:
            widgets.text_result.itemconfig(index, bg='green')                
    index += 1


def sort_article_range_date(start_date, end_date):
    '''функция определения дат по заданным периодам
    '''
    articles = db.get_articles()
    sorted_articles = []
    date_1 = min(start_date, end_date)
    date_2 = max(start_date, end_date) 
    
    while date_1 < date_2:
        date_1 += datetime.timedelta(days=1)
        for article in articles:
            if article['data_create'] == date_1:
                sorted_articles.append(article)

    update_article_list(sorted_articles)
   




