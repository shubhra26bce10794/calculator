from basic_operations import add, subtract, multiply, divide, power
from mathematical_operations import square, square_root, factorial, sine, cosine, tangent, logarithm, natural_log
from scientific_calculator import square, square_root, factorial, sine, cosine, tangent, logarithm, natural_log
from calculation_history import History

while True:
    print("\n CALCULATOR")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square")
    print("7. Square Root")
    print("8. Factorial")
    print("9. Sine")
    print("10. Cosine")
    print("11. Tangent")
    print("12. Logarithm")
    print("13. View History")
    print("0. Exit")
    choice =input("Enter your choice: ")
    if choice == "0":
        print("Thank you for using the calculator!")
        break
    elif choice == "13":
        History()
        continue
    try:
        if choice=="1":
            a=float(input("Enter first number: "))
            b=float(input("Enter second number: "))
            result=add(a,b)
        elif choice=="2":
            a=float(input("Enter first number: "))
            b=float(input("Enter second number: "))
            result=subtract(a, b)
        elif choice=="3":
            a=float(input("Enter first number: "))
            b=float(input("Enter second number: "))
            result=multiply(a, b)
        elif choice=="4":
            a=float(input("Enter first number: "))
            b=float(input("Enter second number: "))
            result=divide(a,b)
        elif choice=="5":
            a=float(input("Enter first number: "))
            b=float(input("Enter second number: "))
            result=power(a, b)
        elif choice=="6":
            a=float(input("Enter number: "))
            result=square(a)
        elif choice=="7":
            a=float(input("Enter number: "))
            result=square_root(a)
        elif choice=="8":
            a=int(input("Enter a whole number: "))
            result=factorial(a)
        elif choice=="9":
            a = float(input("Enter angle in degrees: "))
            result = sine(a)
        elif choice=="10":
            a = float(input("Enter angle in degrees: "))
            result=cosine(a)
        elif choice == "11":
            a = float(input("Enter angle in degrees: "))
            result=tangent(a)
        elif choice == "12":
            a = float(input("Enter number: "))
            result =logarithm(a)
        else:
            print("Invalid choice. Please try again.")
            continue
        print("-------------------------")
        print("Result:", result)
        print("-------------------------")
    except ValueError as error:
        print("Error:", error)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")