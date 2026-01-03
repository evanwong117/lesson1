prime=int(input("Please enter the numbers: "))
flag=False
for i in range (2,prime):
    if (prime % i)==0:
        flag=True
        break
if flag:
    print("This is not a prime number")
else:
    print("This is a prime number") 
