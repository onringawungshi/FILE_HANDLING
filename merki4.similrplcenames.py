files=open("delhi.txt","w")
files1=open("shimla.txt","w")
files2=open("raipur.txt","w")
files3=open("jaipur.txt","w")
files4=open("other.txt","w")
a=open("people1.","r")
f=a.readlines()
# f=[]
# for j in a:
#     l=j.strip()
#     f.append(l)
# print(l)
i=0
while i<len(f):
    if "delhi" in f[i]:
        files.write(f[i])
        files.write("\n")
    elif "shimla" in f[i]:
        files1.write(f[i])
        files1.write("\n")
    elif "raipur" in f[i]:
        files2.write(f[i])
        files2.write("\n")
    elif "jaipur" in f[i]:
        files3.write(f[i])
        files3.write("\n")
    else:
        files4.write(f[i])
        files4.write("\n")
    i+=1
a.close()


# f=open("o.txt","r")
# f1=f.read()
# print(f1)
# f.close()

# f=open("people1.","r")
# f1=f.readlines()
# c=0
# for i in f1:
#     print(c)
#     c+=1

# with f1 open as ""