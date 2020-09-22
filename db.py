import os
import datetime
import sys
import json
import article
import setting


def get_article():
    '''функция чтения файла с нашими данными
    '''
    if os.path.exists(setting.file_task):
    #если файл существует
    #загружаем список расходов
        with open (setting.file_task, 'r', encoding='utf-8') as f:
            try:
            #перехватываем ошибки
                tasks = json.load(f)
                for task in tasks:
                #преобразуем дату в формат datetime
                    task['data_create'] = ( 
                        datetime.datetime.strptime(task['data_create'], setting.date_format))

            except Exception:
                tasks = []        
    else:
        tasks =[]

    return tasks


def write_article():
    '''функция загрузки в файл нашего списка 
    '''
    tasks = article.add_type_rashod()
    write_task = []
    for task in tasks:
        copy_task = {
            'cost': task['cost'],
            'type_item': task['type_item'],
            'type_value': task['type_value'],
            'data_create': task['data_create'].strftime(setting.date_format) 
            }
        write_task.append(copy_task)
    with open (setting.file_task, 'w', encoding='utf-8') as f:
        data = json.dump(write_task, f,ensure_ascii=False, sort_keys=True) 

