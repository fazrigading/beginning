import datetime

print("""
    ====================================
    
                 Avore Cafe                                                                                            
 
    ====================================
    ----LIST OF FOOD AND DRINK MENU----
    1. Toast                   : 25.000
    2. Onion Ring              : 10.000
    3. Spring Roll             : 25.000
    4. Fruit Salad             : 35.000
    5. Chicken Wings           : 40.000
    6. Thai Tea                : 15.000
    7. Ovaltine                : 15.000
    8. Green Tea               : 15.000
    9. Red Velvet              : 15.000
    10. Choco Lava Milo        : 20.000
    ====================================
    -------------Promo List-------------
    a. Get Discount Every Purchase
       3 Drinks at 10%
    b. Get Discount Every Purchase
       2 Foods at 5%
    c. Get Discount Every Payment
       Via E-Money by 5%
    d. Get Discount During Weekend
       by 5%
    e. Get Discount During Weekdays
       by 10%
    ====================================
    """)



food_menu = [
        {"food_list" : 1 , "food_name" : "Toast", "food_price" : 25000},
        {"food_list" : 2 , "food_name" : "Onion Ring", "food_price" : 10000},
        {"food_list" : 3 , "food_name" : "Spring Roll", "food_price" : 25000},
        {"food_list" : 4 , "food_name" : "Fruit Salad", "food_price" : 35000},
        {"food_list" : 5 , "food_name" : "Chicken Wings", "food_price" : 40000},
]
drink_menu = [
        {"drink_list" : 1 , "drink_name" : "Thai Tea", "drink_price" : 15000},
        {"drink_list" : 2 , "drink_name" : "Ovaltine", "drink_price" : 15000},
        {"drink_list" : 3 , "drink_name" : "Green Tea", "drink_price" : 15000},
        {"drink_list" : 4 , "drink_name" : "Red Velvet", "drink_price" : 15000},
        {"drink_list" : 5 , "drink_name" : "Choco Lava Milo", "drink_price" : 20000},
]


def show_menu() :
    print ("\n")
    print ("----ADMIN MENU----")
    print ()
    print ("1. Cafe Menu List")
    print ("2. Add Menu")
    print ("3. Remove Menu From List")
    print ("4. Changing Menu")
    print ("5. Exit")
    
def choose_menu() :
    print ("""
    1. Food Menu
    2. Drink Menu
    """)

def show_menu_makanan() :
    if len (food_menu) <= 0 :
        print ("Food Menu Not Available")
    else :
        print ("FOOD MENU")
        for menu in food_menu:
            print (f"{menu['food_list']}. {menu['food_name']}  ---> Rp. {menu['food_price']}")
            
def insert_food_menu() :
    try :
        choose = 'Yes'
        while choose == 'Yes' :
            show_menu_makanan()
            new_food_menu = {}     
            new_food_menu ["food_list"] = int(input("Please Enter the Number List : "))
            name_food = str(input("Please Enter the Menu You Want To Add : "))
            new_food_menu ["food"] = name_food
            new_food_menu ["space"] = ("        ")
            new_food_menu ["food_price"] = (int(input(f"Please Enter the Price of {name_food} : ")))   
            food_menu.append (new_food_menu)
            show_menu_makanan()
            choose = str(input("Do You Want to Add More Food? "))
    except :
        print ("an Error Occurred in Filling in the Data!")

def delete_food_menu() :
    try :
        choose = 'Yes'
        while choose == 'Yes' :
            print ("FOOD MENU")
            show_menu_makanan ()
            delete_food = int(input("Please Select The Menu You Want To Delete : "))
            delete = delete_food - 1
            del food_menu [delete]
            print ("SUCCEED!!!")
            print ("\nNEW MENU")
            show_menu_makanan ()
            choose = str(input("Do You Want to Delete the Menu Again? "))
    except :
        print ("an Error Occurred in Filling in the Data!")
    
