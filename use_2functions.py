personal_account = [0,[]]
def is_digit(string):
    try:
        float(string)
        return True
    except ValueError:
        return False


def f_account_replenishment(account):
    indicator = 1
    print('*' * 40)
    print('REFILL:')
    while indicator > 0:
        indicator = 0
        recharge_amount = input('Enter the deposit amount: ')
        if not is_digit(recharge_amount):
            print('Enter number!')
            indicator = 1
    account[0] += float(recharge_amount)
    return account


def f_purchase (account):
    indicator = 1
    print('*' * 40)
    print('PURCHASE::')
    while indicator > 0:
        indicator = 0
        price = input('Enter purchase cost: ')
        if not is_digit(price):
            print('Enter number!')
            indicator = 1
    if float(price) > account[0]:
        print('There is not enough money in the account')
    else:
        product = input('Enter purchase name: ')
        account[0] -= float(price)
        account[1].append ([product,price])
    return account


def f_purchase_history (account):
    print('*' * 40)
    print('Purchase hystory:')
    for tandem in account[1]:
        print( "f" 'Product: {tandem[0]} Price: {tandem[1]}')

while True:
    print('*' * 40)
    print("f" 'On your account - {personal_account[0]} rub.')
    print('=' * 40)
    print('Menu:')
    print('1. refill')
    print('2. purchase')
    print('3. purchase hystory')
    print('4. exit')
    print('*' * 40)
    choice = input('Select menu item: ')
    if choice == '1':
        personal_account = f_account_replenishment(personal_account)
    elif choice == '2':
        personal_account = f_purchase(personal_account)
    elif choice == '3':
        f_purchase_history(personal_account)
    elif choice == '4':
        print('#' * 40)
        print('YOU EXITED THE PROGRAM!')
        break
    else:
        print('*' * 40)
        print("Invalid menu item")

#fOn your account - {personal_account[0]} rub.
#========================================
#Menu:
1. refill
2. purchase
3. purchase hystory
4. exit
****************************************
Select menu item: 1
****************************************
Invalid menu item
****************************************
fOn your account - {personal_account[0]} rub.
========================================
Menu:
1. refill
2. purchase
3. purchase hystory
4. exit
****************************************
Select menu item: 2
****************************************
Invalid menu item
****************************************
fOn your account - {personal_account[0]} rub.
========================================
Menu:
1. refill
2. purchase
3. purchase hystory
4. exit
****************************************
Select menu item: 3
****************************************
Invalid menu item
****************************************
fOn your account - {personal_account[0]} rub.
========================================
Menu:
1. refill
2. purchase
3. purchase hystory
4. exit
****************************************
Select menu item: 4
****************************************
Invalid menu item
****************************************
fOn your account - {personal_account[0]} rub.
========================================
Menu:
1. refill
2. purchase
3. purchase hystory
4. exit
****************************************
Select menu item:
#