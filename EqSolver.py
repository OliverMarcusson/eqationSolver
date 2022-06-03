import math
from time import sleep
import os

def solve_esys_2():
    print("Please input your values.")
    nX1 = float(input("nX1:"))
    nY1 = float(input("nY1:"))
    c1 = float(input("c1:"))
    nX2 = float(input("nX2:"))
    nY2 = float(input("nY2:"))
    c2 = float(input("c2:"))

    o_nX1 = nX1
    o_nY1 = nY1
    o_c1 = c1
    
    c2 = c2 * (nY1 * -1)
    c1 = c1 * nY2
    nX1 = nX1 * nY2
    nX2 = nX2 * (nY1 * -1)
    nY1 = nY1 * nY2
    nY2 = nY2 * (o_nY1 * -1)
    
    nX = nX1 + nX2
    c = c1 + c2
    
    o_x = round(c / nX, 2)
    if not isinstance(c / nX, int):
        if nX < 0:
            nX = nX * -1
            c = c * -1
        
        x = f"{c}/{nX}"
    else:
        x = c / nX
    
    if not isinstance((o_x + o_c1) / o_nY1, int):
        if o_nY1 < 0:
            o_nY1 = o_nY1 * -1
            o_x = o_x * -1
            o_c1 = o_c1 * -1
        
        y = f"{(o_x + o_c1)}/{o_nY1}"
    else:
        y = (o_x + o_c1) / o_nY1
    
    return x, y

def main(): # Main Loop
    intro = open('intro.txt', 'r', 8192, 'utf-8')
    print(intro.read())
    sleep(2)
    print("\nWhat equation do you want to solve?")
    print("1. 2nd Degree")
    print("2. Exponential")
    print("3. Equation System")
    ans = input("Input: ")

    # 2nd Degree
    if ans == "1":
        print("Equation Structure: ax^2 + px + q = 0\n")

        # Define values
        a = 0  # Makes sure user can't pick zero
        while a == 0:
            a = float(input("a-value: "))
            if a == 0:
                print("variable a cannot be zero. Try again.")

        p = float(input("p-value: "))
        q = float(input("q-value: "))

        # Fix equation for PQ
        p = p / a
        q = q / a

        # Solve PQ
        try:
            x1 = (p * -1) / 2 + math.sqrt((p / 2) ** 2 - q)
            x2 = (p * -1) / 2 - math.sqrt((p / 2) ** 2 - q)

            # Make answers to strings
            x1 = str(x1)
            x2 = str(x2)

            print("Answer: (x1 = " + x1 + ", " + "x2 = " + x2 + ")")

        except ValueError:
            print("There are no real roots.")  # Inga rötter minsann

    # Exponential
    elif ans == "2":
        print("Equation Structure: y = C * a^x\n")
        print("Which variable do you want to solve for? [y, C, a, x]")
        ans = input(":")
        
        if ans == "y":
            print("Please input your values.")
            C = float(input("C: "))
            a = float(input("a: "))
            x = float(input("x: "))

            print("Answer: y = ", C * a ** x)

        if ans == "C":
            print("Please input your values.")
            y = float(input("y: "))
            a = float(input("a: "))
            x = float(input("x: "))

            print("Answer: C = ", y / (a ** x))

        if ans == "a":
            print("Please input your values.")
            y = float(input("y: "))
            C = float(input("C: "))
            x = float(input("x: "))

            print("Answer: a = ", (y / C) ** (1 / x))

        if ans == "x":
            print("Please input your values.")
            y = float(input("y: "))
            C = float(input("C: "))
            a = float(input("a: "))

            print("Answer: x = ", math.log10(y / C) / math.log10(a))

    # Equation System
    elif ans == "3":
        print("This function solves an equation system with two unknowns.")
        print("The structure in use is: nX + nY = c\n")
        sleep(1)
        solution = solve_esys_2()
        print(f"\nx = {solution[0]}\ny = {solution[1]}")

    else:  # If no valid option is chosen
        print("Please input a valid number.")

# Main Program
if __name__ == '__main__':
    main()
