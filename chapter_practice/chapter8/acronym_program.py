"""
Program accepts a phrase and returns the acronym.
"""


def main():             # define main function
    again = True        # set repeat again value as true
    while again:        # run line while again is true
        user_phrase = input("Enter phrase: ")       # get phrase from user
        users_phrase_split = user_phrase.split()        # split phrase to list
        acronym = ""        # initialise acronym compiler
        for ln in users_phrase_split:       # for statement each line in phrase list
            acronym += ln[0] + "."      # adds first index letter of line to compiler
        print(acronym.upper())      # output acronym
        repeat_program = input("Press Y to enter another phrase: ")     # prompt to repeat program
        if repeat_program.upper() == "Y":       # if user input equals Y for continue
            again = True        # set repeat again as true
        else:       # if user input does not equal Y
            quit()      # quit program


main()      # call main function
