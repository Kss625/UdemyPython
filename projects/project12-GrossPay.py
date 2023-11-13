def GrossPay(Hours, rate):
    if Hours > 40:
        pay1 = 40 * rate
        overtime = Hours - 40
        pay2 = overtime * rate * 1.5
        return f"Total Pay:{round(pay1 + pay2, 2)}"
    else:
        return f"Total Pay:{round(Hours * rate, 2)}"


def check_for_float(p_input):
    try:
        val = float(p_input)
        return val
    except:
        print("Error,Please enter numeric input")
        quit()


Hours = input("Enter The Hours-")
Hour = check_for_float(Hours)
rate = input("Enter The Rate-")
rate = check_for_float(rate)
print(GrossPay(Hours, rate))  # returning the output