def edit_food_menu() :
    try :
        choose = 'Yes'
        while choose == 'Yes' :
            show_menu_makanan ()
            edit_food = str(input("Please Select The Menu You Want To Change : "))
            for food in food_menu :
                if food ['food_list'] == edit_food :
                    change_name = str(input("Please Enter A New Menu  : "))
                    change_price= int(input("Please Enter the Price of the New Menu : "))
                    food ['food'] = change_name
                    food ['food_price'] = change_price
            
            show_menu_makanan ()
            choose = str(input("Do You Want to Change the Menu Again? "))
    except :
        print ("an Error Occurred in Filling in the Data!")
        
def show_menu_minuman () :
    if len (drink_menu) <= 0 :
        print ("Drink Menu Not Available")
    else :
        print ("DRINK MENU")
        for menu in drink_menu:
            print (f"          {menu['drink_list']}. {menu['drink_name']}  ---> Rp. {menu['drink_price']}")

def insert_drinks_menu () :
    try : 
        choose = 'Yes'
        while choose == 'Yes' :
            show_menu_minuman ()
            new_drink_menu = {}     
            new_drink_menu ["drink_list"] = (int(input("Please Enter the Number List : ")))
            name_drink = str(input("Please Enter the Menu You Want To Add : "))
            new_drink_menu ["drink"] = name_drink
            new_drink_menu ["space"] = ("        ")
            new_drink_menu ["drink_price"] = (int(input(f"Please Enter the Price of {name_drink} : ")))   
            drink_menu.append (new_drink_menu)
            show_menu_minuman()
            choose = str(input("Do You Want to Add More Drink? "))
    except :
        print ("an Error Occurred in Filling in the Data!")
    print ("_________________")
    
def delete_drinks_menu() :
    print ("_" * 50)
    try :
        choose = 'y'
        while choose == 'y' or choose == 'Y' :
            show_menu_minuman()
            delete_drink = int(input("Please Select The Menu You Want To Delete : "))
            delete = delete_drink - 1
            del drink_menu[delete]
            print ("SUCCEED!!!")
            print ("--------------------------------------")
            print ("\nNEW MENU")
            show_menu_minuman()
            choose = str(input("Do You Want to Delete the Menu Again? "))
    except :
        print("an Error Occurred in Filling in the Data!")
def edit_drinks_menu() :
    print("_" * 50)
    try :
        choose = 'y'
        while choose == 'y' or choose == 'Y' :
            show_menu_minuman()
            edit_drink = str(input("Please Select The Menu You Want To Change : "))
            for drink in drink_menu :
                if drink['no_d'] == edit_drink :
                    change_name = str(input("Please Enter A New Menu  : "))
                    change_price= int(input("Please Enter the Price of the New Menu : "))
                    drink['drink'] = change_name
                    drink['drink_price'] = change_price
            show_menu_minuman()
            choose = str(input("Do You Want to Change the Menu Again? "))
    except :
        print("an Error Occurred in Filling in the Data!")

def admin_cafe() :
    choose = 'y'
    while choose == 'y' or choose == 'Y' :
        show_menu()
        menu_cafe = int(input("Please Select Menu : "))
        print()
        if menu_cafe == 1 :
            print("""
            ====================================
    
                         Avore Cafe                                                                                            
 
            ====================================
            """)
            show_menu_makanan()
            show_menu_minuman()
        elif menu_cafe == 2 :
            choose_menu()
            Q = int(input("Please Choose : "))
            if Q == 1 :
                insert_food_menu()
            elif Q == 2 :
                insert_drinks_menu()
            else :
                print("This Option is Not Available!")
        elif menu_cafe == 3 :
            choose_menu()
            Q = int(input("Please Choose : "))
            if Q == 1 :
                delete_food_menu()
            elif Q == 2 :
                delete_drinks_menu()
            else :
                print("This Option is Not Available!")
        elif menu_cafe == 4 :
            choose_menu()
            Q = int(input("Please Choose : "))
            if Q == 1 :
                edit_food_menu()
            elif Q == 2 :
                edit_drinks_menu()
            else :
                print("This Option is Not Available!")
        elif menu_cafe == 5 :
            break
        else :
            print("The Menu is Not Available")
        choose = str(input("Want to Go Back to Menu Again? "))

