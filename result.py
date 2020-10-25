import db
from tkinter import END


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
    '''
    sum_result_income = result_income()
    sum_result_expence = result_expence()
    sum_result_all = sum_result_income - sum_result_expence

    return sum_result_all
    


def show_result(text_result_income, text_result_expence, text_result_all):
    '''Выводим суммы доходоб расходов и общий результат
    '''
    sum_result_income = result_income()
    sum_result_expence = result_expence()
    sum_result_all = result_all()
    text_result_income.delete(0, END)
    text_result_expence.delete(0, END)
    text_result_all.delete(0, END)
    text_result_income.insert(0, sum_result_income)
    text_result_income.itemconfig(0, bg='green',)
    text_result_expence.insert(0, sum_result_expence)
    text_result_expence.itemconfig(0, bg='red')
    text_result_all.insert(0, sum_result_all)