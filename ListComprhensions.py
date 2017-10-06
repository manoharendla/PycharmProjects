__author__ = '619635'
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
a_new = []
for i in a:
    if i%2 == 0:
        a_new.append(i)

print(*a_new,sep="\n")


print("*"*30)


even_list=[ even for even in a if even%2 == 0]

print(*even_list,sep="\n")



