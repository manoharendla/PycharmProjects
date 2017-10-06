__author__ = '619635'
#Program for room booking
print("Welcome to bella Vista!!")
user=input("May I know your name?\n")
print("Hello "+ user + "!!")
answer=input("How may I help you today:\n")
if 'room' in answer:
    guests=int(input("May I know the number of guests. So that I can accomadate into one or two rooms"))
    if guests <= 2:
        print("We can reserve one room for you")
    elif  2> guests <= 4:
        print("reserving two rooms")
    else:
        print("We don't have enough rooms to accomadate you")





