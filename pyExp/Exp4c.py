import sys
print("MENU CARD")
lst_choice = []
lst_qty = []
dict_menu = {1:'Naan', 2:'Paneer Masala', 3:'Pepsi', 4:'Kulfi'}
dict_price = {1:15, 2:300, 3:50, 4:20}
while(1):
    print('1: Naan Rs.10/piece \n2: Paneer Masala Rs.300/plate \n3: Pepsi Rs.50/bottle \n4: Kulfi Rs.20/serving')
    try:
        a = input('Do you want to order?(y/n): ')
    except:
        print("Oops!",sys.exc_infoO[0],"occured.")
        continue
    if(a == 'y' or a =='Y'):
        try:
            choice = int(input('Enter choice: '))
        except:
            print("Oops!",sys.exc_infoO[0],"occured.")
            continue
        if(choice >= 1 and choice <= 4):
            try:
                qty = int(input('How much qty do you need: '))
            except:
                print("Oops!",sys.exc_infoO[0],"occured.")
                continue
            if(qty >= 1):
                lst_choice.append(choice)
                lst_qty.append(qty)
                print('\n')
            else:
                print('Wrong Input n')
                continue
        else:
            print('Wrong Input \n')
            continue
    elif(a == 'n' or a == 'N'):
        print('\nBILL:')
        total = 0
        length = len(lst_choice)
        for i in range(0, length):
            val = lst_choice[i]
            print(dict_menu[val],'Qty: ',lst_qty[i],' Rs.', dict_price[val], 'per unit')
            total = total + (dict_price[val] * lst_qty[i])
        print('Total = Rs.', total)
        print('Thank you')
        break
    else:
        print("Wrong input \n")
        continue


