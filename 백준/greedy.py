
# 동전 0
'''https://www.acmicpc.net/problem/11047'''
'''
import sys
try:
    N, K = tuple(map(int, sys.stdin.readline().split(' ')))
    coins = [int(sys.stdin.readline()) for _ in range(N)]
    j = N-1
    rlt = 0
    while K != 0:
        r = K % coins[j]
        if r != K:
            rlt += K // coins[j]
            K = r
        j -= 1
    print(rlt)
except ValueError or IndexError:
    print('Input Error')
'''
# 회의실 배정
'''https://www.acmicpc.net/problem/1931'''
'''
import sys
try:
    N = int(sys.stdin.readline())

    meeting = [tuple(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]

    # tuple의 두 번째 원소로 정렬 같은 값이 나오면 첫 번째 원소로 정렬
    meeting.sort(key=lambda x : (x[1], x[0]))

    rlt, last = 1, meeting[0][1]

    for tup in meeting[1:]:
        if last <= tup[0]:
            rlt += 1
            last = tup[1]

    print(rlt)
except ValueError or IndexError:
    print('Input Error')
'''

# ATM
'''https://www.acmicpc.net/problem/11399'''
'''
import sys
try:
    N = int(sys.stdin.readline())
    list_ = list(map(int, sys.stdin.readline().split(' ')))
    list_.sort()
    rlt = 0
    for i, time_ in enumerate(list_):
        rlt += (N-i)*time_
    print(rlt)
except ValueError or IndexError:
    print('Input Error')
'''

# 잃어버린 괄호
'''https://www.acmicpc.net/problem/1541'''
'''
import sys
try:
    str_ = sys.stdin.readline().rstrip()
    plus_list = str_.split('-')
    rlt = []
    for list_ in plus_list:
        numbers = list(map(int,list_.split('+')))
        rlt.append(sum(numbers))

    min_ = rlt[0]
    for num in rlt[1:]:
        min_ -= num
    print(min_)
except ValueError or IndexError:
    print("Input Error")
'''

# 주유소
'''https://www.acmicpc.net/problem/13305'''
'''import sys
try:
    N = int(sys.stdin.readline())
    distance = list(map(int, sys.stdin.readline().split(' ')))
    weight = list(map(int, sys.stdin.readline().split(' ')))

    rlt = 0
    min_ = weight[0]
    sum_ = distance[0]

    for i in range(1,N-1):
        if min_ > weight[i]:
            rlt += min_ * sum_
            min_ = weight[i]
            sum_ = distance[i]
        else:
            sum_ += distance[i]
    rlt += min_ * sum_

    print(rlt)

except ValueError or IndexError:
    print('Input Error')
'''

# 보물
'''https://www.acmicpc.net/problem/1026'''
'''
import sys
try:
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split(' ')))
    B = list(map(int, sys.stdin.readline().split(' ')))

    A.sort()
    B.sort(reverse=True)

    sum_ = 0
    for a,b in zip(A,B):
        sum_ += a*b

    print(sum_)

except ValueError or IndexError as e:
    print(e)

'''

# 거스름돈
'''https://www.acmicpc.net/problem/5585'''
'''
cashes = [500,100,50,10,5,1]
try:
    price = 1000 - int(input())
    answer = 0
    for cash in cashes:
        r_, price = price // cash, price % cash
        answer += r_
        if price == 0:
            break
    print(answer)
except ValueError:
    print('Input Error')
'''

# 로프
'''https://www.acmicpc.net/problem/2217'''
'''
import sys
try:
    N = int(sys.stdin.readline())
    ropes = [int(sys.stdin.readline()) for _ in range(N)]

    ropes.sort(reverse=True)
    max_ = 0
    for idx, rope in enumerate(ropes, start=1):
        if max_ < idx * rope:
            max_ = idx * rope

    print(max_)
except ValueError:
    print('Input Error')
'''

# 수들의 합
'''https://www.acmicpc.net/problem/1789'''
'''
import math
try:
    S = int(input())

    n = int((math.sqrt(8*S) - 1)/2)
    n = (1 if n == 0 else n)
    while True:
        sum_ = n*(n+1) // 2
        k = S - sum_
        if k < 0:
            n -= 1
        elif k <= n:
            break
        else:
            n += k // n
    print(n)
except ValueError or IndexError or ZeroDivisionError as e:
    print(e)

'''

# 30
'''https://www.acmicpc.net/problem/10610'''
'''
import sys
try:
    list_ = list(map(int,sys.stdin.readline().rstrip()))
    # print(list_)
    list_.sort(reverse=True)
    number = 0
    for num in list_:
        number *= 10
        number += num

    if not number % 30:
        print(number)
    else:
        print(-1)
except ValueError:
    print('Input Error')

'''

# 전자레인지
'''https://www.acmicpc.net/problem/10162'''
'''
try:
    T = int(input())
    buttons = [300,60,10]
    if T % 10:
        print(-1)
    else:
        for button in buttons:
            q, T = T // button, T % button
            print(q, end= ' ')
except ValueError:
    print('Input Error')

'''

# 신입 사원
'''https://www.acmicpc.net/problem/1946'''
'''
import sys
try:
    T = int(sys.stdin.readline())
    for _ in range(T):
        # Input
        N = int(sys.stdin.readline())
        # applicants =[(id, document_grade, interview_grade) for some id in {0,..,N-1}]
        applicants = [(idx,)+tuple(map(int, sys.stdin.readline().split(' '))) for idx in range(N)]

        # Initializing set
        set_ = set()

        # sort by document
        sort_d = sorted(applicants, key=lambda x : x[1])
        max_i = sort_d[0][2]

        for idx,__,i_g in sort_d[1:]:
            if max_i < i_g:
                set_.add(idx)
            else:
                max_i = i_g

        # sort by interview
        sort_i = sorted(applicants, key=lambda x: x[2])
        max_d = sort_i[0][1]

        for idx, d_g, __ in sort_i[1:]:
            if max_d < d_g:
                set_.add(idx)
            else:
                max_d = d_g

        # Output
        print(N-len(set_))

except ValueError or IndexError as e:
    print(e)
'''

# 카드 정렬하기
'''https://www.acmicpc.net/problem/1715'''

import heapq as hq
import sys

try:
    N = int(sys.stdin.readline())
    cards = [int(sys.stdin.readline()) for _ in range(N)]

    # 카드 묶음이 1개인 경우 바로 종료
    if N <= 1:
        print(0)
        sys.exit()


    hq.heapify(cards)

    sum_ = 0
    while True:
        pop1, pop2 = hq.heappop(cards), hq.heappop(cards)
        sum_pop = pop1 + pop2
        sum_ += sum_pop

        if not cards:
            break
        hq.heappush(cards,sum_pop)

    print(sum_)

except ValueError or IndexError as e:
    print(e)






