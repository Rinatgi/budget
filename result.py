import db


def result_income():
    '''считаем наши все доходы
    '''
    income_list = []
    articles = db.get_articles()
    for article in articles:
        if article['type_item']== '+':
            income_list.append(article['cost']) 
    summ_income = sum(income_list)        

    return summ_income


def result_expence():
    '''считаем все наши расходы
    '''
    expence_list = []
    articles = db.get_articles()
    for article in articles:
        if article['type_item'] == '-':
            expence_list.append(article['cost']) 
    summ_expence = sum(expence_list)        

    return summ_expence


def result_all():
    pass
    ''' общий итог
    
    result_income = result_income()
    result_expence = result_expence()
    result_all = result_income - result_expence

    return result_all
    '''