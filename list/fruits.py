# fruits = [
#               {"name":"orange",
#                "price": 45,
#                "quantity":5}
#                ,
#                {"name": "apple",
#                 "price": 100,
#                 "quantity": 15}
#                 ,
#                 {"name": "mango",
#                    "price": 55,
#                    "quantity": 10}
#           ]


# total = 0

# order = True

    
# while order:
#     print("List of fruits Available:\nFruit      Price")
#     for i in fruits:
#         print(f"{i['name']:10}"
#               f"Price:₹{i['price']:1}")
#     gn_fruit = input("choose fruit: Orange Apple Mango\n").lower()
#     gn_quat = int(input(f"how many kgs of {gn_fruit} do you want:\n"))

#     selected_fruit = None

#     for fruit in fruits:
#         if fruit["name"] == gn_fruit:
#             selected_fruit = fruit
#             break

#     if selected_fruit is None:
#         print("Fruit not found!")
#         continue

#     available = selected_fruit["quantity"]

#     if available == 0:
#         print("Sorry, stock unavailable.")
#         continue

#     if gn_quat > available:

#         print(f"Only {available} available.")

#         choice = input(
#             f"Do you want to buy from available stock ({available})? (yes/no): "
#         ).lower()

#         if choice == "yes":
#             gn_quat = int(
#                 input(
#                     f"Enter quantity (1 to {available}): "
#                 )
#             )

#             while gn_quat < 1 or gn_quat > available:
#                 gn_quat = int(
#                     input(
#                         f"Invalid quantity. Enter between 1 and {available}: "
#                     )
#                 )

#         else:
#             continue

#     cost = gn_quat * selected_fruit["price"]

#     total += cost
    
#     selected_fruit["quantity"] -= gn_quat

#     print(f"Subtotal for this item: ₹{cost}")
#     print(f"Running Total: ₹{total}")

#     more = input(
#         "\nWould you like to buy something else? (yes/no): "
#     ).lower()

#     if more != "yes":
#         break


# print(f"Total Amount = ₹{total}")


     


























# # def fruit_price(fruit,gn_quat):
# #     q = fruit_data[fruit]["Quantity"]
# #     print(q)
# #     avil_quat = q
# #     avil_quat -=  gn_quat  
# #     print(q)
# #     print(avil_quat)
# #     fruit_data[fruit]["Quantity"]  = q if (avil_quat < 0) else avil_quat
    
class Animal:

    def eat(self):
        print("Eating")

class fivesense:
    def eat(self):
        print("5 sense")

class Dog(Animal,fivesense):
   pass

d = Dog()

d.eat()
print(d.mro())
