<<<<<<< HEAD
l=[4, 5, 1, 2, 9, 7, 10, 8]
print("Original List :", l)
count=0
for i in l:
    count += i
avg = count/len(l)
print("sum = ", count) 
print("average = ", avg)
l.sort()
print("Smallest element is: ", l[0])
=======
l=[4, 5, 1, 2, 9, 7, 10, 8]
print("Original List :", l)
count=0
for i in l:
    count += i
avg = count/len(l)
print("sum = ", count) 
print("average = ", avg)
l.sort()
print("Smallest element is: ", l[0])
>>>>>>> 244e2e89971618a4f80030cf20f2dc61aa3d5bcd
print("Largest element is: ", l[-1])