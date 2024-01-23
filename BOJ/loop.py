'''
# 구구단
try:
    N = int(input())
    for i in range(1,10):
        print(f'{N} * {i} = {N*i}')
except ValueError:
    print('입력 오류')

# 합 - 3

try:
    N = int(input())

    list_ = [0] * N

    for i in range(N):

        str_ = input()

        numbers = str_.split(' ')

        list_[i] = int(numbers[0]) + int(numbers[1])

    for sum_ in list_:
        print(sum_)

except ValueError or IndexError:
    print('입력오류')

# 합

try:
    N = int(input())

    sum_ = 0

    for i in range(1,N+1):
        sum_ += i

    print(sum_)

except ValueError:
    print('입력 오류')


# 영수증
try:
    X = int(input())
    N = int(input())
    if 1 <= X <= 1000000000 and 1 <= N <= 100:

        sum_ = 0

        for i in range(N):

            str_ = input()

            numbers = str_.split(' ')

            sum_ += int(numbers[0]) * int(numbers[1])

        if sum_ == X:
            print('Yes')
        else:
            print('No')
    else:
        print('입력 오류')

except ValueError or IndexError:
    print('입력 오류')


# 빠른 두수 덧셈
import sys

str_ = sys.stdin.readline()

N = str_.rstrip()

list_ = []

count = 0

try:
    N = int(N)
    for i in range(N):
        str_ = sys.stdin.readline().rstrip()
        numbers = str_.split(' ')

        a, b = int(numbers[0]), int(numbers[1])

        if 1 <= a <= 1000 and 1 <= b <= 1000:
            list_.append(a+b)
        else:
            count = 1
            print('입력오류')
            break

    if count != 1:
        for num in list_:
            print(num)
except ValueError or IndexError:
    print('입력 오류')


# 합 - 7

try:
    N = int(input())

    list_ = [0] * N

    for i in range(N):

        str_ = input()

        numbers = str_.split(' ')

        list_[i] = int(numbers[0]) + int(numbers[1])

    for i, sum_ in enumerate(list_):
        print(f'Case #{i+1}: {sum_}')

except ValueError or IndexError:
    print('입력오류')



# 합 - 8

try:
    N = int(input())

    list1 = [0] * N
    list2 = [0] * N

    for i in range(N):

        str_ = input()

        numbers = str_.split(' ')

        a, b = int(numbers[0]), int(numbers[1])

        list1[i] = a
        list2[i] = b

    for i in range(N):
        print(f'Case #{i+1}: {list1[i]} + {list2[i]} = {list1[i]+list2[i]}')

except ValueError or IndexError:
    print('입력오류')

# 별 찍기 - 1

try:
    N = int(input())

    for i in range(1, N+1):
        print('*' * i)
except ValueError:
    print('Input error')

# 별 찍기 - 2

try:
    N = int(input())

    for i in range(1, N+1):
        print(' ' * (N-i), end = '')
        print('*' * i)
except ValueError:
    print('Input error')


# X보다 작은 수

str_ = input()
list_ = str_.split(' ')

a, b = list_[0], list_[1]

try:
    N = int(a)
    X = int(b)

    numbers = input().split(' ')

    if len(numbers) == N:

        result = []

        for number in numbers:

            num = int(number)

            if num < X:
                result.append(num)

        if len(result) > 0:

            for i in result:
                print(i, end=' ')
        else:
            print('Input error')
    else:
        print('Input error')

except ValueError or IndexError:
    print('Input error')


# 합 - 5

count = 0

result = []
try:
    while True:
        str_ = input()
        numbers = str_.split()

        a, b = int(numbers[0]), int(numbers[1])

        if a == 0 and b == 0:
            break
        else:
            result.append(a+b)

    for num in result:
        print(num)

except ValueError or IndexError:
    print('Input error')

# 합 - 4

while True:
    try:
        str_ = input()
        numbers = str_.split()

        a, b = int(numbers[0]), int(numbers[1])
        print(a+b)

    except:
        break
'''

# 더하기 사이클

try:
    N = int(input())
    new_num = (N%10) * 10 + ((N//10) + (N%10)) % 10
    count = 1
    while new_num != N:
        new_num = (new_num % 10) * 10 + ((new_num // 10) + (new_num % 10)) % 10
        count += 1
    print(count)
except:
    print('Input error')

