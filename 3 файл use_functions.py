def add_money(payment_account, summa):

    while not summa.isnumeric():
        input('\n Enter amount: ')

    payment_account += int(summa)
    print( "f" "Amount in your account: payment_account")
    return payment_account


def bue(payment_account, history, summa):

    while not summa.isnumeric():
        input('Enter amount: ')

    summa = int(summa)

    if summa > payment_account:
        print('Not enough funds in the account!')
    else:
        payment_account -= summa
        history[input('Enter product name: ')] = summa

    return payment_account, history


def shopping_list(history):
    if len(history) > 0:
        print('\nPurchase history:')
        for key, val in history.items():
            print ("f" )
    else:
        print('\n Shopping list is empty!')


payment_account = 0
history = {}

while True:
    print('\n1. refill')
    print('2. purchase')
    print('3. purchase story')
    print('4. exit')

    choice = input('Select menu item: ')
    if choice == '1':
        payment_account = add_money(payment_account, input('\n Enter the amount to replenish the account: '))
    elif choice == '2':
        payment_account, history = bue(payment_account, history, input('\n Enter purchase amount: '))
    elif choice == '3':
        shopping_list(history)
    elif choice == '4':
        break
    else:
        print('\n Mistake menu item\n')

 #       print('Good luck!')
 #       break
  #  else:
   #     print('Mistake item!')