<<<<<<< HEAD
weather=(0,0,0,0,0,0,1)
rainy=0
sunny=0
for i in range(0,7):
    if (weather[i]==0):
        rainy+=1
    else:
        sunny+=1
if(sunny>rainy):
    print("Good weather")
else:
=======
weather=(0,0,0,0,0,0,1)
rainy=0
sunny=0
for i in range(0,7):
    if (weather[i]==0):
        rainy+=1
    else:
        sunny+=1
if(sunny>rainy):
    print("Good weather")
else:
>>>>>>> 04c4823476da5f534fd3da23bb500e70daae35fa
    print("Bad weather")