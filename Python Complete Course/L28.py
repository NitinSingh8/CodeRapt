# Lecture 28

# open:
# open(path, mode)

# mode : 'w' , 'r' ,'rb' ,'wb' ,'a' , 'r+'
# w - > 1. textfile.txt
#         2. delete all the data from file and open the empty file


# opening a file
# try:
#     file = open('textfile.txt','w')
#
#     print("file created /opened successfully")
#
# except:
#     print("some error occur")


# writing into the file

# try:
#     file = open('textfile.txt','a')
#
#     # print("file created /opened successfully")
#
#     data = "\nthis is a new line"
#
#     val = file.write(data)
#     print(val)
#
#
#
#     file.close()
# except:
#     print("some error occur")



# reading the data
try:
    file = open('textfile.txt','r')

    # print("file created /opened successfully")

    #read

    # data = file.read()
    # print(data)

    #readline
    # data = file.readline()
    # print(data)

    # readlines

    # data = file.readlines()
    # print(data)

    # read with parameter
    # data = file.read(11)
    # print(data)

    print(file.tell())
    # seek()
    file.seek(15)


    print(file.tell())

    data = file.read(12)
    print(data)

    file.close()

except:
    print("some error occur")