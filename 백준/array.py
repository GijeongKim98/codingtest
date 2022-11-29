'''

# 최소 최대

try:
    N = int(input())
    str_ = input()
    numbers = list(map(int, str_.split(' ')))

    #  print(numbers)

    if len(numbers) == N:

        max_ = numbers[0]
        min_ = numbers[0]

        for number in numbers:
            if max_ < number:
                max_ = number
            if min_ > number:
                min_ = number

    print(min_, max_)
except:
    print('error')
'''
# 최댓값
'''
try:
    max_ = int(input())
    max_index = 1
    for i in range(8):
        num = int(input())
        if num > max_:
            max_ = num
            max_index = i + 2

    print(max_)
    print(max_index)
except ValueError:
    print('error')

# 나머지

list_ = []

try:
    for i in range(10):
        n = int(input())
        r = n % 42
        if r not in list_:
            list_.append(r)
    print(len(list_))
except ValueError:
    print('Input error')



# 평균

try:
    N = int(input())
    str_ = input()
    scores = list(map(int, str_.split(' ')))

    if len(scores) == N:
        max_ = scores[0]
        # 최대 찾기
        for i in range(1,N):
            if max_ < scores[i]:
                max_ = scores[i]

        new_scores = list(map(lambda x : (x/max_) * 100, scores))

        # print(new_scores)

        sum_ = 0

        for score in new_scores:
            sum_ += score

        print(sum_/N)
    else:
        print('Input error')

except ValueError or IndexError:
    print('Input error')
'''
'''
# OX 퀴즈

def sum(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n * (n+1) // 2
    else:
        return n + sum(n-1)

try:
    N = int(input())

    result = []

    for i in range(N):
        str_ = input()
        list_ = str_.split('X')
        score = 0
        for str__ in list_:
            if str__ != '':
                k = len(str__)
                score += sum(k)

        result.append(score)

    for score in result:
        print(score)

except ValueError:

    print('Input error')
'''
'''
# 평균은 넘겠지
try:
    C = int(input())


    for i in range(C):
        str_ = input()
        list_ = list(map(int, str_.split(' ')))

        N = list_[0]
        scores = list_[1:]

        if len(scores)== N:
            # 평균
            sum_s = 0
            for score in scores:
                sum_s += score
            mean = sum_s / N

            # 평균 넘는 사람 몇명?
            count = 0
            for score in scores:
                if score > mean:
                    count += 1

            p = count / N
            p *= 100
            print(f'{p:.3f}%')

        else:
            print('Input error')
            break
except:
    print('error')
'''
# 개수 세기
'''https://www.acmicpc.net/problem/10807'''
'''
import sys
try:
    N = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split(' ')))
    v = int(sys.stdin.readline())

    count = 0
    for num in numbers:
        if v == num:
            count += 1
    print(count)
except ValueError or IndexError:
    print('Input Error')
'''
# 과제 안 내신 분?
'''https://www.acmicpc.net/problem/5597'''

import sys
try:
    list_ = [int(sys.stdin.readline()) for _ in range(28)]

    set_ = set(list_)
    set_all = set(range(1,31))

    __ = list(set_all - set_)
    __.sort()
    for rlt in __:
        print(rlt)
except ValueError or IndexError:
    print('Input Error')

