# program song
# data var
x = int()

# progress
for x in range(99, 0, -1):      # list var count range
    print(format(x, ',.0f') + ' bottles of beer on the wall,')      # output var count w/ string
    print(format(x, ',.0f') + ' bottles of beer')                   # output var count w/ string
    print('Take one down, pass it around')                          # output string
    if x == 2:      # if var count equals 2
        break       # break count
    print(format(x - 1) + ' bottles of beer on the wall\n')     # continue to output var count -1 w/ string

for x in range(1, 0, -1):       # start count at 1
    print(format(x, ',.0f') + ' bottle of beer on the wall\n')      # output count relate to x == 2: break
    print(format(x, ',.0f') + ' bottle of beer on the wall,')       # output 1 count with string
    print(format(x, ',.0f') + ' bottle of beer')                    # output 1 count with string
    print('Take one down, pass it around')                          # output string
    print(format(x - 1) + ' bottles of beer on the wall')           # output 0 count with string
    if x == -1:     # if range count equals -1
        break       # break count
