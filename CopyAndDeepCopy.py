__author__ = '619635'
import copy
num=['1','2','3','4']
num_copy=copy.copy(num)

num=['6','7','8']

for i in num:
    print(i+"\n")

print("Copy example")

for j in num_copy:
    print(j+"\n")




'''
And copy.deepcopy() is used when you have list objects inside your list
'''