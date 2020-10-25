import db
import widgets
import random
import datetime
import setting
from random_timestamp import random_timestamp
from tkinter import messagebox 


demo_articles = []


def request_user():
    '''получаем ответ от пользователя на удаления данных
    '''

    articles = db.get_articles()
    answer = messagebox.askyesno(title="Вопрос", message="Удалить данные?")
    if answer == True:
        articles.clear()
        db.write_articles(articles)
        demo()
        

def demo():

    categories = setting.CATEGORY
    counter = 0
    date = datetime.datetime.today()

    while counter != 25:
        category = random.choice(categories)
        if category == 'Зарплата':
            result = random.randrange(15000, 25000, 1000)
            type_item = '+' 


        elif category == 'Премия':
            result = random.randrange(1000, 10000, 500)
            type_item = '+'

        elif category == 'Авто':
            result = random.randrange(500,3000, 100)
            type_item = '-'

        elif category == 'Продукты':
            result = random.randrange(100, 3000, 100)
            type_item = '-'

        elif category == 'Одежда':
            result = random.randrange(500, 3000, 200)
            type_item = '-'
        
        elif category == 'ЖКХ':
            result = random.randrange(3000 ,10000, 1000)
            type_item = '-'

        elif category == 'Образование':
            result = random.randrange(1000, 20000, 1000)                   
            type_item = '-'

        random_date = random_timestamp(2020, part='DATE')
        new_article = {
            'cost':result,
            'type_item': type_item,
            'type_value': category,
            'data_create': random_date
            }
    #widgets.ent_rashod_dohod.delete(0, END)
        demo_articles.append(new_article)
        counter += 1
    db.write_articles(demo_articles)
    widgets.update_article_list()                    
