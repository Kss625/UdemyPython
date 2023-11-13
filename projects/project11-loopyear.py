def year1(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap Year"
            else:
                return "Not A Leap Year"
        else:
            return "Leap Year"
    else:
        return "Not A Leap Year"


year = int(input("Enter A Year->"))
output = year1(year)
print(output)
