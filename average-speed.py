s1=int(input("enter the first number:") )
s2=int(input ("enter the second number: "))
s3=int(input ("enter the third number: "))
avg=(s1+s2+s3)/3
print("avg:",avg)
if s1<avg:
    print(str(s1)+"is slower than avg")
elif s2<avg:
    print(str(s2)+"is slower than avg")
elif s3<avg:
    print(str(s3)+"is slower than avg")
