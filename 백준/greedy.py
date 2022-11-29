
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
import sys
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



