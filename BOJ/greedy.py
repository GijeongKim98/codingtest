
# 동전 0
''' https://www.acmicpc.net/problem/11047 '''
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
'''
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
'''
# 뒤집기
'''https://www.acmicpc.net/problem/1439'''
'''
import sys
try:
    numbers = list(map(int, list(sys.stdin.readline().rstrip())))
    number_of_part = [0, 0]

    pre_ = numbers[0]
    for number in numbers[1:]:
        if pre_ != number:
            number_of_part[pre_] += 1
            pre_ = number
    number_of_part[pre_] += 1

    print(min(number_of_part))

except ValueError or IndexError as e:
    print(e)

'''


# A -> B
'''https://www.acmicpc.net/problem/16953'''
'''
try:
    a,b = map(int, input().split(' '))
    cnt = 0
    while a < b:
        if b % 10 == 1:
            b = b // 10
        elif not b % 2:
            b = b // 2
        else:
            b = -1
        cnt += 1

    if a == b:
        print(cnt+1)
    else:
        print(-1)

except ValueError or IndexError as e:
    print(e)
'''

# 단어수학
'''https://www.acmicpc.net/problem/1339'''
'''
from collections import Counter
import sys

try:
    N = int(sys.stdin.readline())
    input_list = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

    sort_list = sorted(input_list, key=lambda x : len(x), reverse=True)

    max_digit = len(sort_list[0])

    for idx, list_ in enumerate(sort_list[1:], start=1):
        sort_list[idx] = [0] * (max_digit - len(list_)) + list_

    # get count
    count_list = []
    for i in range(max_digit):
        list_ = []
        for j in range(N):
            list_.append(sort_list[j][i])
        count_list.append(Counter(list_))

    # number mapping
    def map_number(index_):
        len_ = len(count_list[index_])
        if len_ == 1:
            return alphabet

    x = 9
    dict_ = {}

    for idx in range(max_digit):
        # 0을 제거 숫자 셀 때 필요가 없다.
        count_list[idx].pop(0, None)
        items = list(count_list[idx].items())
        print(items)
        len_ = len(count_list[idx])
        if len_ == 1:
            dict_[items[0][0]] = x
            x -= 1
            print(dict_)
            continue


except ValueError or IndexError as e:
    print(e)
'''

# 단어 수학
'''https://www.acmicpc.net/problem/1339'''
# backtracking
'''
import sys
sys.setrecursionlimit(10**8)

try:
    # Input
    N = int(sys.stdin.readline())
    words = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

    # sort by length
    words = sorted(words, key=lambda x : len(x), reverse=True)

    # max_digit
    max_digit = len(words[0])

    # Transformation words
    words_r = []
    for word in words:
        word.reverse()
        words_r.append(word)

    t_words = []
    for digit in range(max_digit-1,-1,-1):
        words_i = []
        for word in words_r:
            try:
                words_i.append(word[digit])
            except IndexError:
                break
        t_words.append(words_i)


    # print(t_words)


    # alphabets
    set_ = set()
    for word in words:
        set_ = set_.union(set(word))
    alphabets = list(set_)

    # mapping number
    dict_map = {alphabet : -1 for alphabet in alphabets}

    # The number of alphabet
    len_alpha = len(alphabets)

    # calculation
    def calculation():
        sum_ = 0
        for word in words:
            number = 0
            # print(f'{word}의 숫자는 ')
            for idx, alpha in enumerate(word):
                number += dict_map[alpha]*(10 ** idx)
                # print(f'idx = {idx}, number = {number}')
            # print(number)
            sum_ += number
        return sum_


    # max_sum
    max_ = 0

    # define dfs()
    def dfs(number, step):
        print(dict_map)
        global max_
        if number == 9 - len_alpha:
            cal_ = calculation()
            max_ = max(max_, cal_)
            print(max_)
            return
        if step >= max_digit:
            return

        if len(t_words[step]) == 1:
            if dict_map[t_words[step][0]] == -1:
                dict_map[t_words[step][0]] = number
                dfs(number-1, step+1)
            else:
                dfs(number,step+1)
        else:
            cnt = 0
            for w in t_words[step]:
                if dict_map[w] != -1:
                    cnt+=1
                else:
                    dict_map[w] = number
                    dfs(number-1,step)
                    dict_map[w] = -1
            if cnt == len(t_words[step]):
                dfs(number, step+1)

    dfs(9, 0)
    # print(dict_map)
    print(max_)
except ValueError or IndexError as e:
    print(e)
'''

