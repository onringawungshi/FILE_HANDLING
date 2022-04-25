user=input("enter filename:")
user.split()
i=0
while i<len(user):
    if user[i]!=".":
        user.remove(user[i])
    elif user[i]==".":
        break
    i+=1
print(user)