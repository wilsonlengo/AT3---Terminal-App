#Welcome to subway
print("Welcome to Subway!")




#Dictonary of ingredients
# Loop through menu, and into breads and
menu = {
    "breads" : {
        "whitebread" : 2,
        "wheatbread" : 2,
        "italianherb": 2,
        "maltedrye": 2,
        "plainwrap": 2,
        "glutenfreewrap": 2,
        "multigrainwrap": 2,
    },
  
    "cheese" : {
        "cheddar": 1,
        "mozzarella": 1,
        "oldenglish": 1,
    },

    "vegetables" : {
        "avocado": 1,
        "capsicum": 1,
        "carrots": 1,
        "cucumbers": 1,
        "lettuce": 1,
        "onions": 1,
        "spinach": 1,
        "jalapeno": 1,
        "olives": 1,
        "pickles": 1,
        "beetroot": 1,
    },

    "sauce" : {
        "habanero_hot_sauce": 1,
        "blue_cheese_dressing": 1,
        "smoky_bbq": 1,
        "chipotle_southwest": 1,
        "mayonnaise": 1,
        "garlic_aioli": 1,
        "sweet_onion": 1,
        "honey_mustard": 1,
        "ranch_dressing": 1,
        "tomato_sauce": 1,
        "spicy_mayo": 1,
    },
}

toasted = None
cart = [] # {Avocado: 3}

def build():
    print("Baked fresh daily and available in 6-inch and Footlong sizes")

    bread_choice = None
    bread_price = None
    
    # for key, value in menu["breads"].items():
    #     print(f"{key.capitalize()}: ${value}")

    # bread_choice = input("Choose your bread from the list above:\n")
    # bread_price = menu["breads"][bread_choice]
    # print("BREAD CHOICE: ", bread_choice)
    # print("BREAD PRICE: ", bread_price)

    # for key, value in menu["cheese"].items():
    #     print(f"{key.capitalize()}: ${value}")
        
    # cheese_choice = input("Choose your type of cheese:\n")
    # cheese_price = menu["cheese"][cheese_choice]
    # print("CHEESE CHOICE ", cheese_choice)
    # print("CHEESE PRICE: ", cheese_price)

    # for key, value in menu["vegetables"].items():
    #     print(f"{key.capitalize()}: ${value}")
    
    vegetable_choice = input("List all the vegetables you want (e.g. lettuce, tomato, beetroot):\n")
    vegetable_price = 0

    # 'lettuce, tomato, beetroot'
    print(vegetable_choice)
    vegetable_choices = vegetable_choice.split(',')
    print(vegetable_choice)

    for vegetable in vegetable_choices:
        # vegetable_price += 
        print(menu["vegetables"][vegetable])

    print(vegetable_price)
 
    

    


#Dictionary of sidemenu

sidemenu = {
    "cookies" : {
        "chocchip" : 1,
        "chocchip_rainbow" : 1,
        "double_chocolate" : 1,
        "raspberry_cheesecake" : 1,
        "macadamia_nut" : 1, 
    },
    "beverage" : {
        "coke" : 1,
        "coke_nosugar" : 1,
        "sprite" : 1,
        "icedtea_peach" : 1,
        "coffee_dare" : 1,
        "water_bottled" : 1,
    },
    "snack" : {
        "hamcheesetomato_jaffle" : 1,
        "chipotle" : 1,
        "meatball_mozza_pot" : 1,     
    },
    "toastie" : {
        "toastie_avocado" : 1,
        "toastie_cheesygarlic" : 1,
        "toastie_garlicherb" : 1,
    }


#Receipt Generator + Total price

#Delivery
