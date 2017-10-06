__author__ = '619635'
num=int(input("Please enter the number:\n"))
print("Please find the list of divisors for this number upto 100\n")
for i in range(1,1000):
    if num%i == 0:
        print(i)
