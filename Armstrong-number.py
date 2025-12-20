num=int(input("Enter a number: "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    print("digit =", digit)
    sum += digit **3
    print("sum =",sum)
    temp //=10
    print("temp =", temp)
if num==sum:
    print(num," is an Armstrong number")
else:
    print(num,"is not an Armstrong number")