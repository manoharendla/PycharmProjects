__author__ = '619635'
print("Welcome to the Menu")
print("1. View the Menu")
print("2. Add to the Menu")
print("3. Remove item from Menu")
print("9. Exit from the Menu")

menu_list=[]
while True:
    menu_item=int(input("Pleas select your option "))
    if menu_item==1:
        current=0
        if len(menu_list)>0:
            while current<len(menu_list):
                print(int(current)+1,".",menu_list[current])
                current= current+1

        else:
            print("menu is empty")
    if menu_item==2:
        item_name=input("Please enter the item to add to the menu\n")
        menu_list.append(item_name)
    if menu_item==3:
        item_name=input("Please enter the item name to be removed\n")
        if item_name in menu_list:
            item_index=menu_list.index(item_name)
            menu_list.remove(item_index)
    if menu_item==9:
        print("Exiting..")
        break

