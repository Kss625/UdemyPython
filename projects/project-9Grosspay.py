try:
    Hours = float(input("Enter Hours:"))
except ValueError:
    print("Enter Hour in Integer or float")
    Hours = float(input("Enter Hours:"))
try:
    rate = float(input("Enter Rate:"))
except ValueError:
    print("Enter rate in Integer or float")
    rate = float(input("Enter Rate:"))  # overtime rate is 1.5
if Hours > 40:
    pay1 = 40 * rate
    overtime = Hours - 40
    pay2 = overtime * rate * 1.5
    print(f"Total Pay:{round(pay1 + pay2, 2)}")
else:
    print(f"Total Pay:{round(Hours * rate, 2)}")
