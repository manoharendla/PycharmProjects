__author__ = '619635'

def findGrade(percent):
    if int(percent) >= 90:
        return "A"
    elif int(percent) in range(80,90) :
        return  "B"
    elif int(percent) in range(0,70) :
        return  "C"

num=input("Please enter the percentage for the grade to be found")
per=findGrade(num)
print(per)
