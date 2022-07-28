# Lecture 29

# Regular Expression

import re

# print(re.__doc__)

# method :
# match => sentence must be start with pattern
# search => sentence / word  must have that pattern
# findall => return a list
# sub => replace the data


# sentence = "human being human"
#
# pattern = r"human being human"
#
# ismatch  = re.fullmatch(pattern, sentence)
#
# print(bool(ismatch))


# sentence = "Human being Human Habcn"
#
# pattern = r"H...n"
#
# elements = re.findall(pattern, sentence)
# print(elements)

sentence = "My Laptop have 256gb ssd and hard disk is 128gb"

new_sentence = re.sub('...gb','512gb',sentence)

print(new_sentence)

