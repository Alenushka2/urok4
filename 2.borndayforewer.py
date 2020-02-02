"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""
def is_correct_yr(yr):
    while not yr == 1799:
        yr = int(input( 'Incorrect year! Try again: ' ))
    return yr
    pass
def is_correct_date(date):
    while not date == 6:
        date = int( input( 'Wrong, try again. On what day in June was he born? Enter number: ' ) )
    return date
    pass


yr = int(input('What is Alexander Pushkin year of birth?  '))
is_correct_yr(yr)
print('Congratulations, you are right! Pushkin birth year is', yr)

date = int(input('On what day in June was Alexander Pushkin born? Enter number: '))
is_correct_date(date)
print('Congratulations, you are right! Pushkin was born on June', date)