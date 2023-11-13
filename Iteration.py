''' for loops in python '''
l = [1, 3, 5, 34, 56, 89]

for i in l:
    print(i, end=" ")
    print(f"index value is {l.index(i)}")  # take characters through index value
a = 0
for i in range(1, 6):  # range function
    a = a + i
print(a)

'''                  Highest Score Problem                           '''

l = [65, 60, 50, 80, 75, 55]
s = 0
for score in l:
    if score > s:
        s = score
print(f"Highest score is {s}")

'''                    finding integer value from given list                               '''
custom_list = [11, 30.1, 90.2, 30, 45.1, 54, '54']
for num in custom_list:
    # if type(num) == type(1):
    #     print(num)
    if isinstance(num, int):
        print(num)
'''                         sum of above average scores                                  '''
student_scores = [80, 60, 50, 65, 75, 55]


def sum_score_above_average(p_student_scores):
    # TODO
    sum = 0
    total_students = 0
    sum1 = 0
    for score in p_student_scores:
        sum = sum + score
        total_students = total_students + 1
    avg = (sum / total_students)
    for num in p_student_scores:
        if num > avg:
            sum1 = sum1 + num
    return sum1


print(sum_score_above_average(student_scores))
'''custom function'''


def password_controller(password):
    if len(password) > 8:
        return True
    else:
        return False


password_list = ["qwer", "123456", "0986573685948y", "abchrofj"]
for password in password_list:
    result = password_controller(password)
    print(password, result)

'''                             Loop with range                     '''
sum = 0
for number in range(1, 11):
    sum = sum + number
    print(number, end=" ")
print()
print("Sum is", sum)

vegetables = ["potato", "Tomato", "Brinjal", "Corn"]
for i in range(len(vegetables)):
    print(vegetables[i])
print()
'''sum of add numbers '''


def add_odd_numbers(start, stop, step):
    # TODO
    sum_of_oddNumbers = 0
    for i in range(start, stop, step):
        if i % 2 != 0:
            sum_of_oddNumbers = sum_of_oddNumbers + i
    return sum_of_oddNumbers


print(add_odd_numbers(start=1, stop=101, step=1))

'''sum of even numbers'''


def add_even_numbers(start, stop):
    # TODO
    sum_of_evenNumbers = 0
    for i in range(start, stop):
        if i % 2 == 0:
            sum_of_evenNumbers = sum_of_evenNumbers + i
    return sum_of_evenNumbers


print(add_even_numbers(1, 101))

'''While Loops'''
i = 1
while i <= 10:
    print(i, end=" ")
    i = i + 1
print()
'''checking username'''
username = ""
while username != "test":
    username = input("Enter username:")
print()
'''Continue and break keywords'''
for num in range(1, 10):
    if num == 5:
        continue  # printing numbers between 1 to 10 except 5
    print(num, end="")

print()
for num in range(1, 11):
    if num == 5:
        break
    print(num)
'''finding factorial of given numvber'''


def factorial(p_num):
    # TODO
    factorial = 1
    if p_num == 0:
        return f"factorial of {0} is {1}"
    elif p_num == -1:
        return f"factorial of {-1} is {1}"
    elif p_num < 0:
        return f"factorial does not exist for negative numbers"
    else:
        for i in range(1, p_num + 1):
            factorial = factorial * i
        return f"factorial of {p_num} is {factorial}"


print(factorial(4))
print(factorial(-1))


def check_for_floats(p_input):
    try:
        val = float(p_input)
        return val
    except (ValueError, TypeError):
        print("Error,please enter numeric input")
        return False


count = 0
total = 0.0
average = 0.0
while True:
    number = input("Enter a numer: ")
    if number == "done":
        break

    number = check_for_floats(number)
    if not number:
        continue
    count = count + 1
    total = total + number
if count != 0:
    average = total / count
print(total, count, average)

input1 = input("Enter a number: ")
if input1 == "done":
    quit()
number = check_for_floats(input1)
if not number:
    print("The first entered has to be number to continue")
    quit()
smallest = number
biggest = number
while True:
    number = input("Enter a number: ")
    if number == "done":
        break
    number = check_for_floats(number)
    if number > biggest:
        biggest = number
    if number < smallest:
        smallest = number
print(f"maximum number:{biggest},minimum number:{smallest}")
