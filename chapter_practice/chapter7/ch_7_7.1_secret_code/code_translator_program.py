# Program reads coded cypher.txt, decrypt and output to console plain message

import random                                           # import random module
random.seed(0)                                          # set seed constant for random numbers
random_generator = random.sample(range(0, 99), 67)      # create scramble integer list to parallel w/ character
character = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
             "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8",
             "9", "0", ",", ".", "?", "!", " "]         # set list for valid characters


def main():                                                     # define main()
    try:                                                        # try statement
        name_doc = input("Enter document name: ") + ".txt"      # get document name from user
        open_doc = open(name_doc, "r")                          # open cypher.txt for writing
        file_doc = open_doc.readlines()                         # value to hold cypher.txt contents
        decoder = ""                                            # initialize decoder message
        for line in file_doc:                                   # for loop lines of cypher.txt
            strip_line = int(line.rstrip())                     # value to strip \n and hold line as integer
            for digit in range(len(random_generator)):          # for loop range of random_generator
                if strip_line == random_generator[digit]:       # if item in cypher.txt matches item in
                                                                # random_generator indexed list
                    decoder += character[digit]                 # compile corresponding index of character to
                                                                # random_generator matched index
        open_doc.close()                                        # close cypher.txt
        print('Message:', decoder)                              # output plain message
    except Exception as error:                                  # exception to print error, resume main()
        print("Error: ", error)                                 # output error message
        print()
        main()                                                  # resume main()


main()                                                          # call main()
