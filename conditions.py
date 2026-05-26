#write a program to take 2 nos as input and find the largest
'''
num1 = int(input("Enter no1:"))
num2 = int(input("Enter no2:"))

if num1>num2:
    print(num1,"is largest")
elif num1==num2:
    print("both are equal")
else:
    print(num2,"is largest")
'''
#write a program to take input and check whether its even or odd
'''
num = int(input("Enter no:"))
if num%2==0:
    print("Even")
else:
    print("Odd")
'''
#write a program to take 3 sides as input and check whether the traingle they form is equilateral/
#isoceles or scalene
'''
side1 = int(input("Enter No1:"))
side2 = int(input("Enter No2:"))
side3 = int(input("Enter No3:"))
if side1+side2>side3 and side2+side3>side1 and side3+side1>side2:
    if side1==side2==side3:
        print("Equilateral Traingle")
    elif side1==side2 or side2==side3 or side3==side1:
        print("Isoceles Traingle")
    else:
        print("Scalene Traingle")
else:
    print("Invalid Traingle")
'''
#SINGLE LINE IF ELSE
num = int(input("Enter no:"))
print("Even") if num%2==0 else print("Odd")
