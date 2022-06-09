num = []  # create an empty list

for i in range(10):  # Used for loop to take input 10 times from user
    n = int(input())
    num.append(n)  # adding every number in list

myset = set(num)  # created a set from list num by typecasting

for val in myset:
    # use count() method which return no of occurrence in list
    print(f"Occurrence of {val} : ", num.count(val))
