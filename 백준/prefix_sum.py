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



# 전구 상태 뒤집기
'''https://www.acmicpc.net/problem/25634'''

import sys
try:
    N = int(sys.stdin.readline())
    list_a = list(map(int, sys.stdin.readline().split(" ")))
    list_b = list(map(int, sys.stdin.readline().split(" ")))

    index_ = 0
    start_ = list_b[0]

    ########### 전구가 다 켜진 경우 ##########
    if len(list_b) == sum(list_b):
        print(sum(list_a) - min(list_a))
        sys.exit()
    #########################################

    
    ####### [0,1,1,0,0,1] => [0,1,0,1] #######
    rlt = 0 # 켜진 전구의 밝기 : 현재 밝기
    sum_ = 0
    for i , a_i in enumerate(list_a):
        if list_b[i]:
            rlt += a_i

        if start_ == list_b[i]:
            sum_ += a_i
        else:
            list_a[index_], list_b[index_] = sum_, start_
            sum_ = a_i
            start_ = (start_ + 1) % 2
            index_ += 1
     
    list_a[index_], list_b[index_] = sum_, start_
    list_a = list_a[:index_+1]
    list_b = list_b[:index_+1]
    ##########################################
    
    # 중간 결과 확인
    print(list_a)
    print(list_b)

    prefix_0 = []
    prefix_1 = []

    sum_0, sum_1 = 0,0
    max_ = 0
    for idx, a_idx in enumerate(list_a):
        if list_b[idx]:
            sum_1 += a_idx
            prefix_1.append(sum_1)
        else:
            max_ = max(max_,a_idx)
            sum_0 += a_idx
            prefix_0.append(sum_0)
    
    for i in range(1,len(prefix_0)):
        for k in range(len(prefix_0)):
            max_ = max(prefix_0[i])



    print(rlt+max_)
    
except ValueError or IndexError as e:
    print(e)