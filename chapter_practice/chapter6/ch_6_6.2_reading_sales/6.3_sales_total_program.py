"""
Accumulate sales total and calculate average sales
"""


def main():  # define main()
    # data
    total = 0.0  # set total accumulator
    line_count = 0  # set line counter
    try:
        # process
        print('Available files:\n\tsales_totals-1 \n\tsales_error')  # prompt user available files
        select_file = input('Enter file name: ')  # get file name
        file_name = (select_file + '.txt')  # link file name to document
        sales_doc = open(file_name, 'r')  # open sales_totals-1.txt for read
        for line in sales_doc:  # iterate process for each line
            line = line.rstrip('\n')  # strips '\n' symbol
            amount = float(line)  # convert lines value to float
            total += amount  # add amount to total
            line_count += 1  # add one to counter
            print('$' + format(amount, ',.2f'))  # output formatted line for dollar amount
        average = total / line_count  # calculate for average
        # output total, line_cont, and average
        print('Total: $' + format(total, ',.2f'))
        print('Line count: ' + str(line_count))
        print('Average: $' + format(average, ',.2f'))
        print()
        start_again()  # call function to continue/exit program
    except ValueError as err:  # print value error found
        print('Line ' + str(line_count) + ' ' + str(err))
        print()
        start_again()  # call function to continue/exit program
    except Exception as err:  # print error and continue to main
        print('Error!', err)
        print()
        main()


def start_again():  # function to continue/exit program
    start_over = input('Do you want to select another file?: ')
    if start_over == 'yes':  # continue to main
        print()
        main()
    elif start_over == 'no':
        exit_program = input('Do you want to exit? ')  # prompt to exit
        if exit_program == 'yes':  # quit program
            quit()
        elif exit_program == 'no':
            start_again()
        else:  # prompt for valid entry/ request to continue
            print('Please select a valid entry.')
            print()
            start_again()
    else:
        print('Please select a valid entry.')  # prompt for valid entry/ request to continue
        print()
        start_again()


main()  # call main()
