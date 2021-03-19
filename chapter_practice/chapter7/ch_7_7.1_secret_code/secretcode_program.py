# Program to input phrase, convert characters of phrase into parallel arrays of random integers,
# write integers list into cypher.txt.

import random                                               # import random module

phrase = input('Enter phrase: ')                            # get phrase from user
random.seed(2)                                              # set seed constant for random numbers
random_generator = random.sample(range(0, 99), 67)          # create scramble integer list to parallel w/ character
character = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
             "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8",
             "9", "0", ",", ".", "?", "!", " "]             # set list for valid characters

cypher_str = ""                                             # initialize cypher string for cypher.txt output
cypher_lst = []                                             # initialize cypher list for console output

file_doc = open("cypher.txt", "w")                          # open cypher.txt for writing
for letter in phrase:                                       # for loop matching phrase letters to characters to integers
    for char in range(len(character)):
        if letter == character[char]:                       # if statement matching letter to character[index]
            cypher_lst.append(random_generator[char])       # append indexed integer to cypher_lst
            cypher_str += str(random_generator[char]) + "\n"    # concatenate indexed integers to cypher_str
file_doc.write(cypher_str)                                  # write string cypher_str to cypher.txt
file_doc.close()                                            # close cypher.txt
print(cypher_lst)                                           # output coded integers
