import os
import datetime
import sys
import json
import setting
import widgets
import category


def get_articles():
    '''функция чтения файла с нашими данными
    '''
    if os.path.exists(setting.ARTICLE_FILE_NAME):
    #если файл существует
    #загружаем список расходов
        with open (setting.ARTICLE_FILE_NAME, 'r', encoding='utf-8') as f:
            try:
            #перехватываем ошибки
                articles = json.load(f)
                for article in articles:
                #преобразуем дату в формат datetime
                    article['data_create'] = ( 
                        datetime.datetime.strptime(article['data_create'], setting.DATE_FORMAT))

            except Exception:
                articles = []        
    else:
        articles =[]

    return articles


def write_articles(articles):
    '''функция загрузки в файл нашего списка 
    '''
    write_article = []
    for article in articles:
        copy_article = {
            'cost': article['cost'],
            'type_item': article['type_item'],
            'type_value': article['type_value'],
            'data_create': article['data_create'].strftime(setting.DATE_FORMAT) 
            }
        write_article.append(copy_article)
    with open (setting.ARTICLE_FILE_NAME, 'w', encoding='utf-8') as f:
        data = json.dump(write_article,f, ensure_ascii=False, sort_keys=True) 


def get_articles_category():
    '''функция чтения файла с нашим списком значений расходов и доходов
    '''
    if os.path.exists(setting.ARTICLE_OPTIONS):
    #если файл существует
    #загружаем список расходов
        with open (setting.ARTICLE_OPTIONS, 'r', encoding='utf-8') as f:
            try:
            #перехватываем ошибки
                articles_category = json.load(f) 
            except Exception:
                articles_category = []  
    else:
        articles_category = []

    return articles_category


def write_article_category(articles_category):
    '''функция загрузки в файл нашего списка значений расходов и доходов 
    ''' 
    write_articles = []
    for category in articles_category:
        write_articles.append(category)
    with open (setting.ARTICLE_OPTIONS, 'w', encoding='utf-8') as f:
        data = json.dump(write_articles,f, ensure_ascii=False)     
    widgets.update_option_category_list(write_articles)

