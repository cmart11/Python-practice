import math


name = 'cis'.upper()
age = 90

msg = f'{name} is {age} years old.'

is_hot = False
is_cold = True

while is_hot == False:
    if age >= 85:
        age -= 2
        print(f'age is: {age}')
    else:
        is_hot = True
        print('done.')

# for str in name:
#     print(str)

# array = [1, 2, 3, 4, 5, 6]
# for el in range(len(array)):
#     print(el)


def addPrices():
    sum = 0
    prices = [10, 20, 30]

    for price in prices:
        sum += price
    print(sum)


addPrices()
# tuples are immutable
numbers = (1, 2, 3, 4)

# unpacking
coordinates = (1, 2, 3)
x, y, z = coordinates


def two_num_sum(arr, target):
    result = []
    left = 0
    right = len(arr) - 1
    while left != right:
        possibleSum = arr[left] + arr[right]
        if target == possibleSum:
            result.append([arr[left], arr[right]])
            left += 1
            right -= 1
        elif possibleSum < target:
            left += 1
        elif possibleSum > target:
            right -= 1
    return result


arrA = [1, 3, 4, 7, 8, 33]

print(two_num_sum(arrA, 10))


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')
