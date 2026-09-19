def pizza_price(size, quantity):
    price = 50 if size == "small" else 75 if size == "medium" else 100 
    price *= quantity
    return price

top_price = 20
total = 0
order= True

print(""" welcome to Pizza Shop!! choice down from the menu and place your order, 
      we have pizzas in 3 SIZES and toppings added with extra cost""")

print(f"we have small, medium and large pizzas")

while order:
    size = input("\nEnter pizza size (small, medium, large): ")
 
    quantity = int(input("How many of this specific pizza do you want? "))
    toppings = int(input("How many toppings would you like? "))

    
    pizza = pizza_price(size, quantity)
    tot_top = toppings * top_price
    order_cost = pizza + tot_top
    
    total += order_cost
    print(f"Added {quantity} {size} pizza(s) to your order. Subtotal: ${order_cost:.2f}")
    

    reorder = input("\nWould you like to order another pizza? (yes/no): ").lower()
    if reorder not in ['yes','ya']:
        order = False


print(f"thank you for ordering , your order totaling ${total:.2f} to be soon delivered ")
