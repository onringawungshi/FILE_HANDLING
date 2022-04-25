f = open("hobby.txt","w")
h = [ ]
for i in range(5):
       n = input("Enter hobby name:")
       h.append(n)
       h.append()
f.writelines(h)
f.close()
print(f)