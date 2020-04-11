number_1 = int(input("Insert a number: "))
number_2 = int(input("Insert another number: "))
operator = input("Insert an operator: ")

if operator == "+":
    print(number_1 + number_2)
elif operator == "-":
    print(number_1 - number_2)
elif operator == "*":
    print(number_1 * number_2)
elif operator == "/":
    print(number_1 / number_2)
else:
    print("This calculator can only add, subtract, multiply and divide. Please provide valid operator.")
