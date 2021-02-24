

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

