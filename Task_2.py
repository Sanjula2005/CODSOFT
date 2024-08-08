import task2_Ascii_art
import os

print(task2_Ascii_art.art)
print("Welcome to our digital Calculator!!")



def CALC():
    a = int(input("Please enter the first operand: "))
    b = int(input("Please enter the second operand: "))
    def Calculator(a,b):
        operators={"add":"+","subtract":"-","multiply":"*","divide":"/"}
        print(operators)
        op=input("Pick an operation from the above list: ")
        if op=="+":
            ans=a+b
            print(f"{a}{op}{b}={ans}")
        elif op=="-":
            ans=a-b
            print(f"{a}{op}{b}={ans}")
        elif op=="*":
            ans=a*b
            print(f"{a}{op}{b}={ans}")
        elif op=="/":
            ans=a/b
            print(f"{a}{op}{b}={ans}")

    Calculator(a,b)
    print("Thank you for using our Calculator")

CALC()


