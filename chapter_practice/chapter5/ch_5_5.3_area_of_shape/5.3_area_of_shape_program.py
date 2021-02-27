"""
Calculate the area of a shape
"""

# data var
menu = 'Find area for?\n1. Rectangle\n2. Triangle\n3. Square\n4. Circle\n5. Quit\n'     # menu selection
PI = 3.14       # Pi value


# process
def main():                                 # main function
    try:
        print(menu)
        get_menu = int(input('Enter number for selection:'))    # get int range
        option = func_validate(get_menu)        # validates int in range
        if option == 1:
            shape = 'rectangle'
            length = float(input('Enter length: '))
            width = float(input('Enter width: '))
            area = func_rectangle(length, width)    # calculates for area = length * width
            func_output(shape, area)                # output for shape and area
        elif option == 2:
            shape = 'triangle'
            base = float(input('Enter base: '))
            height = float(input('Enter height: '))
            area = func_triangle(base, height)      # calculates for area = base * height
            func_output(shape, area)
        elif option == 3:
            shape = 'square'
            length = float(input('Enter length: '))
            area = func_square(length)              # calculates for area = length *squared
            func_output(shape, area)
        elif option == 4:
            shape = 'circle'
            radius = float(input('Enter radius: '))
            area = func_circle(radius)                 # calculates for area = radius *squared * PI = 3.14
            func_output(shape, area)
        else:
            print('End program')
            quit()
    except ValueError:
        print('Enter valid selection.')
        print()
    main()                                  # return to main()


def func_validate(num):                     # validates int in range
    if num < 1 or num > 5:                  # return prompt to enter valid selection
        print('Enter valid selection.')
        print()
        main()
    else:                                   # return valid int = option
        return num


def func_rectangle(length, width):                       # return rectangle area
    area = length * width
    return area


def func_triangle(base, height):                        # return triangle area
    area = (base * height) / 2
    return area


def func_square(length):                          # return square area
    area = length ** 2
    return area


def func_circle(radius):                          # return circle area
    area = (radius ** 2) * PI
    return area


def func_output(shape, area):               # output shape and area statement
    print('The area of your ' + shape + ' is ' + format(area, ',.2f'))


main()      # call main
