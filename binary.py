f=open("lily.jpg","rb")
# f.read()
f1=open("ma.jpg","wb")
for i in f:
    f1.write(i)
print(f1)
f.close()
# print(f)