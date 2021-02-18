# sales program
# data var
total_sales = 0


# processing
for day in ('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'):       # run through list
    get_day_sales = float(input('Enter day sales for ' + day + ': $ '))         # input sale for day
    total_sales += get_day_sales        # add day sale to total
avg_sales = total_sales / 7     # getting average sale per day

# output
print('Total sales for week: $' + format(total_sales, ',.2f'))      # print total
print('Average sales per day: $ ' + format(avg_sales, ',.2f'))      # print average
