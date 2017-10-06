__author__ = '619635'

import random

num=random.randint(1,10)

while True:
    provideinput=int(input("Please provide your input\n"))
    if provideinput > num:
        print("your number is higher than the guess number\n")
    elif provideinput < num:
        print("your number is smaller than the guess number\n")
    else:
        print("Good you have guessed the number and the number is:",num)

