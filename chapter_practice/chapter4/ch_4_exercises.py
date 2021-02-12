"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section in your textbook that explain the required code
    Your file should compile error free
    Submit your completed file
"""
# TODO 4.2 A condition controlled loop
print("=" * 10, "Section 4.2 condition controlled loop", "=" * 10)
# write a loop that will change the variable in num by subtracting 1
# then print the variable. Keep looping until the num = 0: while num > 0
num = 10
# write your code here, the variable needs to exist before you start the loop
while num > 0:      # when num is greater than 0
    print(num)      # print current num
    num -= 1        # reduce num value by 1


# TODO 4.3 the For Loop
print("=" * 10, "Section 4.3 for loop", "=" * 10)
# Use a for loop with a list of the days of the week,
# print each day of the week
for day in ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'):   # draw list of day
    print(day)


# TODO 4.3 the for loop - range function
print("=" * 10, "Section 4.3 using range() in a for loop", "=" * 10)
# use the range function to print the numbers from 1 to 10
for num in range(1, 11):    # draw range of num
    print(num)


# TODO 4.4 a running total
print("=" * 10, "Section 4.4 running total", "=" * 10)
# Use a loop to have the user enter 5 numbers, provide a total at the end
# You will need to initialize your accumulator before entering the loop
# You can assume valid integers are entered
num_count = 0
total = 0
while num_count < 5:                                # set the limit of num_count
    num1 = int(input('Enter number: '))             # get number
    total = total + num1                            # add number to total
    num_count += 1                                  # initiate count up to num_count limit
print(total)                                        # print total


# TODO 4.5 Sentinel Value
print("=" * 10, "Section 4.5 sentinel value", "=" * 10)
# Create a variable to store a total amount
# Create a variable to store a count of the numbers entered
# Use a loop to have the user enter test scores until a
# sentinel value of -1 is entered.
# After the loop, display the total, the count and the average (total / count)
score = 0
total = 0
count = 0
done = 0
print('Enter \"done\" when you are finished')               # instruction to finish
while done != -1:                                           # while input is not finished
    in_score = (input('Enter test score: '))                # get test score
    if in_score == 'done':                                  # when in_score = done
        done = -1                                           # done is set to finish
        print('Finished entering scores.')                  # print end of input
    else:                                                   # when in_score != done
        score = float(in_score)                             # convert in_score to float score
        count += 1                                          # raise count amount
        total = total + score                               # add score to total

print('You entered ' + str(count) + ' test scores.')        # print number of test scores entered
print('Your total score is ' + str(total) + '.')            # print total of test scores entered
print('Your average score is ', format((total / count), ',.2f'), '.')  # print average of test scores entered


# TODO 4.6 validating data
print("=" * 10, "Section 4.6 data validation loop", "=" * 10)
# Ask the user to enter a number between 1 and 10.
# Use a while loop to force the user to repeat the
# prompt until the user enters a valid number. Test with
# both valid and invalid data

num = int(input('Enter a number from 1 though 10: '))              # get num
while num < 1 or num > 10:                                        # while 1 > num > 10
    print('Error')                                                # print error
    num = int(input('Enter a valid number from 1 though 10: '))    # prompt to get valid num
