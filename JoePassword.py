__author__ = '619635'
while True:
    print("Please enter the userName: ")
    user_name=input()
    if user_name != 'Joe':
        continue
    print("Welcome Joe !! Enter your password to continue")
    count=0
    while True:
        password=input()
        if password != 'Joe':
            count=count+1
            if count == 1:
                time='first'
            elif count == 2:
                time='Second'
            elif count == 3:
                time='third'
            else:
                print("You have crossed maximum attempts to login !!")
                break
            print("Hey Joe!! You have entered a wrong password and it is your "+ time + "attempt" )
            continue
        print("Joe successfully authenticated" )
        break
    break



