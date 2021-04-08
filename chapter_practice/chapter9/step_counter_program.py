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
            main()

    for key, vl in dict_day_step.items():
        if vl > max_step:
            max_step = vl
        if vl < min_step:
            min_step = vl
    print()
    print('Your total steps for the week: ' + format(step_count, ',.0f'))
    print('Your average step for the week: ' + format(step_count / len(days), ',.1f') + '\n')

    print('Days with max step of ' + str(max_step) + ':')
    for val in dict_day_step:
        if max_step == dict_day_step[val]:
            print(val)
    print()

    print('Days with min step of ' + str(min_step) + ':')
    for val in dict_day_step:
        if min_step == dict_day_step[val]:
            print(val)
    quit()


main()
