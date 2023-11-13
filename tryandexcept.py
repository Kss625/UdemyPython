print("Welcome To Mortgage Calculator ")
try:
    salary = int(input("What is your Salary? "))
except ValueError:
    print("Enter An Integer Number!")
    try:
        salary = int(input("What is your Salary? "))
    except ValueError:
        print("Enter An Integer Number!")
finally:
    if salary >= 2000:
        print("Eligible For Mortgage")
        credit = int(input("Enter Your Credit Score"))
        if credit > 800:
            print("Interest Rate is 4%")
        else:
            if credit > 600:
                print("Interest Rate is 6%")
            else:
                print("Interest Rate is 8%")
    else:
        print("You Are Not Eligible For Mortgage")
print("Thanks For Using Our Calculator")
