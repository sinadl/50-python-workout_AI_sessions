menu = {'sandwich':10,'coffee':2.45,'pizza':5.25,'tea':4.5,'lattee':3,'coca':1.5}
def restaurant_menu():
    total = 0
    while True:
        order = input('please enter your item on the menu:')
        if not order:
            break
        if order in menu:
            total += menu[order]
            print(f'cost of {order} is: {menu[order]}')
            print(f'total cost of your order: {total}')
        else:
            print(f'{order} is not on our menu. go somewhere else and never come back!!!')
    print(f'your total money: {total}')
    
restaurant_menu()