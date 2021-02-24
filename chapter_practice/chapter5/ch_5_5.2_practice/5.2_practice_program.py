def main():
    get_int = int(input('Enter a whole number between 20 and 100: '))
    val_num(get_int)
    print(get_int)
    print(val_num(get_int))


def val_num(g_int):
    valid_int = g_int * 12
    print(g_int)
    print(g_int * 2)
    print(valid_int)


main()
'''
*None?

def main():
    get_num()
    val_num()
    div2_num()
    div3_num()
    div5_num()


def get_num():
    number = int(input('Enter a whole number between 20 and 100: '))
    val_num(number)
    div2_num(number)
    div3_num(number)
    div5_num(number)
'''


def get_num():
    number = int(input('Enter a whole number between 20 and 100: '))
    val_num(number)
    div2_num(number)

def val_num(number):
    while 20 < number < 100:
        return number
    while 20 > number > 100:
        print('Enter a valid number')
        get_num()


def div2_num(number):
    div_by_2 = number / 2




'''
        val_num()
        div2_num()
        div3_num()
        div5_num()


def val_num(get_num()):
    while 20 < get_num() < 100:
        valid = get_num()
        return valid
    while 20 > number > 100:
        print('Enter a valid number')
        get_num()


def div2_num(number):
    div_by_2 = number / 2
    print(number)


def div3_num(number):
    div_by_3 = number / 3
    print(number)


def div5_num(number):
    div_by_5 = number / 5
    print(number)

'''
