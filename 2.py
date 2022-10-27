kingdom_name = input("enter the kingdom name")
# print(kingdom_name[-1])

if kingdom_name[-1] == 'a'or kingdom_name[-1] == 'e' or kingdom_name == 'i' or kingdom_name =='o'or kingdom_name=='u':
    print("Alice's Kigdom")
elif kingdom_name[-1] =='y':
    print("No ruler")
else:
    print("Bob's Kingdom")
