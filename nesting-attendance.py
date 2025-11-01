medical_cause=input("did you have a medical cause Y or N:")

if medical_cause=='Y':
    print("You are allowed")
else:
    atten=int(input("enter the attendance of the student:"))
    if atten>=75:
        print("Allowed")
    else:
        print("Not allowed")