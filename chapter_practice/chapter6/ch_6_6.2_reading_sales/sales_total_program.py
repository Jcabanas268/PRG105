"""
Accumulate sales total and calculate average sales
"""


def main():                                         # define main()
    # data
    total = 0.0                                     # set total accumulator
    line_count = 0                                  # set line counter
    # process
    sales_doc = open('sales_totals-1.txt', 'r')     # open sales_totals-1.txt for read
    for line in sales_doc:                          # iterate process for each line
        line = line.rstrip('\n')                    # strips '\n' symbol
        amount = float(line)                        # convert lines value to float
        total += amount                             # add amount to total
        line_count += 1                             # add one to counter
        print('$' + format(amount, ',.2f'))         # output formatted line for dollar amount
    average = total / line_count                    # calculate for average
    # output total, line_cont, and average
    print('Total: $' + format(total, ',.2f'))
    print('Line count: ' + str(line_count))
    print('Average: $' + format(average, ',.2f'))


main()                                              # call main()
