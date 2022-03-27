# FIRST TASK

# a, b, c = 1, 15, 77
# print(a, b, c)
# name = input("What is your name?")
# number = int(input("What is your favourite number?"))
# print(name, number)

# SECOND TASK

# time_In_secs = int(input("Enter the time for your project in seconds: "))
# hours_in_data = time_In_secs // 3600
# minutes_in_data = (time_In_secs % 3600) // 60
# secs_in_data = (time_In_secs % 3600) % 60
# print(f"Your time for project is {hours_in_data}:{minutes_in_data}:{secs_in_data}")
# print("Your time for project is {}:{}:{}".format(hours_in_data, minutes_in_data, secs_in_data))

# THIRD TASK

# number = input("Enter a number: ")
# number2 = (number + number)
# print(number2)
# number3 = (number + number + number)
# print(number3)
# sum_of_numbers = int(number) + int(number2) + int(number3)
# print(sum_of_numbers)

# FOURTH TASK

# user_number = input("Enter your number: ")
# a = user_number[0]
# b = user_number[1]
# c = user_number[2]
# while a > b and a > c:
#     print(f"Your max figure in a number is {a}")
#     break
# while b > a and b > c:
#     print(f"Your max figure in a number is {b}")
#     break
# while c > a and c > b:
#     print(f"Your max figure in a number is {c}")
#     break

# FIFTH TASK

# proceeds = int(input("What is your firm-corporation' proceeds?"))
# expenses = int(input("What is your firm' expenses?"))
# employee_number = int(input("How many employees do your firm have?"))
# income = proceeds - expenses
# income_for_person = round(income/employee_number, 2)
# if proceeds > expenses:
#     print("You are doing very well!!! You have income!!!")
#     profitability = round(income/proceeds, 2)
#     print(f"Your profitability is {profitability}")
#     print(f"Your income for an employee is {income_for_person}")
# else:
#     print("You need work over optimization!!!")

# SIXTH TASK

a = 2
b = 10
day_count = 1
while a <= b:
    print(f"At {day_count} day you achieved {round(a, 2)} km")
    day_count += 1
    day_increase = round(a * 0.1, 2)
    a += day_increase
print(f"At {day_count} day your result is {a} km")
