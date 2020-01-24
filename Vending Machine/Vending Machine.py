from tkinter import gui

# make gui
# sets,tuples,dictionaries,file handling

def items(run,curbal,itemsBought,prices):
    while run == 'y':
        print()
        item = str(input("What Do You Want To Buy? : "))
        print()
        if item=='A1':
            curbal -= 20
            itemsBought.append("Lays")
            prices.append(20)
            print("Lays\t",'20')
        elif item=='A2':
            curbal -= 30
            itemsBought.append("KurKure")
            prices.append(30)
            print("KurKure\t",'30')
        elif item=='A3':
            curbal -= 80
            itemsBought.append("Snickers")
            prices.append(80)
            print("Snickers\t",'80')
        elif item=='A4':
            curbal -= 45
            itemsBought.append("Coca Cola")
            prices.append(45)
            print("Coca Cola\t",'45')
        elif item=='A5':
            curbal -= 10
            itemsBought.append("DingDong")
            prices.append(10)
            print("DingDong\t",'10')
        elif item=='A6':
            curbal -= 40
            itemsBought.append("Doritos")
            prices.append(40)
            print("Doritos\t",'40')
        elif item=='A7':
            curbal -= 50
            itemsBought.append("M&Ms")
            prices.append(50)
            print("M&Ms\t",'50')
        elif item=='A8':
            curbal -= 40
            itemsBought.append("KitKat")
            prices.append(40)
            print("KitKat\t",'40')
        elif item=='A9':
            curbal -= 30
            itemsBought.append("Sprite")
            prices.append(30)
            print("Sprite\t",'30')
        elif item=='A10':
            curbal -= 20
            itemsBought.append("Oreo")
            prices.append(20)
            print("Oreo\t",'20')
        elif item=='B1':
            curbal -= 200
            itemsBought.append("Red Bull")
            prices.append(200)
            print("RedBull\t",'200')
        elif item=='B2':
            curbal -= 10
            itemsBought.append("Twitch")
            prices.append(10)
            print("Twitch\t",'10')
        elif item=='B3':
            curbal -= 60
            itemsBought.append("Ruffles")
            prices.append(60)
            print("Ruffles\t",'60')
        elif item=='B4':
            curbal -= 30
            itemsBought.append("Milk Treat")
            prices.append(30)
            print("MilkTreat\t",'30')
        elif item=='B5':
            curbal -= 20
            itemsBought.append("Water")
            prices.append(20)
            print("Water\t",'20')
        elif item=='B6':
            curbal -= 45
            itemsBought.append("Milo")
            prices.append(45)
            print("Milo\t",'45')
        elif item=='B7':
            curbal -= 40
            itemsBought.append("Cheetos")
            prices.append(40)
            print("Cheetos\t",'40')
        elif item=='B8':
            curbal -= 20
            itemsBought.append("Dairy Milk")
            prices.append(20)
            print("DairyMilk\t",'20')
        elif item=='B9':
            curbal -= 30
            itemsBought.append("Biscuit")
            prices.append(30)
            print("Biscuit\t",'30')
        elif item=='B10':
            curbal -= 70
            itemsBought.append("Skittles")
            prices.append(70)
            print("Skittles\t",'70')
        else:
            print("Invalid Input, Kindly Enter a Valid Product Code")
            print()
            continue
        while curbal<0:
            add = -curbal
            print("Enter Rs.",add, "or more Into The Machine: ", end ="")
            rem= int(input(" "))
            curbal+=rem
            
                
            print()

        print("Your Remaining Cash is Rs.",curbal,"/-\n")
        
        run = input("Do you want to buy something else? [y/n]: ")
        print()
        if run == 'y':
            continue
            
        
    return(curbal,itemsBought,prices,run)

def main():
    run = 'y'
    count = 0
    print("********************************************************************************")
    print("This is a program of a Vending Machine Simulator, you can use it to buy snacks")
    print("virtually,although it can be applied to an actual machine with more adjustments")
    print("********************************************************************************")
    print()
    while run == 'y' and count>=0:
        money = int(input("Enter Money Into The Machine: "))
        print()
        #valid money = 185,280,150 etc and not 283, 281 etc
        while money%5!=0:
            print("Enter valid amount of money for example 150|285|90:", end ="")
            money = int(input(" "))
        if count == 0:
            curbal = 0
            itemsBought = []
            prices = []
            qty = []
            count+=1
        
        if curbal>0 or curbal<0:
            curbal+=money
        elif curbal==0:
            curbal = money

        Lays = "A1"
        Kurkure = "A2"
        Snickers = "A3"
        CocaCola = "A4"
        DingDong = "A5"
        Doritos = "A6"
        MMs = "A7"
        KitKat = "A8"
        Sprite = "A9"
        Oreo = "A10"
        RedBull = "B1"
        Twitch = "B2"
        Ruffles = "B3"
        B4 = "B4"
        B5 = "B5"
        B6 = "B6"
        B7 = "B7"
        B8 = "B8"
        B9 = "B9"
        B10 = "B10"


        print("Your Current Balance is Rs.",curbal,"/-\n")
        print('\tProduct Codes\nCode\t Product\t Price \nA1- \t Lays	  \t Rs.20 \nA2- \t Kurkure \t Rs.30 \nA3- \t Snickers \t Rs.80 \nA4- \t CocaCola \t Rs.45 \nA5- \t DingDong \t Rs.10 \nA6- \t Doritos \t Rs.40 \nA7- \t M&Ms	  \t Rs.50 \nA8- \t KitKat \t Rs.40\nA9- \t Sprite \t Rs.30 \nA10- \t Oreo	  \t Rs.20 \nB1- \t RedBull \t Rs.200 \nB2- \t Twitch \t Rs.10 \nB3- \t Ruffles \t Rs.60 \nB4- \t MilkTreat \t Rs.30 \nB5- \t Water	  \t Rs.20 \nB6- \t Milo	  \t Rs.45 \nB7- \t Cheetos \t Rs.40 \nB8- \t DairyMilk \t Rs.20 \nB9- \t Biscuit \t Rs.30 \nB10- \t Skittles \t Rs.70')

        list1 = items(run,curbal,itemsBought,prices)
        # one of the main loop conditions
        print()
        
        if list1[0] == 0:
            run = input("Do you want to continue buying items? [y/n]: ")
            if run == 'y':
                continue

        # loop will break when run not equal to y
        if list1[3] != 'y':
            # print receipt
            print("Here's your receipt!")
            print("Product\tPrice\tQty")
            #for i in dict3:
             #   if dict3[i]>0:
              #      qty.append(dict3[i])
            for i in range(len(list1[1])):
                # insert check for more than one quantity
                print(list1[1][i],"\t",list1[2][i])
                gui(list1[1])
            print()
            # remaining balance
            if list1[0]>0:
                print("Your remaining Cash is ", list1[0])
                print("Rs.",list1[0], "will be returned to you right now")
            print()
            
            print("Thank You for Using this Service!!")
            break            
        

main()

#Prices
#'''#Lays = 20
#Kurkure = 30
#Snickers = 80
#CocaCola = 45
#DingDong = 10
#Doritos = 40
#MMs = 50
#KitKat = 40
#Sprite = 30
#Oreo = 20
#RedBull = 200
#Twitch = 10
#Ruffles = 60
#MilkTreat = 30
#Water = 20
#Milo = 45
#Cheetos = 40
#DairyMilk = 20
#Biscuit = 30
#Skittles = 70'''


