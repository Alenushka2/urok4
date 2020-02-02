acc_balance = 0
shop_list = []

def acc_repl():
    return(float(input('Enter the amount to replenish the account:')))
def shop_history():
    if len(shop_list) == 0:
        print('No purchases yet!')
    else:
        print('Purchase hystory:')
        for item in shop_list:
            print(item[0],item[1], 'rub')


def shop_action(acc_bal):
    sum = float(input('Enter purchase cost:'))
    if sum > acc_bal:
        print('There is not enough money in the account')
    else:
        name = input('Enter purchase name:')
        acc_bal -= sum
        shop_list.append([name, sum])
    return acc_bal


while True:
    print('1. refill')
    print('2. purchase')
    print('3. purchase hystory')
    print('4. exit')


    choice = input('Select menu item')
    if choice == '1':
        acc_balance += acc_repl()
        print('Account balance {0: 8.2f} rubles'.format(acc_balance))
    elif choice == '2':
        acc_balance = shop_action(acc_balance)
    elif choice == '3':
        shop_history()
    elif choice == '4':
        print('Thanks for shopping! Come again!')
        break
    else:
        print('Invalid menu item')

""""
1. refill
2. purchase
3. purchase hystory
4. exit
Select menu item1
Invalid menu item
1. refill
2. purchase
3. purchase hystory
4. exit
Select menu item2
Invalid menu item
1. refill
2. purchase
3. purchase hystory
4. exit
Select menu item3
Invalid menu item
1. refill
2. purchase
3. purchase hystory
4. exit
Select menu item200
Invalid menu item
1. refill
2. purchase
3. purchase hystory
4. exit
Select menu item 
""""""        
