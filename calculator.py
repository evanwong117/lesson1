def add(num1, num2):
    a=num1+num2
    print("addition of 2 numbers is ", a )
def sub(num1, num2):
    b=num1-num2
    print("subtraction of 2 numbers is ", b )
def mul(num1, num2):
    c=num1*num2
    print("multiplication of 2 numbers is ", c )
def div(num1, num2):
    d=num1/num2
    print("division of 2 numbers is ", d )
print("Please select your operation")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")
choice=input("Please enter choice (a/ b/ c/ d/):")
num1=int(input("Please enter the first number: "))
num2=int(input("Please enter the second number: "))
if choice=="a":
    add(num1,num2)
elif choice=="b":
    sub(num1, num2)
elif choice=="c":
    mul(num1,num2)
elif choice=="d":
    div(num1,num2)
else:
    print("invalid input")

