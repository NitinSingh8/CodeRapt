# Lecture 26

# SynatxError:
#
# print("hello")
#
# if 10<20:
#     print("10 is less than 20")



# Exception:
nums = [10,20,30,40]

try:
    # n = int(input("Enter the number : "))
    #
    # print(nums[n])
    # print(3+"s") # type error

    # a = 10
    # b = 0
    # print(a/b) # zerodivision errro
    print("Simple Statement")


except IndexError:
    print("Exception came")
except (ZeroDivisionError,TypeError):
    print("Exception came of zerodivision/TypeError")
except:
    print("All exception handle")

finally:
    print("Hello this is finally block")