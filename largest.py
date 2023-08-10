number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
number_3 = int(input("Enter third number: "))

if number_1 > number_2:
    largest_number = number_1

if number_3 > largest_number:
    largest_number = number_3
    
print(largest_number)