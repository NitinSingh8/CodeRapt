sentence = input()  # taking the sentence from user

word_list = sentence.split()  # converted sentence int word list using split() method

cnt = 0
for word in word_list:          # used for loop to iterate over every word in word list
    if len(word) > 2 and word[0] == word[-1]:  # checking both condition
        cnt += 1                                # if condition true then increment cnt

print(cnt)  # At last printing the output to user
