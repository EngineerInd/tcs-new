menu = [['Espresso Coffee','Cappuucino Coffee','Latte Coffee'], ['Plain Tea',

'Assam Tea','Ginger Tea','Cardamom Tea','Masala Tea','Lemon Tea','Green Tea',

'Organic Darjeeling Tea'], ['Hot and Sour Soup','Veg Corn Soup','Tomato Soup',

'Spicy Tomato Soup'], ['Hot Chocolate Drink', 'Badam Drink',

'Badam-Pista Drink']]

m = input()

if m=='c' or m=='t' or m=='s' or m=='b':

    if m=='c':

        submenu = int(input())

        if submenu in range(3):

            print('Welcome to CCD!\nEnjoy your {}!'.format(menu[0][submenu-1]))

        else:

            print("INVALID INPUT")

    if m=='t':

        submenu = int(input())

        if submenu in range(8):

            print('Welcome to CCD!\nEnjoy your {}!'.format(menu[1][submenu-1]))

        else:

            print("INVALID INPUT")

    if m=='s':

        submenu = int(input())

        if submenu in range(4):

            print('Welcome to CCD!\nEnjoy your {}!'.format(menu[2][submenu-1]))

        else:

            print("INVALID INPUT")

    if m=='b':

        submenu = int(input())

        if submenu in range(3):

            print('Welcome to CCD!\nEnjoy your {}!'.format(menu[3][submenu-1]))

        else:

            print("INVALID INPUT")

else:

    print("INVALID INPUT!")
