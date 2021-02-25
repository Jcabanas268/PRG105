"""
Calculate the area of a shape
"""

# data var
menu = '1. Rectangle \n2. Triangle \n3. Square \n4. Circle \n5. Quit'
PI = 3.14


# process
def main():
    print(menu)
    get_menu = int(input('Enter number for selection:'))
    option = func_validate(get_menu)
    shape = func_shape(option)
    area = func_area(option)
    func_output(shape, area)


def func_validate(num):
    if 0 > num > 5:
        print('Enter valid selection.')
        main()
    else:
        return num


def func_shape(num):
    if num == 1:
        return 'rectangle'
    elif num == 2:
        return 'triangle'
    elif num == 3:
        return 'square'
    elif num == 4:
        return 'circle'


def func_area(num):
    if num == 1:
        return func_rectangle
    elif num == 2:
        return func_triangle
    elif num == 3:
        return func_square
    elif num == 4:
        return func_circle


def func_rectangle():
    length = int(input('Enter length: '))
    width = int(input('Enter width: '))
    area = length * width
    return area


def func_triangle():
    base = int(input('Enter base: '))
    height = int(input('Enter height: '))
    area = (base * height) / 2
    return area


def func_square():
    length = int(input('Enter length: '))
    area = length ** 2
    return area


def func_circle():
    global PI
    radius = int(input('Enter radius: '))
    area = (radius ** 2) * PI
    return area


def func_output(shape, area):
    print('The area of your' + shape + 'is' + str(area))


def func_quit(num):
    while num == 5:
        print('End Program')
        break
    else:
        main()


main()
