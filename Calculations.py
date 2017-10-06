__author__ = '619635'
print("Program for basic calculator:")
x=input("Please enter the value of X:")
y=input("Please enter the value of Y:")
z=input("What type of calculations do you want to make add, sub, mul, division :")

if "add" in z:
    print(type(x))
    print("Performing an addition between x and y and the value is :" + str(int(x)+int(y)))
elif "sub" in z:
    print("Performing an subtraction between x and y and the value is :" + str(int(x-y)))
elif "mul" in z:
    print("Performing an mul between x and y and the value is :" + str(int(x*y)))
elif "div" in z:
    print("Performing an div between x and y and the value is :" + str(int(x/y)))
elif "exp" in z:
    print("Performing an exp between x and y and the value is :" + str(int(x**y)))
else:
    print("Nothing to do")

