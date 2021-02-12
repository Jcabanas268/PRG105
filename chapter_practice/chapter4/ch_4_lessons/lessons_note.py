# number = 10
# while number >= 0:
# print(number)
# number = number - 1

# -------------------------
# rainfall = 0
# total = 0

# for rain in ('jan', 'feb', 'mar', 'apr'):
#     rainfall = float(input('Enter rain for ' + rain))
#     total = total + rainfall
# print(total)

# -------------------------
# end_point = int(input('Highest number to square: '))
# for num in range(1, end_point + 1):
#     value = num * num
#     print(str(num) + " squared " + str(value))

# -------------------------
"""
print('range(10)')
for num in range(6, -11, -2):
    print(num)

print("\n\n2, 4, 6, 8, 10")
for num in (2, 4, 6, 8, 10):
    print(num)

done = 1
print('Enter 0 when you are done')
while done != 0:
    score = float(input('Enter test score: '))

range = (1, 10)
num = int(input('Number'))
while num = 1:
    print(num)

print('Number\tSquare')
print('--------------')
for number in range(1, 11):
    square = number**2
    print(number, '\t', square)
"""

score = int(input('Enter a number from 1 though 10:'))
while score < 1 or score > 10:
    print('Error')
    score = int(input('Enter a valid number from 1 though 10:'))

