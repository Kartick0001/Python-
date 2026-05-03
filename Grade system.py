#Grade students based on marks
print("Know your grade according to your marks")
mks = float(input("Enter your marks : "))
if(mks>=90):
    print("your grade is : A ")
elif(mks<90 and mks>=80):
    print("your grade is : B ")
elif(mks<80 and mks>=70):
    print("your grade is : C ")
else:
    print("your grade is : D ")
