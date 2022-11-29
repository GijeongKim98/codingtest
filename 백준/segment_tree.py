# 구간의 합 구하기
'''https://www.acmicpc.net/problem/2042'''

# 입력 : 수의 개수(N), 변경의 횟수(M), 구간의 합을 구하는 횟수(K)
# 입력 : 1 ~ N+1줄에 N개의 수
# 입력 : a(if a == 1 then update(b <- c), if a == 2: print of sum(b~c))
# 출력 : a == 1 일때 b부터 c 까지의 합 출력
'''
import sys
try:
    N,M,K = tuple(map(int, sys.stdin.readline().split(' ')))
    numbers = [int(sys.stdin.readline()) for _ in range(N)]
    s_tree = [0] * (len(numbers) * 4)

    def init(start, end, index):
        # 끝에 도달 했을 경우
        if start == end:
            s_tree[index] = numbers[start]
            return s_tree[index]
        # 그 외 경우 한 단계 더 밑으로 진행
        mid = (start + end) // 2
        s_tree[index] = init(start, mid, index*2) + init(mid+1, end, index*2 + 1)
        return s_tree[index]

    def sum_interval(start,end,index,left,right):
        # 범위안에 없을 때
        if start > right or end < left:
            return 0
        # 범위안에 완전 포함 될 때
        if left <= start and end <= right:
            return s_tree[index]
        # 범위에 부분 포함 될 때 부분을 나눠 진행한다.
        mid = (start + end) // 2
        return sum_interval(start,mid,index*2,left,right) + sum_interval(mid+1,end,index*2 + 1, left, right)

    def update(start,end,index,idx,value):
        # 범위 안에 없을때
        if start > idx or end < idx:
            return
        # 범위에 있을때
        s_tree[index] += value
        if start == end: # 끝 노드면 마침
            return
        # 끝 노드가 아닐 경우 밑으로 계속 진행
        mid = (start + end) // 2
        update(start,mid,index*2,idx,value)
        update(mid+1,end,index*2+1,idx,value)

    init(0,N-1,1) # segment tree initializing

    for __ in range(M+K):
        a,b,c = tuple(map(int,sys.stdin.readline().split(' ')))
        if a == 1:
            delta = c - numbers[b-1]
            numbers[b-1] = c
            update(0,N-1,1,b-1,delta)
        if a == 2:
            sum_ = sum_interval(0,N-1,1,b-1,c-1)
            print(sum_)
except ValueError or IndexError:
    print('Input Error')
'''

# 최솟값과 최댓값
'''https://www.acmicpc.net/problem/2357'''

# 입력 : 수의 개수(N), 범위(M)
# 입력 : 1 ~ N+1줄 까지 수
# 입력 : M개의 범위
# 출력 : 최소 // 최대

import sys
try:
    N, M = tuple(map(int, sys.stdin.readline().split(' ')))
    numbers = [int(sys.stdin.readline()) for _ in range(N)]
    s_tree = [[0,0] for ___ in range (len(numbers) * 4)]

    def init(start,end,index):
        if start == end:
            s_tree[index][0], s_tree[index][1] = numbers[start], numbers[start]
            return s_tree[index]
        mid = (start + end) // 2
        left_ = init(start,mid,index*2)
        right_ = init(mid+1,end,index*2 + 1)
        s_tree[index][0] = min(left_[0], right_[0])
        s_tree[index][1] = max(left_[1], right_[1])
        return s_tree[index]


    def get_min_max(start,end,index,left,right):
        if left > end or start > right:
            return [1000000000, 1]

        if left <= start and end <= right:
            return s_tree[index]

        mid = (start + end) // 2
        left_ = get_min_max(start,mid,index*2,left,right)
        right_ = get_min_max(mid+1,end,index*2 + 1, left,right)

        return [min(left_[0],right_[0]), max(left_[1],right_[1])]


    init(0,N-1,1)

    for __ in range(M):
        a,b = tuple(map(int, sys.stdin.readline().split(' ')))
        l = get_min_max(0,N-1,1,a-1,b-1)
        print(f'{l[0]} {l[1]}')
except ValueError or IndexError:
    print('Input Error')

