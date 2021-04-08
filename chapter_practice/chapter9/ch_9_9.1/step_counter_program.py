"""
Step counter program allows users to input step count for days of the week,
displaying total amount of steps, average number of steps,
and maximum/minimum amount of steps with corresponding days.
"""
print('Please enter your number of steps for the following days of the week.')      # prompt 


def main():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']       # list for days
    dict_day_step = {}      # dictionary for days key and step value
    step_count = 0      # initialize step total
    max_step = 0        # initialize max step
    min_step = 999999       # initialize min step
    for day in days:        # for each day  in days list
        steps = input('Enter step count for ' + day + ': ')     # get step count for following day
        if steps.isdigit():             # if step count is a digit
            dict_day_step[day] = int(steps)     # add day key with step value
            step_count += int(steps)        # accumulate steps for total
        else:           # if step is not a digit
            print()
            print('Error! ' + '\"' + steps + '\"' + ' value is invalid.\n')     # prompt value is invalid
            print('Please enter step count, value must be a number.')       # prompt value must be a number
            main()         # loop to main

    for key, vl in dict_day_step.items():       # for key and value in dictionary
        if vl > max_step:       # if value is greater than max step
            max_step = vl       # set max step as value
        if vl < min_step:       # if value is less than min step
            min_step = vl       # set min step as value
    print()
    print('Your total steps for the week: ' + format(step_count, ',.0f'))       # output total steps for the week
    print('Your average step for the week: ' + format(step_count / len(days), ',.1f') + '\n')   # output average steps for the week

    print('Days with max step of ' + str(max_step) + ':')       # print max step for following days
    for val in dict_day_step:       # for day in dictionary
        if max_step == dict_day_step[val]:      # if max step equals day value in dictionary
            print(val)      # print day of week
    print()

    print('Days with min step of ' + str(min_step) + ':')       # for day in dictionary
    for val in dict_day_step:           # for day in dictionary
        if min_step == dict_day_step[val]:      # if min step equals day value in dictionary
            print(val)      # print day of week
    quit()      # end program


main()          # call main
