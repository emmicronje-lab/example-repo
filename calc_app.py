while True:
    
    print("Welcome to the calculator app!")
    print("You can perform basic operations like subtraction, addition, multiplication and division.")
    print("1. Perform a calculation")
    print("2. Previous calculations")
    print("3. Exit")

    choice = input("Please enter your choice (1, 2 or 3):")
    
    if choice == '1':
        try:
            num1 = float(input("Please enter the first number: "))
            num2 = float(input("Please enter the second number: "))
            operator = input("Please enter the operator (-,+,*,/): ")

            if operator == '-':
                result = num1 - num2
            elif operator == '+':
                result = num1 + num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Cannot divide by zero, try again...")
                    continue
            else:
                 print("Please enter a valid operator, try again...")
                 continue
        
            equation = f"{num1} {operator} {num2} = {result}"
            print(f"Answer: {equation}")

            with open("equations.txt", "a") as file:
                file.write(equation + "\n")

        except ValueError:
            print("Please enter a valid number, try again...")
            continue

    elif choice == '2':
        try:
            with open("equations.txt", "r") as file:
                equations = file.readlines()
                if equations:
                    print("Previous calculations: ")
                    for equation in equations:
                        print(equation.strip())
                else:
                    print("No previous calculations found.")
        except FileNotFoundError:
            print("No previous calculations found.")

    elif choice == '3':
        print("Thank you for using the calculator app. Goodbye!")
        break
    else:
        print("Invalid choice, please select 1,2 or 3...")
    

        
    
        
    


