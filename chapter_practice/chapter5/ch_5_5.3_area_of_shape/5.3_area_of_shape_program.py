"""
Calculate the area of a shape
"""

# data var
menu = 'Find area for?\n1. Rectangle\n2. Triangle\n3. Square\n4. Circle\n5. Quit\n'     # menu selection
PI = 3.14       # Pi value


# process
def main():                                 # main function
    print(menu)
    get_menu = int(input('Enter number for selection:'))    # get int range
    option = func_validate(get_menu)        # validates int in range
    shape = func_shape(option)              # strings shape from int
    area = func_area(option)                # returns area value
    func_output(shape, area)                # output for shape and area
    print()
    main()                                  # return to main()


def func_validate(num):                     # validates int in range
    if num < 1 or num > 5:                  # return prompt to enter valid selection
        print('Enter valid selection.')
        print()
        main()
    if num == 5:                            # menu option for exit program
        print('End Program')
        quit()
    else:                                   # return valid int = option
        return num


def func_shape(num):                        # strings shape from int
    if num == 1:
        return 'rectangle'
    elif num == 2:
        return 'triangle'
    elif num == 3:
        return 'square'
    elif num == 4:
        return 'circle'


def func_area(num):                         # returns area value for int
    if num == 1:
        num = func_rectangle()
        return num
    elif num == 2:
        num = func_triangle()
        return num
    elif num == 3:
        num = func_square()
        return num
    elif num == 4:
        num = func_circle()
        return num


def func_rectangle():                       # return rectangle area
    length = int(input('Enter length: '))
    width = int(input('Enter width: '))
    area = length * width
    return area


def func_triangle():                        # return triangle area
    base = int(input('Enter base: '))
    height = int(input('Enter height: '))
    area = (base * height) / 2
    return area


def func_square():                          # return square area
    length = int(input('Enter length: '))
    area = length ** 2
    return area


def func_circle():                          # return circle area
    radius = int(input('Enter radius: '))
    area = (radius ** 2) * PI
    return area


def func_output(shape, area):               # output shape and area statement
    print('The area of your ' + shape + ' is ' + str(area))


main()      # call main
