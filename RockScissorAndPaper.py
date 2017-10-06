__author__ = '619635'
import sys

option=["rock", "scissor", "paper"]

def compare(user1,user2):
    if user1 == user2:
        print("its a tie exiting")
    elif user1 == "rock":
        if user2 == "scissor":
            print("User 1 has won")
        else:
            print("User 2 has won")
    elif user1 == "scissor":
        if user2 == "paper":
            print("user 1 has won")
        else:
            print("User 2 has won")
    elif user1 == "paper":
        if user2 == "rock":
            print("user1 has won")
        else:
            print("user2 has won")
    else:
        print("wrong input, please choose one option from rock, scissor or paper")


res=input("Would you like to play the game yes or no \n")
res=str.lower(res)
if res == "yes":
    user1=input("Please choose Rock, scissor or paper for user1")
    user2=input("Please choose Rock, scissor or paper for user2")

    user1=str.lower(user1)
    user2=str.lower(user2)

    print(user1)
    print(user2)

    if user1 and  user2  in option:
        compare(user1,user2)
    else:
        print("wrong input")


else:
    print("exiting the game")
    sys.exit()