def customer_cafe() :
    try :
        print("_______WELCOME_______")
        show_menu_makanan()
        show_menu_minuman()
    #Proses 
    
        list_ordered_makanan = []
        list_ordered_minuman = []
        greet1 = str(input("Want to Order Something? "))
        
                
        #Jika Ingin Memesan
        
        while greet1 == 'y' or greet1 == 'Y' :
            print("________Pemesanan_______")
            order = str(input("What Would You Like to Order? (Food/Drink) "))
            if order == 'Food' :
                order_food = int(input("Please Select Your Food Menu : "))
                ordered = next((sub for sub in food_menu if sub['food_list'] == order_food), None)
                total_food = int(input(f"How Many Servings of {ordered['food']} Would You Like to Order? "))
                ordered['total_food'] = int(total_food)
                ordered['payment'] = ordered['total_food'] * ordered['food_price']
                list_ordered_makanan.append(ordered)
                greet1 = str(input("are there any more? "))
            elif order == 'd' or order == 'D' :
                order_drink = input("Please Select Your Food Menu : ")
                ordered = next((sub for sub in drink_menu if sub['drink_list'] == order_drink), None)
                total_drink = int(input(f"How Many Servings of {ordered['drink']} Would You Like to Order? "))
                ordered['total_drink'] = int(total_drink)
                ordered['payment'] = ordered['total_drink'] * ordered['drink_price']
                list_ordered_minuman.append(ordered)
                greet1 = str(input("are there any more? "))      
            else :
                print("the Menu is Not Available!")   
        
        print("_________________")
    
        #Proses Penjumlahan Pesanan
        
        total_food = 0
        total_drinks = 0
        for list_order in list_ordered_makanan :
            total_food += list_order['total_food']
        for list_order in list_ordered_minuman :
            total_drinks += list_order['total_drink']
            
        #Potongan Harga Yang Di Dapatkan
        
        if total_food >= 2 :
            food_discount = 5
        else :
            food_discount = 0
        if total_drinks >= 3 :
            drink_discount = 10
        else :
            drink_discount = 0
        menu_discount = food_discount + drink_discount
        if datetime.datetime.today().weekday() < 5 :
            day_discount = 10
        else : 
            day_discount = 5
        payment = str(input("Do You Want to Make Payments via E - Money? "))
        if payment == 'y' or payment == 'Y' :
            emoney_discount = 5
        else :
            emoney_discount = 0
            
    except : 
        print("an Error Occurred in Filling in the Data!")

        #Proses Perhitungan Keseluruhan
        
    print("_________________")
    print()
    print("                     PEMBAYARAN                 ")
    print("                     ----------                 ")
    for list_order in list_ordered_makanan :
        print(list_order['food'])
        print(list_order['food_price'], "x", list_order['total_food'], "= RP.", list_order['payment'])
    for list_order in list_ordered_minuman :
        print(f"{list_order['drink']}")
        print(f"{list_order['drink_price']} x {list_order['total_drink']} = RP. {(list_order['payment'])}")
    print("---------------------------------------------------+")
    total_discount = menu_discount + day_discount + emoney_discount
    list_all_ordered = list_ordered_makanan + list_ordered_minuman
    total_price = sum(list_order['payment'] for list_order in list_all_ordered)
    cut_discount = total_price * total_discount / 100
    total_payment = total_price - cut_discount
    print("                                         RP.", total_price)
    print("----------------------------------------------------")
    print("Diskon Makanan :  ",  food_discount, "%")
    print("Diskon Minuman :  ", drink_discount, "%")
    print("Diskon Hari    :  ",   day_discount, "%")
    print("Diskon E_Money :  ",emoney_discount, "%")
    print("---------------------------------------------------+")
    print("            RP.", total_price, "Diskon Sebesar", total_discount, "%")
    print("---------------------------------------------------=")
    print("                                Total : RP.",  total_payment)
    print("__________________")
    
choose = 'y'
while choose == 'y' or choose == 'Y' :
    
    print("""
    ---LOGIN---
    
    1. Admin  
    2. Customer
    3. Exit
    _________________
    """)
    login = int(input("    You Want to Login as : "))
    if login == 1 :
        admin_cafe()
    elif login == 2 :
        customer_cafe()
    elif login == 3 :
        exit()
    else :
        print("the Menu is Not Available!")
    choose = str(input("Want to Go Back to the Login Menu? "))
