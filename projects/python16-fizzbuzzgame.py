print("Welcome To FizzBuzz-Game")
upper_limit = int(input("Enter a Upper Limit: "))
lower_limit = int(input("Enter a lower Limit: "))
print("Fizz comes when Number is either is divisible by 5")
print("Buzz comes when Number is either is divisible by 7")
print(" FizzBuzz comes when Number is divisible by both 5 and 7")
for i in range(lower_limit, upper_limit + 1):
    if i % 5 == 0 and i % 7 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Fizz")
    elif i % 7 == 0:
        print("Buzz")
    else:
        print(i)
print("Hope,You Enjoy FizzBuzz-Game")
