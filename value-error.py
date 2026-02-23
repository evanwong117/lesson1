try:
    number=int(input("Please enter the number: "))
    print("The number entered is", number)
except ValueError as ex:
    print("Exception", ex)
try:
    number=int(input("Please enter the number: "))
    print("The number entered is", number)
except ValueError:
    print("Please enter number only")
