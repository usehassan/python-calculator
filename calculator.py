def calculator():
    while True:
        try:
            n1 = float(input("Enter the first number: "))
    
            oper = input("Enter the operation (+, - , ** , /, *): ")
            
            n2 = float(input("Enter the second number: "))

            if oper == "+":
                result = n1 + n2
            elif  oper == "-":
                result = n1 - n2
            elif  oper == "*":
                result = n1 * n2
            elif  oper == "**":
                result = n1 ** n2
            elif  oper== "/":
                if n2 == 0:
                    print("Dividing by 0 is not possible.")
                    continue
                result = n1 / n2
            else:
                print("Invalid operation. Please try again.")
                continue
            
            print(f"Result: {result}")

        except ValueError:
            print("Please enter valid numbers.")



calculator()
