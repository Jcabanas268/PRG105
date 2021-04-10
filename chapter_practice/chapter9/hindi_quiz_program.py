"""
hindi_quiz_program has dictionary of numbers 0-10 with values in hindi,
user is prompted to enter digit equivalent to value,
user is given feedback for value,
score is evaluated, and displayed.
"""

import random           # import random functions
random_number = random.sample(range(0, 11), 11)         # generate random series for place key
numbers_share = {0: 'shunya', 1: 'ek', 2: 'do', 3: 'teen', 4: 'chaar', 5: 'paanch',
                 6: 'che', 7: 'saat', 8: 'aath', 9: 'nau', 10: 'das'}           # set dictionary key, val
letter_grade = {11: "A", 10: "A-", 9: "B-", 8: "C-", 7: "D", 6: "F",
                5: "F", 4: "F", 3: "F", 2: "F", 1: "F", 0: "F"}        # set dictionary point key, letter value
score = 0       # set score
print("Enter a digit which corresponds to the number in Hindi\n")       # prompt

for channel in random_number:       # for random series number
    for key, val in numbers_share.items():      # for key and value in dictionary
        if channel == key:          # if random series number match key in dictionary
            guess = (input("What is the equivalent of " + val + " : "))     # user prompt the value of dictionary key
            while not int(guess.isdigit()):     # if/while user input value is not a digit
                print()
                print("Please enter a valid digit.")    # prompt
                guess = (input("What is the equivalent of " + val + " : "))     # attempt user error
            else:           # or else
                if channel == int(guess):       # if random number match user input
                    score += 1          # add 1 to score value
                    print("\t" + "Correct!: " + val + " is " + str(guess) + ".\n")          # prompt guess is correct
                else:           # if random number do not match user input
                    print("\t" + "Incorrect!: " + val + " is " + str(channel) + ".\n")      # prompt guess is incorrect

for points, letter in letter_grade.items():         # for point and letter in letter_grade dictionary
    if points == score:         # if point key match score value
        print("Your final score is: " + str(score) + "/11")         # display score
        print("You got an " + letter + ".")         # display letter grade
