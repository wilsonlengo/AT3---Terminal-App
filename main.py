#Welcome to subway
print("Welcome to Subway!")
print("Baked fresh daily and available in 6-inch and Footlong sizes")

submenu = ["Ultimate Chicken", "Ultimate Meatball", "BLT", "Buffalo Chicken", "Chicken Bacon", "Chicken Classic", "Chicken Strips", "Chicken Teriyaki", "Chicken Schnitzel", "Leg Ham", "Meatball Melt", "Pizza Melt", "Roast Beef", "Falafel", "Steak Melt", "Tuna Mayo", "Turkey", "Veggie", "Veggie Patty"]
submenu_price = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

orderItems = []
orderTotal = []

sidemenu = ["HamCheeseTomato Jaffle", "Meatball Pot", "Chipotle", "Avocado Toastie", "CheesyGarlic Toastie", "GarlicHerb Toastie", "Ultimate Toastie", "Chocolate Cookie", "Rainbow Cookie", "DoubleChocolate Cookie", "Raspberry Cookie", "Macadamnia Cookie", "Coke", "Sprite", "Coke NoSugar", "IcedTea", "Water Bottled", "Water Sparkling"]
sidemenu_price = [5, 5, 5, 4, 4, 4, 4, 2, 2, 2, 2, 4, 4, 4, 4, 3, 3]
order = input("Are you looking to purchase a sandwich today or just side menu items? Please enter 'yes' for the Sub Menu or 'no' for the Side Menu:\n")
if order == "yes":
    print(submenu)
    subOrder = input("What are you after? Select 1 (e.g Ultimate Chicken)\n")
    if subOrder == "Ultimate Chicken":
        orderItems.append(submenu[0])
        orderTotal.append(submenu_price[0])
    
    elif subOrder == "Ultimate Meatball":
         orderItems.append(submenu[1])
         orderTotal.append(submenu_price[1])
    
    elif subOrder == "BLT":
         orderItems.append(submenu[2])
         orderTotal.append(submenu_price[2])
        
    elif subOrder == "Buffalo Chicken":
         orderItems.append(submenu[3])
         orderTotal.append(submenu_price[3])
    
    elif subOrder == "Chicken Bacon":
         orderItems.append(submenu[4])
         orderTotal.append(submenu_price[4])

    elif subOrder == "Chicken Classic":
         orderItems.append(submenu[5])
         orderTotal.append(submenu_price[5])

    elif subOrder == "Chicken Strips":
         orderItems.append(submenu[6])
         orderTotal.append(submenu_price[6])

    elif subOrder == "Chicken Teriyaki":
         orderItems.append(submenu[7])
         orderTotal.append(submenu_price[7])

    elif subOrder == "Chicken Schnitzel":
         orderItems.append(submenu[8])
         orderTotal.append(submenu_price[8])

    elif subOrder == "Leg Ham":
         orderItems.append(submenu[9])
         orderTotal.append(submenu_price[9])

    elif subOrder == "Meatball Melt":
         orderItems.append(submenu[10])
         orderTotal.append(submenu_price[10])

    elif subOrder == "Pizza Melt":
         orderItems.append(submenu[11])
         orderTotal.append(submenu_price[11])

    elif subOrder == "Roast Beef":
         orderItems.append(submenu[12])
         orderTotal.append(submenu_price[12])

    elif subOrder == "Falafel":
         orderItems.append(submenu[13])
         orderTotal.append(submenu_price[13])

    elif subOrder == "Steak Melt":
         orderItems.append(submenu[14])
         orderTotal.append(submenu_price[14])

    elif subOrder == "Tuna Mayo":
         orderItems.append(submenu[15])
         orderTotal.append(submenu_price[15])

    elif subOrder == "Turkey":
         orderItems.append(submenu[16])
         orderTotal.append(submenu_price[16])

    elif subOrder == "Veggie Only":
         orderItems.append(submenu[17])
         orderTotal.append(submenu_price[17])
    
    elif subOrder == "Veggie Patty":
         orderItems.append(submenu[18])
         orderTotal.append(submenu_price[18])
    else: 
        print("Not on menu!")
elif order == "no":
    print(sidemenu)
    sidemenuOrder = input("What are you looking for in the side menu? (e.g CheesyGarlic Toastie)\n")
else:
    print("Invalid!")

print(orderItems)
print(orderTotal)
#print(submenu)