# 구간 합 구하기 4
'''https://www.acmicpc.net/problem/11659'''
import sys

'''
import sys

try:
    N, M = tuple(map(int,sys.stdin.readline().split(' ')))
    numbers = list(map(int,sys.stdin.readline().split(' ')))

    sum_list = [0]
    sum_ = 0
    for num in numbers:
        sum_ += num
        sum_list.append(sum_)

    for m in range(M):
        i, j = tuple(map(int, sys.stdin.readline().split(' ')))
        print(sum_list[j] - sum_list[i-1])

except ValueError or IndexError:
    print("Input Error")
'''
# 수열
'''https://www.acmicpc.net/problem/2559'''
'''
import sys
try:
    N, K = tuple(map(int,sys.stdin.readline().split(' ')))
    numbers = list(map(int, sys.stdin.readline().split(' ')))

    sum_ = 0
    for i in range(K):
        sum_ += numbers[i]

    max_ = sum_
    for j in range(K,N):
        sum_ += numbers[j] - numbers[j-K]
        max_ = (max_ if max_ > sum_ else sum_)

    print(max_)

except ValueError or IndexError:
    print("Input Error")
'''

# 인간-컴퓨터 상호작용
'''https://www.acmicpc.net/problem/16139'''
'''
import sys
try:
    str_ = sys.stdin.readline().rstrip()
    len_ = len(str_)
    sum_list = [[0] * len_ for _ in range(26)]

    def trans_ch_int(char):
        return ord(char) - ord('a')

    for j, c in enumerate(str_):
        number_ac = trans_ch_int(c)

        for i in range(number_ac):
            sum_list[i][j] = sum_list[i][j-1]
        sum_list[number_ac][j] = sum_list[number_ac][j-1] + 1
        for k in range(number_ac+1,26):
            sum_list[k][j] = sum_list[k][j-1]


    q = int(input())
    for q_ in range(q):
        list_ = list(sys.stdin.readline().split(' '))
        ac_num = trans_ch_int(list_[0])
        idx1, idx2 = tuple(map(int, list_[1:]))
        if idx1 == 0:
            print(sum_list[ac_num][idx2])
        else:
            print(sum_list[ac_num][idx2] - sum_list[ac_num][idx1-1])

except ValueError or IndexError:
    print("Input Error")
'''
# 나머지 합
'''https://www.acmicpc.net/problem/10986'''
# N개의 숫자 (1 <= N <= 1000000), sum_interval % M == 0 => count_interval
# 참고
'''https://velog.io/@dev-junku/BOJ-%EB%82%98%EB%A8%B8%EC%A7%80-%ED%95%A9-in-Python'''

# 1 2 3 1 2
# 1 3 6 7 9
# 1 0 0 1 0

# list_r = [3,2,0]  # len = M,

'''

import sys
try:
    N, M = tuple(map(int, sys.stdin.readline().split(' ')))
    numbers = list(map(int,sys.stdin.readline().split(' ')))

    res_list = [0 for _ in range(M)]
    sum_ = 0
    count = 0

    for num in numbers:
        sum_ += num
        r = sum_ % M
        if r == 0:
            count += 1
        res_list[r] += 1

    for res in res_list:
        if res < 2:
            continue
        count += res * (res-1) //2

    print(count)
except ValueError or IndexError:
    print("Input Error")

'''
'''
# 구간의 합 구하기 5
import sys
try:
    N, M = tuple(map(int, sys.stdin.readline().split(' ')))
    sum_list = [[0] * (N+1) for _ in range(N+1)]

    num_list = [list(map(int, sys.stdin.readline().split(' '))) for _ in range(N)]

    for i in range(1,N+1):
        for j in range(1,N+1):
            sum_list[i][j] = sum_list[i-1][j] + sum_list[i][j-1] + num_list[i-1][j-1] - sum_list[i-1][j-1]

    for quest in range(M):
        x1, y1, x2, y2 = tuple(map(int, sys.stdin.readline().split(' ')))
        rlt = sum_list[x2][y2] - sum_list[x1 - 1][y2] - sum_list[x2][y1 - 1] + sum_list[x1-1][y1-1]
        print(rlt)
except ValueError or IndexError:
    print("Input Error")
    '''

# 체스판 다시 칠하기
'''https://www.acmicpc.net/problem/25682'''

import sys
try:
    N, M, K = tuple(map(int, sys.stdin.readline().split(' ')))

    board = [sys.stdin.readline().rstrip() for _ in range(N)]

    prefix_sum = [[0] * (M+1) for __ in range(N+1)]

    odd_color = 'B'
    even_color = 'W'

    for i in range(1,N+1):
        for j in range(1,M+1):
            now_color = board[i-1][j-1]
            if (i+j) % 2 == 0:
                now_ = (0 if now_color != even_color else 1)
            else:
                now_ = (0 if now_color != odd_color else 1)

            prefix_sum[i][j] = now_ + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]


    min_ = K**2
    K_squared = K**2

    for i in range(K,N+1):
        for j in range(K,M+1):
            trans_count = prefix_sum[i][j] - prefix_sum[i-K][j] - prefix_sum[i][j-K] + prefix_sum[i-K][j-K]
            min_ = min(trans_count, K_squared - trans_count, min_)

    print(min_)
except ValueError or IndexError:
    print('Input Error')

