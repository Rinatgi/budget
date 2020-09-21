import os
import datetime
import sys
import json
import settings

#переменная названия файла
file_task = 'data_file.txt'
#формат даты
date_format = '%Y.%m.%d'


def read_file():
    '''функция чтения файла с нашими данными
    '''
    if os.path.exists(file_task):
    #если файл существует
    #загружаем список расходов
        with open (file_task, 'r', encoding='utf-8') as f:
            try:
            #перехватываем ошибки
                tasks = json.load(f)
                for task in tasks:
                #преобразуем дату в формат datetime
                    task['data_create'] = ( 
                        datetime.datetime.strptime(task['data_create'], date_format))

            except Exception:
                tasks = []        
    else:
        tasks =[]

    return tasks


def write_file():
    '''функция загрузки в файл 
        наших значений 
    '''
    tasks = settings.add_type_rashod()
    write_task = []
    for task in tasks:
        copy_task = {
            'cost': task['cost'],
            'type_item': task['type_item'],
            'type_value': task['type_value'],
            'data_create': task['data_create'].strftime(date_format) 
            }
        write_task.append(copy_task)
    with open (file_task, 'w', encoding='utf-8') as f:
        data = json.dump(write_task, f,ensure_ascii=False, sort_keys=True) 

