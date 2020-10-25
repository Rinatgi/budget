import db
import datetime
import widgets
import cal
from tkinter import END


def refresh_sort_category():
    widgets.combo_category['values'] = db.get_articles_category()



def sort_article_list(select_date):
    '''функция сотировки по дате
    '''
    print(select_date)
    articles = db.get_articles()
    sorted_articles = []
    for article in articles:
        if article['data_create'] == select_date:
            sorted_articles.append(article)
    print(sorted_articles)
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

