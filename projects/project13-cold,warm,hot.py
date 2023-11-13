def temperature(temp):
    if temp > 28:
        return "Hot"
    elif temp <= 28 and temp >= 18:
        return "Warm"
    else:
        return "Cold"


try:
    temp = float(input("Enter The Temperature-"))
except ValueError:
    print("Error,Please Give Numeric Input")
    temp = float(input("Enter The Temperature-"))
    output = temperature(temp)
    print(output)
else:
    output = temperature(temp)
    print(output)
finally:
    print("Hope,You Enjoy Your Weather")
