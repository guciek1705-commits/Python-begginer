# Concession stand program 

menu = {"pizza": 3.00,
        "hot dog": 2.00,
        "soda": 1.00,
        "popcorn": 5.00,
        "candy": 1.50,
        "nachos": 4.00,
        "pretzel": 2.50,
        "ice cream": 3.50}
cart = []
total = 0

print("---------Welcome to the Concession Stand!---------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("--------------------------------------------------")  

while True:
    food = input("Select an item (q to quit): ")
    if food == "q":
         break
    elif menu.get(food) is not None:
        cart.append(food) 

print("------------YOUR ORDER------------") 
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print(f"Total is: ${total:.2f}")
