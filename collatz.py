__author__ = '619635'

num =0
def collatz(number):
    return_value=0
    if number%2 == 0:
        return_value=number//2
    elif number%2 == 1:
        return_value= 3*number + 1
    return return_value



while num!=1:
    try:
        num=int(input("Please enter a number"))
    except ValueError :
        num=0
        print("input number not an integer")
    if num == 1:
        print("Got  key to exit")
    renum=collatz(num)
    print(renum)





