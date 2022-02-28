f=open("shimla.txt","r")
line=0
words=0
char=0
for i in f:
    a=i.split()
    line+=1
    words+=len(a)
    char+=len(i)
print(line)
print(words)
print(char)