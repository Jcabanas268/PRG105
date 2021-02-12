# Determine Financial_Aid eligibility
# data var
eligibility = 0
gpa = 0

# processing
# student status
print('Are you a new student? ')
new_student = str(input('yes or no: '))
if new_student == 'yes':
    eligibility += 1
else:
    gpa = float(input('Please enter current GPA: '))
    if gpa >= 2.0:
        eligibility += 1
    else:
        eligibility = 0

# yes/no for criminal record
print('Do you have a criminal record? ')
criminal = str(input('yes or no: '))
if criminal == 'no':
    eligibility += 1
else:
    eligibility = 0

# yes/no credit availability
print('Are you applying for 6 or more credit hours: ')
credit_hours = str(input('yes or no: '))
if credit_hours == 'yes':
    eligibility += 1
else:
    eligibility = 0

# gross income
income = float(input('Enter gross yearly income: '))
if income <= 50000:
    eligibility += 1
else:
    eligibility = 0

# output
if eligibility >= 4:
    print('You are eligible for Financial Aid')     # finaid AVAILABLE
else:
    print('You are not eligible for Financial Aid')     # finaid Not AVAILABLE
    if new_student == 'no':
        gpa < 2                                     # help. cant resolve gpa !warning!
        print('Your GPA of ' + str(gpa) + ' is too low.')
    if criminal == 'yes':
        print('You have a criminal record.')
    if credit_hours == 'no':
        print('You do not have enough credit hours applied. ')
    if income > 50000:
        print('Your income is too high.')
