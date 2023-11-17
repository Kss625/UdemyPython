Hours = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
# new rate for overtime is 1.5
pay1 = 40 * rate
if Hours > 40:
    h1 = Hours - 40
    pay2 = h1 * rate * 1.5
    print(f"Total Pay:{round(pay1 + pay2, 2)}")
else:
    print(f"Total Pay:{round(Hours * rate, 2)}")
