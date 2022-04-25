f=open("co.txt","r")
f1=f.read()
c,b,x=0,0,0
for i in f1:
    if str.isupper(i):
        c+=1
    if str.islower(i):
        b+=1
    if str(i) not in ("a","e","i","o","u","A","E","I","O","U") and str(i)!=" ":
        x+=1
print("uppercase",c)
print("lowercase",b)
print("consonant",x)