# 두 수 비교하기

numbers = input()

numbers = numbers.split(' ')
try:
    a = int(numbers[0])
    b = int(numbers[1])

    if a > b:
        print('>')
    elif a < b:
        print('<')
    else:
        print('==')

except ValueError:

    print('입력오류')


# 시험 성적
try:
    score = int(input())

    if score > 100 or score < 0:
        print('입력 오류')
    elif score > 89:
        print('A')
    elif score > 79:
        print('B')
    elif score > 69:
        print('C')
    elif score > 59:
        print('D')
    else:
        print('F')

except ValueError:
    print('입력 오류')

# 윤년
try:
    year = int(input())

    if 0 < year < 4001:
        if year % 400 == 0:
            print(1)
        elif year % 100 == 0:
            print(0)
        elif year % 4 == 0:
            print(1)
        else:
            print(0)
    else:
        print('입력 오류')
except ValueError:
    print('입력 오류')


# 4분면 고르기

x = input()
y = input()

try:
    x = int(x)
    y = int(y)

    if -1001 < x < 1001 and -1001 < y < 1001 and x*y != 0:
        if x < 0:
            print(f'{(3 if x*y > 0 else 2)}')
        else:
            print(f'{(1 if x*y > 0 else 4)}')
    else:
        print('입력 오류')

except ValueError:
    print('입력 오류')


# 알람 시계

str_ = input()

str_list = str_.split(' ')

if len(str_list) > 2:
    print('입력 오류')

else:
    try:
        H = int(str_list[0])
        M = int(str_list[1])

        if 0 <= H <= 23 and 0 <= M <= 59:
            print(f'{(H if M - 45 >= 0 else (H-1 if H-1 >= 0 else 23))} {(M - 45 if M - 45 >= 0 else M + 15)}')
        else:
            print('입력 오류')
    except ValueError:
        print('입력 오류')

# 오븐 시간

str1 = input()
str2 = input()

try:
    time_ = str1.split(' ')
    H = int(time_[0])
    M = int(time_[1])

    t = int(str2)

    M += t
    H += M // 60

    print(f'{H%24} {M%60}')

except ValueError or IndexError:
    print('입력오류')


# 주사위 세개

# case1 : x = y = z
# case2 : x = y != z  3개 x y z

str_ = input()

try:
    numbers = str_.split(' ')

    x = int(numbers[0])
    y = int(numbers[1])
    z = int(numbers[2])

    # 숫자 정렬 역순
    if x < y:
        x, y = y, x
    if y < z:
        y, z = z, y
    if x < y:
        x, y = y, x

    if x == z:
        print(10000 + 1000 * x)
    elif x == y:
        print(1000 + 100 * x)
    elif y == z:
        print(1000 + 100 * y)
    else:
        print(100 * x)

except ValueError or IndexError:
    print('입력오류')






