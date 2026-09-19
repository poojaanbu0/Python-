s,m,l= 24,23,20
s_price ,m_price ,l_price ,topping_pr = 50,75,100,20

print(""" welcome to Pizza Shop!! choice down from the menu and place your order, 
      we have pizzas in 3 SIZES and toppings added with extra cost""")

print(f"we have small, medium and large pizzas, starting at {s_price}$")

while True:
    quantity = int(input("How many pizzas would you like to order:"))
        
    if quantity <= 0 :
        print("enter again, quantity must be greater than zero")
        continue

    size_gn = [] 
    for i in range(quantity):
        while True:
            Pizza_size = (input(f"what size do you prefer for pizza {i+1}: S M L\n"))
            if Pizza_size in ['s','S','1','small']:
                print(f"price of small size {s_price}$")
                Pizza_size = 'small'
                break
            elif Pizza_size in['m','M', '2' ,'medium']:
                print(f"price of medium size {m_price}$")
                Pizza_size = 'medium'
                break
            elif Pizza_size in ['l' ,'L', '3' ,'large']:
                print(f"price of large size {l_price}$")
                Pizza_size = 'large'
                break
            else:
                print(f"enter a valid size for {i+1} pizza")

        size_gn.append(Pizza_size)
    
    print("pizza size:",size_gn)
    
    top_list = []
    topping = input("would you like to add toppings to the pizzas: Y N\n")
    if topping in ['y','Y',"yes", 'ya','sure']:
        for i in range(len(size_gn)):
            top_size = size_gn[i]
            top = input(f"for pizza {i+1} of size {top_size}: Y N\n")
            if top in ['Y', 'yes',"ya", 'sure']:
                top_list.append(topping_pr)
            else:
                top_list.append(0)
        print("topping",top_list)
    
    add_order = input("would you like to add something else to your order: Y N\n ")
    if "n" in add_order.lower() :
        print("thank you for ordering , your order totaling to be soon delivered")
        break
    print("sure")

    print('total')
    # else:
    #     print("invalid input")




    









