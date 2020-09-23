import os
import datetime
import sys
import json
import article
import setting


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


def write_articles():
    '''функция загрузки в файл нашего списка 
    '''
    articles = get_articles()
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
        data = json.dump(write_article, f,ensure_ascii=False, sort_keys=True) 

