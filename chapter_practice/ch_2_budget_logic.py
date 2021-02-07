'''
A program that helps someone create a budget. It should ask the user for monthly income and the following expenses:
'''

# var data
income = float(input('What is your total net monthly income?: $'))
print('Please provide expenses for the following')
housing = float(input('How much do you spend on housing each month?: $'))
food = float(input('How much do you spend on food each month?: $'))
transportation = float(input('How much do you spend on transportation each month?: $'))
phone = float(input('How much do you spend on your phone bill each month?: $'))
utilities = float(input('How much do you spend on your utilities each month?: $'))
clothing = float(input('How much do you spend on clothing each month?: $'))

# processing
def func_budget_percent():
    # get percent
    housing_budget = (100 / income) * housing
    food_budget = (100 / income) * food
    transportation_budget = (100 / income) * transportation
    phone_budget = (100 / income) * phone
    utilities_budget = (100 / income) * utilities
    clothing_budget = (100 / income) * clothing
    # print formatted statement
    print('Housing takes up', format(housing_budget, ',.2f'), '% of your monthly budget.')
    print('Food takes up', format(food_budget, ',.2f'), '% of your monthly budget.')
    print('Transportation takes up', format(transportation_budget, ',.2f'), '% of your monthly budget.')
    print('Phone bill takes up', format(phone_budget, ',.2f'), '% of your monthly budget.')
    print('Utilities takes up', format(utilities_budget, ',.2f'), '% of your monthly budget.')
    print('Clothing takes up', format(clothing_budget, ',.2f'), '% of your monthly budget.')

def func_take_home_pay():
    # difference for take home pay
    take_home_pay = (income - (housing + food + transportation + phone + utilities + clothing))
    # print take home pay
    print('You have $', format(take_home_pay, ',.2f'), 'left from your income after paying these monthly expenses.')

# output budget percent and take home pay
func_budget_percent()
func_take_home_pay()