# 단어 수학
'''https://www.acmicpc.net/problem/1339'''
'''
import sys
try:
    N = int(sys.stdin.readline())
    words = list(sys.stdin.readline().rstrip() for _ in range(N))

    dict_alpha = {}

    for word in words:
        for digit, alphabet in enumerate(word[::-1]):
            if alphabet in dict_alpha:
                dict_alpha[alphabet] += 10**digit
            else:
                dict_alpha[alphabet] = 10 ** digit

    # data 확인
    # print(dict_alpha)

    # sort dict_alpha
    sorted_alphabet = sorted(dict_alpha.items(), key=lambda x : x[1], reverse=True)

    # data 확인
    # print(sorted_alphabet)

    # Calculation
    number = 9
    answer = 0
    for alpha, coefficient in sorted_alphabet:
        answer += number * coefficient
        number -= 1

    # Output
    print(answer)
except ValueError or IndexError as e:
    print(e)
'''
# 캠핑
'''https://www.acmicpc.net/problem/4796'''
'''
import sys
try:
    c = 1
    while True:
        L, P, V = map(int, sys.stdin.readline().split(' '))
        if not L and not P and not V:
            break

        if V % P < L:
            answer = (V//P) * L + V % P
        else:
            answer = (V//P) * L + L
        print(f'Case {c}: {answer}')
        c += 1
except ValueError:
    print('Input Error')

'''

# 보석도둑
'''https://www.acmicpc.net/problem/1202'''
'''
import sys
import heapq as hq
try:
    # Input
    N, K = map(int, sys.stdin.readline().split(' '))
    jewels = []
    for _ in range(N):
        m, v = map(int, sys.stdin.readline().split(' '))
        hq.heappush(jewels,(-v,m))

    weights = [int(sys.stdin.readline()) for _ in range(K)]

    # Sorting
    weights.sort()
    # jewels.sort(key=lambda x : (x[1],-1 * x[0]), reverse=True)

    # available_bag
    # available_bags = [True] * K

    # Result
    result = 0

    # Get Max Value
    while jewels:
        v, m = hq.heappop(jewels)
        for bag, w in enumerate(weights):
            if m <= w:
                result -= v
                weights.pop(bag)
                break

    print(result)

except ValueError or IndexError as e:
    print(e)
'''

# 팰린드롬 만들기
'''https://www.acmicpc.net/problem/1213'''

import sys
try:
    alpha_list = list(sys.stdin.readline().rstrip())
    # print(alpha_list)
    len_str = len(alpha_list)
    dict_ = {}
    for alpha in alpha_list:
        if alpha not in dict_:
            dict_[alpha] = 1
        else:
            dict_[alpha] += 1

    count_odd = 0
    odd_char = None
    for alpha, cnt in dict_.items():
        if cnt % 2:
            count_odd += 1
            odd_char = alpha
            if count_odd > 1:
                print('I\'m Sorry Hansoo')
                sys.exit()
    
    sort_list = sorted(dict_.items(), key = lambda x : ord(x[0]), reverse=True)

    result = (odd_char if odd_char and count_odd else '')

    for alpha, cnt in sort_list:
        r = cnt // 2
        result = alpha*r + result + alpha*r
    
    print(result)
    
except ValueError and IndexError as e:
    print(e) 



