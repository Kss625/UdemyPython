print("Welcome To Trip Cost Calculator ")
Hotel_Price = float(input("Enter The Hotel Price Per Night?-$"))
Flight_Price = float(input("Enter The Flight Price?-$"))
Days = int(input("How Many Days You Stay Here-"))
RentalCar = float(input("If You Need Rental Car Then Enter The Price Otherwise Zero?-$"))
other = float(input("Enter the Price of other expenses-$"))
total = Flight_Price + other + (Hotel_Price + RentalCar) * Days
print(f"Total Price Of TripCost {round(total, 2)}")
