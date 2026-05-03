# Python
## Some demo work as beginner :
# Check the divisibilty
# code :
print("Put your number below , I will check if it divisible by 3 or 5 or both 3 and 5")
Num = int(input("Wright your number here : "))
if Num % 3 == 0 and Num % 5 == 0:
    print("Divisible by both")
elif Num % 3 == 0:
    print("Divisible by 3")
elif Num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 3 or 5")

