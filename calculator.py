# addition
def add(x, y):
    return x + y


#  subtraction 
def subtract(x, y):
    return x - y


#  multiplication 
def multiply(x, y):
    return x * y


#  division 
def divide(x, y):
    return x / y


print("Select operation.\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Modulus\n")

while True:

    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "%", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")
