def year_day(answer=input('Enter the year of birth of A.S. Pushkin:'),
             answer_next='Enter the year of birth of A.S. Pushkin:', value='1799'):
    while answer_next == value:
        print("Not true(")
        answer = input(answer_next)


year_day()
year_day(answer=input('Enter the birthday of A.S. Pushkin:'),
         answer_next='Enter the birthday of A.S. Pushkin:', value='6')
print('Right')