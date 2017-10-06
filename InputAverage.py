__author__ = '619635'
avg_list=[]
for i in range(3):
    a=int(input("enter a: \n"))
    b=int(input("enter b: \n"))
    c=int(input("enter c: \n"))
    x=int(input("enter x: \n"))
    print("Check")
    print(str(a)+""+str(b)+""+str(c)+""+str(x))
    if (a+b+c) <= x:
        print("Checking the average")
        avg_list.append([a,b,c])
    for j in avg_list:
        print(j)

mod_list=[]

for k in avg_list:
    if k not in mod_list:
        mod_list.append(k)

print("Mod List")
for m in mod_list:
    print(m)

print("final List with ascending order")
asc_list=mod_list.sort()

for n in mod_list:
    print(n)
