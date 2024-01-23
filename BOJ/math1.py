'''
# 손익 분기점

# A = 고정 비용 // B = 가변 비용 // C = 판매 가격
# A + B * i  < C * i  --- (*),  (*)를 만족 하는 i를 찾기
# condition : A > 0  =>  if B > C then (*) = False for all i in N(Natural Number)
# (*)  =>  A < (C - B) * i  =>  A / (C - B) < i

try:
    str_ = input()
    numbers = list(map(int, str_.split(' ')))

    if numbers[1] >= numbers[2]:
        print(-1)
    else:
        result = numbers[0] / (numbers[2] - numbers[1])
        result = int(result + 1)
        print(result)
except ValueError or IndexError:
    print('Input Error')
'''
'''
# 벌집
# 2 ~ 7  //  8 ~ 19  //  20 ~ 37   //  38 ~ 61  // ...  #
# 0 ~ 5  //  6 ~ 17  //  18 ~ 35   //  36 ~ 59  // ...  # -2
#   0    //  1 ~ 2   //   3 ~  5   //   6 ~ 9   // ...  # // 6 * 1           # i = 1, j = 1
#   0    //    0     //      1     //   2 ~ 3   // ...  # // 6 * (1 + 2)     # i = 2, j = 1 +2
#   0    //    0     //      0     //      1    // ...  # // 6 * (1 + 2 + 3) # i = 3, j = 1 + 2 + 3
try:
    N = int(input())
    if 2 <= N <= 1000000000:
        i = 1
        j = 1
        N -= 2
        while N // (j * 6) > 0:
            i += 1
            j += i
        i += 1
        print(i)
    elif 1 == N:
        print(1)
    else:
        print('Input Error')

except ValueError:
    print('Input Error')

#  지그재그 분수
# 1/1  ||   1/2   2/1 || ... 
try:
    N = int(input())
    if 1 <= N <= 10000000:
        i = 0
        while N > 0:
            i += 1
            N -= i
        r = N + i
        sum_ = i + 1
        if i % 2 == 0:
            print(f'{r}/{sum_ - r}')
        else:
            print(f'{sum_ - r}/{r}')
except ValueError:
    print('Input error')



# 달팽이는 올라가고 싶다

# 높이 v인 나무막대기를  낮에는 A만큼 올라가고 밤에는 B만큼 떨어진다.

# 입력 : 1 <= B < A <= V <= 1000000000

# V < (A-B)X + A를 만족하는 최소 X를 찾아라

import math

try:
    str_ = input()
    numbers = tuple(map(int, str_.split(' ')))
    A, B, V = numbers

    if 1 <= B < A <= V <= 1000000000:
        day = (V - A) / (A - B) + 1

        day = math.ceil(day) # 올림을 해야한다

        print(day)
    else:
        print('Input Error')

except ValueError or IndexError:
    print('Input Error')

# ACM Hotel
# H : 층수, W : 방수  0 이상 99 이하 인 정수로 입력  + 몇번쨰 손님 입력 N

# 조건 : 층수와 상관 없이 엘베랑 가까운 곳 부터 방 배정

# 즉, N // H  + 1 => XX 값,  N % H => YY 값  =>  출력 : YYXX호수
# N % H == 0 일때 는  XX값이 H, YY값 = YY - 1


try:
    T = int(input())
    for i in range(T):
        str_ = input()
        numbers = tuple(map(int, str_.split()))
        H, W, N = numbers
        if 1 <= H <= 99 and 1 <= W <= 99 and 1 <= N <= H * W:
            YY = (N % H if N % H != 0 else H)
            XX = (N // H if H == YY else N // H + 1)

            if XX // 10 == 0:
                print(f'{YY}0{XX}')
            else:
                print(f'{YY}{XX}')
        else:
            print('Input Error')
except ValueError or IndexError:
    print('Input Error')


# 부녀 회장이 될테야
# a층 b호  a-1 층 1 , ... , b호 까지의 사람 들의 수의 합만큼 데려와 살아야 한다
# 0층 i호 에는 i 명이 산다.
# 입력 T \n  k \n  n  k 층 n호
# 1  2  3   4   5   6  ...  n
# 1  3  6  10  15  21  ...  sigma i with i = 1 ,..., n
# 1  4  10 20  35  56
# j층 i호


try:
    T = int(input())
    for test in range(T):
        k = int(input())
        n = int(input())

        if 1 <= k <= 14 and 1 <= n <= 14:
            list_floor = []
            list_0 = list(range(1, n+1))
            list_floor.append(list_0)
            for i in range(k):
                list_k = []
                sum_k = 0
                for j in range(n):
                    sum_k += list_floor[i][j]
                    list_k.append(sum_k)
                list_floor.append(list_k)

            print(list_floor[k][n-1])
        else:
            print('Input Error')
            break
except ValueError or IndexError:
    print('Input error')


# 설탕 배달
# 5키로 3키로

# n = 5i + 3j 를 만족 하는 i + j가 최소가 되는 i와 j를 찾는 문제

# 16 , ..., 30까지 다 나눌수 있음
# 여기에 15씩 더한 값도 다 가능

# 106 => 1001 // 15  11

try:
    N = int(input())
    if 3 <= N <= 5000:
        p = N // 15

        # 16이상은 무조건 값이 존재
        if p == 0:
            r = N
            sum_ = 0
        else:
            r = N % 15 + 15
            sum_ = 3 * (p-1)

        j = -1
        i = 0
        # i 값을 증가 시키며 위 조건에 만족 하는 값을 찾기
        while i * 5 <= r:  #
            if (r - i * 5) % 3 == 0:
                j = (r - i * 5) // 3
                k = i
            i += 1
        print((sum_ + k + j if j >= 0 else j))
    else:
        print('Input Error')
except ValueError:
    print('Input Error')
'''

# 큰 수 덧셈

# 문자열 덧셈

def sum_char(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    str1_r = str1[::-1]
    str2_r = str2[::-1]

    i = 0
    carry = 0
    result = ''

    while True:
        if i >= len1 and i >= len2:
            if carry == 1:
                result += '1'
            break
        elif i >= len2:
            if carry == 0:
                result += str1_r[i:]
                break
            add_ = ord(str1_r[i]) - ord('0') + 1
        elif i >= len1:
            if carry == 0:
                result += str2_r[i:]
                break
            add_ = ord(str2_r[i]) - ord('0') + 1
        else:
            add_ = ord(str1_r[i]) - ord('0') + ord(str2_r[i]) - ord('0') + carry

        carry = add_ // 10
        result += str(add_ % 10)
        i += 1
    return result[::-1]
'''

    while i < len(str1) and i < len(str2):
        add_ = ord(str1_r[i]) - ord('0') + int(str2_r[i]) - ord('0') + carry
        carry = add_ // 10
        result += str(add_ % 10)
        i += 1

    while i < len(str1):
        if carry == 0:
            result += str1_r[i:]
            break
        add_ = ord(str1_r[i]) - ord('0') + carry
        carry = add_ // 10
        result += str(add_ % 10)
        i += 1

    while i < len(str2):
        if carry == 0:
            result += str2_r[i:]
            break
        add_ = ord(str2_r[i]) - ord('0') + carry
        carry = add_ // 10
        result += str(add_ % 10)
        i += 1

    if carry == 1:
        result += '1'

    return result[::-1]

'''
try:
    str_ = input()
    numbers = str_.split(' ')
    rlt = sum_char(numbers[0], numbers[1])
    print(rlt)

except ValueError:
    print('Input Error')



