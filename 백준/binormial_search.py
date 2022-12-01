# 수 찾기
'''https://www.acmicpc.net/problem/1920'''
'''
import sys
try:
    N = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split(' ')))
    numbers.sort()

    M = int(sys.stdin.readline())
    s_numbers = list(map(int, sys.stdin.readline().split(' ')))

    def binomial_search(l, r, num):
        while l <= r:
            mid = (l + r) // 2
            mid_number = numbers[mid]
            if mid_number == num:
                return 1
            elif mid_number > num:
                r = mid - 1
            else:
                l = mid + 1
        return 0

    for sn in s_numbers:
        print(binomial_search(0,N-1,sn))

except ValueError or IndexError:
    print('Input Error')
'''

# 랜선 자르기
'''https://www.acmicpc.net/problem/1654'''
'''
import sys
try:
    K, N = tuple(map(int,sys.stdin.readline().split(' ')))
    lengths = [int(sys.stdin.readline()) for _ in range(K)]

    max_ = 0
    for length in lengths:
        max_ = (max_ if max_ > length else length)

    low, high, value = 1, max_, N

    rlt = 1

    while low <= high:
        mid = (low + high) // 2
        count = 0

        for len_ in lengths:
            count += len_ // mid

        if count < value:
            high = mid - 1

        elif value <= count:
            rlt = mid
            low = mid + 1

    print(rlt)

except ValueError or IndexError:
    print('Input Error')
'''

# 나무 자르기
'''https://www.acmicpc.net/problem/2805'''
'''
import sys
try:
    N, M = tuple(map(int, sys.stdin.readline().split(' ')))
    lengths = list(map(int, sys.stdin.readline().split(' ')))

    low = 0
    high = 0
    for length in lengths:
        high = max(high,length)

    rlt = 0
    while low <= high:
        sum_ = 0
        mid = (low+high) // 2

        for len_ in lengths:
            sum_ += max(0, len_-mid)
        if sum_ == M:
            rlt = mid
            break

        elif sum_ < M:
            high = mid - 1
        else:
            rlt = mid
            low = mid + 1

    print(rlt)
except ValueError or IndexError:
    print('Input Error')
'''

# 공유기 설치
'''https://www.acmicpc.net/problem/2110'''
'''
import sys
try:
    N, C = tuple(map(int, sys.stdin.readline().split(' ')))
    arr = [int(sys.stdin.readline()) for _ in range(N)]

    arr.sort()
    if C == 2:
        print(arr[-1] - arr[0])
        sys.exit()
    start, end = arr[0], arr[-1]
    low, high = 1, end - start
    rlt = -1

    while low <= high:
        count = 2
        mid = (low+high) // 2

        for i in range(1,N-1):
            distance = min(arr[i] - start, end - arr[i])
            if distance >= mid:
                start = arr[i]
                count += 1

        if count < C:
            high = mid - 1
        else:
            rlt = mid
            low = mid + 1

        start, end = arr[0], arr[-1]

    print(rlt)
except ValueError or IndexError:
    print('Input Error')
'''

# K번째 수
# n, k 입력 // b[k] 출력
# 관찰 1 : m 보다 작은 숫자의 개수 for 1<=i<=N min(m//i, N) sum
# 이때 m의 minimum 값을 구하자

'''https://www.acmicpc.net/problem/1300'''
'''
import sys
try:
    N, K = int(sys.stdin.readline()), int(sys.stdin.readline())

    low = 1
    high = K
    rlt = 0

    while low <= high:
        mid = (low+high) // 2
        count = 0
        for number in range(1,N+1):
            count += min(mid//number, N)

        if count < K:
            low = mid + 1
        else:
            rlt = mid
            high = mid - 1

    print(rlt)
except ValueError:
    print('Input Error')

'''
# 가장 긴 증가하는 부분수열 2
'''https://www.acmicpc.net/problem/12015'''

# [1,3,5,7,9,11]에서 value가 10 이면 [1,3,5,7,9,10]으로 변경가능

# [1,3,5,7,9,11]에서 value가 8 이면 [1,3,5,7,8,11]으로 변경가능

import sys
try:
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split(' ')))

    list_ = [0]

    def binary_search(k):
        low, high = 1, len(list_)-1
        while low <= high:
            mid = (low+high) // 2
            if list_[mid] == k:
                return mid

            if list_[mid] < k:
                low = mid + 1
            else:
                high = mid - 1
        return low

    for number in arr:
        if list_[-1] < number:
            list_.append(number)
        elif list_[-1] > number:
            idx = binary_search(number)
            list_[idx] = number

    print(len(list_)-1)
except ValueError or IndexError:
    print('Input Error')
