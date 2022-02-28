# A file is a named location on disk to store related information.
# File is a collection of data that is available to a program. We can retrieved and used data stored
# in a file whenever we required.
# The file handling plays an important role when the data needs to be stored permanently into the file.

# --Advantages--

# 1.Stored data is permanent unless someone removed it.
# 2.It is possible to remove or update a data.

# Two types of files--

# 1.Text file-It stores data in the form of characters. It is used to stores character and strings.
# 2.Binary file-It stores data in form of bytes, a group of eight bits each.It is used to stored images,
#   text,pdf,csv,video and audio.
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)


# If a file doesn't exist ,a new file is created.
# If a file already exists, it iaa overwritten.

# readlines()-this method return a list containing each line of the file.
# writelines()-this method writes the items of a list to a file.

# There are four different methods (modes) for opening a file:

# 'r' for reading – The file pointer is placed at the beginning of the file. This is the default mode.
# 'r+' Opens a file for both reading and writing. The file pointer will be at the beginning of the file.
# 'w' Opens a file for writing only. Overwrites the file if the file exists.
#     If the file does not exist, creates a new file for writing.
# 'w+'Opens a file for both writing and reading. Overwrites the existing file if the file exists.
#     If the file does not exist, it creates a new file for reading and writing.
# 'rb'Opens a file for reading only in binary format.
#     The file pointer is placed at the beginning of the file.
# 'rb+'Opens a file for both reading and writing in binary format.
# 'wb+'Opens a file for both writing and reading in binary format.
#      Overwrites the existing file if the file exists. If the file does not exist,
#      it creates a new file for reading and writing.
# 'a' Opens a file for appending. The file pointer is at the end of the file if the file exists. 
#     That is, the file is in the append mode. If the file does not exist,
#     it creates a new file for writing.
# 'ab'Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. 
#     That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.
# 'a+'Opens a file for both appending and reading. The file pointer 
#     is at the end of the file if the file exists. The file opens in the append mode.
#     If the file does not exist, it creates a new file for reading and writing.
# 'ab+'Opens a file for both appending and reading in binary format. 
#      The file pointer is at the end of the file if the file exists. The file opens in the append mode.
#      If the file does not exist, it creates a new file for reading and writing.
# 'x' open for exclusive creation, failing if the file already exists (Python 3)

