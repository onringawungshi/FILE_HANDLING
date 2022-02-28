banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
file=open("file.q3.txt","w")
i=0
while i<len(banks_list):
    file.write(banks_list[i])
    file.write("\n")
    i+=1