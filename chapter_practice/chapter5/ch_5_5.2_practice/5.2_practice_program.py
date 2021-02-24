# 5.2 Practice Program


def main():     # main func
    number = int(input('Enter a whole number between 20 and 100: '))        # get integer between 20 & 100
    valid_num = validate(number)        # validates integer in range
    two = div_by_2(valid_num)       # set value for two w/ div_by_2 function
    three = div_by_3(valid_num)     # set value for two w/ div_by_3 function
    five = div_by_5(valid_num)      # set value for two w/ div_by_5 function
    output(valid_num, two, three, five)     # set values for output
    print()
    main()      # repeat main function


def validate(num):      # validates integer in range = valid_num
    if 20 <= num <= 101:        # returns num when in range
        return num      # return as valid_num
    else:       # when num is not in range
        while num < 20 or num > 100:        # print when num is in not valid range
            print('Invalid number.')
            num = int(input('Enter a whole number between 20 and 100: '))       # get new int
            validate(num)       # validates int as new num
            return num      # return as valid_num


def div_by_2(num):      # divide num by 2
    if num % 2 == 0:        # check float value with 0 remainder
        return 'is divisible by 2'
    else:           # remainder not 0
        return 'is not divisible by 2'


def div_by_3(num):      # divide bum by 3
    if num % 3 == 0:        # check float value with 0 remainder
        return 'is divisible by 3'
    else:           # remainder not 0
        return 'is not divisible by 3'


def div_by_5(num):      # divide bum by 5
    if num % 5 == 0:        # check float value with 0 remainder
        return 'is divisible by 5'
    else:           # remainder not 0
        return 'is not divisible by 5'


def output(num, div2, div3, div5):      # output values
    print(num, div2)        # output valid_num w/ div_by_2 value
    print(num, div3)        # output valid_num w/ div_by_3 value
    print(num, div5)        # output valid_num w/ div_by_5 value


main()      # call main
