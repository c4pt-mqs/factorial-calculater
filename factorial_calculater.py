while True:
    try:
        def my_first_num():
            firstNum = int(input("Enter your number: "))

            # ---------------- Calculate the Factorial ----------------#
            factorial = 1
            if firstNum < 0:
                print("The factorial of negative numbers cannot be calculated. ")
            elif firstNum == 0:
                print("1")
            elif firstNum:
                for i in range(1, firstNum + 1):
                    factorial = factorial * i
                print("Factorial of the number: ", factorial)

            # ---------------- Print the Numbers (side by side) ----------------#
            while firstNum >= 1:
                print(*range(firstNum, 0, -1), sep=" ")

                firstNum -= 1

        if __name__ == "__main__":
            my_first_num()

    except ValueError:
        print("You entered wrong. Please try again!")
