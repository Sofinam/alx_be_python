num1 = float(input("Enter the first number"))
num2 = float(input("Enter the second number"))

#Asking for the operation type
operation = input("Choose the operation (+, -, *, /): ").strip()

#Perform calculations using the match case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}")
        else:
            print("Cannot divide by zero.")
    case _:
        print ("Choose the operation (+, -, *, /)")
