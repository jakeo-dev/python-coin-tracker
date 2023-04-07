# this is a mock 'create performance task' python project for ap csp

money = []
total = 0


def isNum(a):
    # used and modified https://stackoverflow.com/a/5424739 to check if something is a number
    try:
        b = int(a)
        return True
    except ValueError:
        return False


def calcPennies(pennies):
    return pennies * 0.01


def calcNickels(nickels):
    return nickels * 0.05


def calcDimes(dimes):
    return dimes * 0.10


def calcQuarters(quarters):
    return quarters * 0.25


def newMoney():
    total = 0
    for i in range(4):
        currentCoins = whichCoin(
            input('Enter a type of coin (P: pennies, N: nickels, D: dimes, Q: quarters): '))

        while 'currentCoins' not in locals() or currentCoins == 0.0009:
            # used https://stackoverflow.com/a/843293 to check if variable exists
            currentCoins = whichCoin(input('Enter a type of coin: '))

        total = round(total + currentCoins, 2)
        print(name.title() + ' now has $' + str(total))

    return total


def whichCoin(c):
    if 'p' in c:
        while True:
            inp = input('Number of pennies: ')
            if inp.isnumeric():
                currentCoins = calcPennies(float(inp))
                break
    elif 'n' in c:
        while True:
            inp = input('Number of nickels: ')
            if inp.isnumeric():
                currentCoins = calcNickels(float(inp))
                break
    elif 'd' in c:
        while True:
            inp = input('Number of dimes: ')
            if inp.isnumeric():
                currentCoins = calcDimes(float(inp))
                break
    elif 'q' in c:
        while True:
            inp = input('Number of quarters: ')
            if inp.isnumeric():
                currentCoins = calcQuarters(float(inp))
                break
    else:
        print('Could not recognize that type of coin.')
        currentCoins = 0.0009

    return currentCoins


while True:
    name = input('\nEnter name: ').lower()

    action = input('What do you want to do with your money? (view, edit): ')

    if action.lower() == 'edit':
        if name.lower() not in money:
            money.append(name)

        total = newMoney()

        if len(money) > (money.index(name) + 1) and isNum(money[money.index(name) + 1]) == True:
            money.pop(money.index(name) + 1)
            # used https://www.w3schools.com/python/python_lists_remove.asp to remove list item by index
        money.insert(money.index(name) + 1, total)
    elif action.lower() == 'view':
        if name in money:
            # used https://stackoverflow.com/a/843293 to check if variable exists
            print(name.title() + ' has $' + str(money[money.index(name) + 1]))
        else:
            print('You don\'t have any money!')
