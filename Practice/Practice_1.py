import time
from math import sqrt
print(">>>=== Mini Calculator ===<<<")
print("\n")
name = input("Enter your name: ")
while True:
    print("\n\n")
    print("Options ===>")
    time.sleep(.5)
    print("1. Square Root & Power")
    time.sleep(.5)
    print("2. Arithmatic (+, -, *, /)")
    time.sleep(.5)
    print("0. Exit")
    time.sleep(.5)
    opt = int(input(f"{name}, Choose your option: "))
    
    print("\n")
    
    if opt == 1:
        time.sleep(.5)
        print("a. Square Root")
        time.sleep(.5)
        print("b. Power")
        time.sleep(.5)
        choise = input("Choose your option (a or b): ")
        if choise == 'a':
            n = float(input("Enter any number: "))
            print(f"Square root of {n} is = {sqrt(n)}")
            
        elif choise == 'b':
            base = float(input("Enter base: "))
            exponent = float(input("Enter exponet: "))
            print(f"{base} to the power {exponent} is = {pow(base, exponent)}")
        else:
            print("Invalid choise!!!")
            
    elif opt == 2:
        time.sleep(.5)
        print("a. Addition")
        time.sleep(.5)
        print("b. Substraction")
        time.sleep(.5)
        print("c. Multiplication")
        time.sleep(.5)
        print("d. Division")
        time.sleep(.5)
        choise = input("Choose your option (a, b, c, d): ")
        
        if choise == 'a':
            print("Enter two numbers here === >>>")
            n1 = float(input("Enter number_1: "))
            n2 = float(input("Enter number_2: "))
            print(f"{n1} + {n2} = {n1+n2}")
            
        elif choise == 'b':
            print("Enter two numbers here === >>>")
            n1 = float(input("Enter number_1: "))
            n2 = float(input("Enter number_2: "))
            print(f"{n1} - {n2} = {n1-n2}")
            
        elif choise == 'c':
            print("Enter two numbers here === >>>")
            n1 = float(input("Enter number_1: "))
            n2 = float(input("Enter number_2: "))
            print(f"{n1} × {n2} = {n1*n2}")
            
        elif choise == 'd':
            print("Enter two numbers here === >>>")
            n1 = float(input("Enter number_1: "))
            n2 = float(input("Enter number_2: "))
            print(f"{n1} ÷ {n2} = {n1/n2}")
            
        else:
            print("Invalid Choise!!!")
            
    elif opt == 0:
        print(f"Thanks {name} For Using Calculator 😊")
        time.sleep(.5)
        print("Exiting Program.....")
        for i in range(4):
            print(".")
            time.sleep(.5)
        print("Programe Closed")
        
        break
            
    else:
        print("Invalid Option Choise!!!")
        time.sleep(.2)
        print(f"Oh no {name}... What Have You Done?!!!")
        for i in range(3):
            print(".")
            time.sleep(.5)
        print("Program Is Closing...")
        for i in range(3):
            print(".")
            time.sleep(.5)
        print("Program Closed")
        break
    
