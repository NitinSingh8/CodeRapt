# Lecture 7

# String is immutable

                # Concatenation in String

# firstname = "CodeRapt"
# lastname = "Coder"
#
# # result : CodeRapt Coder
#
# # + operator between two string work as concatenation
# name = firstname + " " + lastname
# print(name)


        # Using * operator
# name = "CodeRapt"
# # CodeRaptCodeRapt
# print(name*2)


# Slicing in String

# name = "CODERAPT"
#
# print(name[2:5])
# print(name[-6:-3])
# print(name[-5:-9:-1])
# Task 1 :
# "TPAREDOC"

                # String Formatting

# name = "CodeRapt"
# age = 19

# format()
# print("name = {first}, age = {second}".format(first= name,second = age))

# f string
# print(f"name = {name}, age = {age}")

# join()
# print("".join([name,str(age)]))


                    # String Methods

# 1.lower()
# name = "CodeRapt"
# print(name)
# print(name.lower())

# 2. upper()
# print(name)
# print(name.upper())

# 3. capitalize

# text = "today is rainy day"
# print(text)
# print(text.capitalize())

# 4. title

# text = "today is rainy day"
# print(text)
# print(text.title())

# 5. islower()

# string = "hello"
# print(string.islower())

# 6. isupper()

# string = "HELLO"
# print(string.isupper())

# 7. startswith

name = "CodeRapt"
#
# print(name.startswith("C"))

# 8. endswith

print(name.endswith("Code"))