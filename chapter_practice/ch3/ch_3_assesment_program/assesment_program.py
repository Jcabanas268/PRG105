# assessment_program_play_tickets
# data variable
# customer
general = 10.00
student = 5.00
senior = 6.00
veteran = 7.00
sponsor = 2.00
# maths variable
discount_10 = .90
discount_15 = .85
discount_20 = .80
total = 0

# get customer status
customer = input('1) General Admission   $ 10.00 \n2) Student   $ 5.00 \n3) Senior   $ 6.00 \n'
                 '4) Veteran   $ 7.00 \n5) Sponsor   $ 2.00 \nSelect Customer Option 1-5: ')
ticket_count = int(input('How many tickets: '))     # get number of tickets

# general admission processing
if customer == '1':
    total = ticket_count * general                      # total price of ticket
    b4_discount = total
    print('Your total is: $', total)                    # print total price
    if 4 < ticket_count < 8:                            # discount by number of tickets
        total *= discount_10
    if 9 < ticket_count < 15:
        total *= discount_15
    if 15 < ticket_count:
        total *= discount_20
    print('Your grand total after discount is: $', format(total, ',.2f'))       # total after discount
    b4_discount -= total
    print('You saved: $', format(b4_discount, ',.2f'))                          # total savings

# student admission processing
if customer == '2':
    total = ticket_count * student
    b4_discount = total
    print('Your total is: $', total)
    if 4 < ticket_count < 8:
        total *= discount_10
    if 9 < ticket_count < 15:
        total *= discount_15
    if 15 < ticket_count:
        total *= discount_20
    print('Your grand total after discount is: $', format(total, ',.2f'))
    b4_discount -= total
    print('You saved: $', format(b4_discount, ',.2f'))

# senior admission processing
if customer == '3':
    total = ticket_count * senior
    b4_discount = total
    print('Your total is: $', total)
    if 4 < ticket_count < 8:
        total *= discount_10
    if 9 < ticket_count < 15:
        total *= discount_15
    if 15 < ticket_count:
        total *= discount_20
    print('Your grand total after discount is: $', format(total, ',.2f'))
    b4_discount -= total
    print('You saved: $', format(b4_discount, ',.2f'))

# veteran admission processing
if customer == '4':
    total = ticket_count * veteran
    b4_discount = total
    print('Your total is: $', total)
    if 4 < ticket_count < 8:
        total *= discount_10
    if 9 < ticket_count < 15:
        total *= discount_15
    if 15 < ticket_count:
        total *= discount_20
    print('Your grand total after discount is: $', format(total, ',.2f'))
    b4_discount -= total
    print('You saved: $', format(b4_discount, ',.2f'))

# sponsor admission processing
if customer == '5':
    total = ticket_count * sponsor
    b4_discount = total
    print('Your total is: $', total)
    if 4 < ticket_count < 8:
        total *= discount_10
    if 9 < ticket_count < 15:
        total *= discount_15
    if 15 < ticket_count:
        total *= discount_20
    print('Your grand total after discount is: $', format(total, ',.2f'))
    b4_discount -= total
    print('You saved: $', format(b4_discount, ',.2f'))
