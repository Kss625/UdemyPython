'''Calculate Price'''
available_parts = {
    "1": "Computer",
    "2": "monitor",
    "3": "keyboard",
    "4": "mouse",
    "5": "hdmi cable",
    "6": "dvd drive"
}
price_quantity = {
    "Computer": {"Price": 500, "quantity": 10},
    "monitor": {"Price": 200, "quantity": 8},
    "keyboard": {"Price": 500, "quantity": 5},
    "mouse": {"Price": 10, "quantity": 0},
    "hdmi cable": {"Price": 20, "quantity": 7},
    "dvd drive": {"Price": 50, "quantity": 5},
}
print("Please add Options from the List")
price = 0
for key, value in available_parts.items():
    print(key, value)
print(f"{0} finish")
total_price = 0
i = True
while i:
    current_choice = input("> ")

    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if price_quantity[chosen_part]["quantity"] > 0:
            print(f"Adding {chosen_part}")
            price_quantity[chosen_part]["quantity"] -= 1
            total_price = price_quantity[chosen_part]["Price"] + total_price
        else:
            print(f"{chosen_part} is out of stock")
            break
    elif current_choice == "0":
        i = False
print(f"{total_price}")
