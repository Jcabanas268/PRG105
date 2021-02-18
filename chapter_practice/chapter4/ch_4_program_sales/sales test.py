# data var
sel_week = 1
get_day_sales = 0
day_total = 0
sale_total = 0
week_total = 0
avg_per_day = 0
week = 'Select the day of the week.\n' \
       '(Sun 1) \t (Mon 2) \t (Tue 3) \t (Wed 4) \t (Thu 5) \t (Fri 6) \t (Sat 7)\nEnter done to exit: '


# processing
sel_day = input(week)

if sel_day == 'done':
    print('Thank you happy done')
    print(sale_total)

    print(avg_per_day)

else:
    if sel_day == '1':
        print('Sunday')
    if sel_day == '2':
        print('Monday')
    if sel_day == '3':
        print('Tuesday')
    if sel_day == '4':
        print('Wednesday')
    if sel_day == '5':
        print('Thursday')
    if sel_day == '6':
        print('Friday')
    if sel_day == '7':
        print('Saturday')
    get_day_sales = (float(input('Enter total sales: $ ')))
    while sel_day == '1':
        sun_sales = get_day_sales
        sale_total += get_day_sales
        print('$', format(sun_sales, ',.2f'))
        sel_day = input(week)


while sel_day == '2':
    print('Monday')
    mon_sales = get_day_sales
    sale_total += get_day_sales
    sel_day = input(week)

while sel_day == '3':
    print('Tuesday')
    tue_sales = get_day_sales
    sale_total += get_day_sales
    sel_day = input(week)

while sel_day == '4':
    print('Wednesday')
    wed_sales = get_day_sales
    sale_total += get_day_sales
    sel_day = input(week)

while sel_day == '5':
    print('Thursday')
    thu_sales = get_day_sales
    sale_total += get_day_sales
    sel_day = input(week)

while sel_day == '6':
    print('Friday')
    fri_sales = get_day_sales
    sale_total += get_day_sales
    sel_day = input(week)

while sel_day == '7':
    print('Saturday')
    sat_sales = get_day_sales
    sale_total += get_day_sales
    sel_day = input(week)

avg_per_day /= (sun_sales + mon_sales + tue_sales + wed_sales + thu_sales + fri_sales + sat_sales)





