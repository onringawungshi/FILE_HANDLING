import os
def file_size(filename):
        f= os.stat("appfil.py")
        return f.st_size
print("File size in bytes of a plain file: ",file_size("test.txt"))
