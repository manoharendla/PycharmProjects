__author__ = '619635'
a=[2,5,21,0,1,9,7]
for i in a:
    print("before sorting "+str(i))

a.sort()
for i in a:
    print("after sorting " + str(i))

print("Print in reverse order:")
a.sort(reverse=True)

for j in a:
    print(str(j))

