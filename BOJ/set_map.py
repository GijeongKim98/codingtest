'''# 숫자 카드

try:
    M = int(input())
    set_ = set(map(int, input().split(' ')))

    N = int(input())
    list_ = list(map(int, input().split(' ')))

    if N == len(list_):
        for number in list_:
            print((1 if number in set_ else 0), end =' ')
    else:
        print("Input Error")
except ValueError:
    print("Input Error")
'''
# 문자열 집합
'''
try:
    N, M = tuple(map(int, input().split(' ')))
    set_ = set()
    list_ = []
    for i in range(N):
        set_.add(input())
    for j in range(M):
        list_.append(input())
    count = 0
    for str_ in list_:
        if str_ in set_:
            count += 1

    print(count)
except ValueError:
    print("Input Error")


# 나는야 포켓몬 마스터 이다솜

try:
    N, M = tuple(map(int, input().split(' ')))
    dict1 = dict()
    dict2 = dict()

    for i in range(N):
        name = input()
        dict1[name] = i + 1
        dict2[i+1] = name

    # print(list_)
    for j in range(M):
        quiz = input()
        try:
            print(dict2[int(quiz)])
        except ValueError:
            print(dict1[quiz])

except ValueError or IndexError:
    print("Input Error")


# 숫자 카드 2
try:
    N = int(input())
    cards = list(map(int, input().split(' ')))
    cards_count = dict()

    for card in cards:
        if card in cards_count:
            cards_count[card] += 1
        else:
            cards_count[card] = 1

    M = int(input())
    list_ = list(map(int, input().split(' ')))

    for num in list_:
        if num in cards_count:
            print(cards_count[num], end=' ')
        else:
            print(0, end=' ')

except ValueError or IndexError:
    print("Input Error")

# 듣보잡

try:
    N, M = tuple(map(int, input().split(' ')))
    set1 = set()
    for i in range(N):
        set1.add(input())
    set2 = set()
    for j in range(M):
        set2.add(input())

    intersection = set1 & set2

    list_ = list(intersection)
    list_.sort()

    print(len(list_))
    for name in list_:
        print(name)
except ValueError:
    print("Input Error")

# 대칭 차집합

try:
    len_a, len_b = tuple(map(int, input().split(' ')))
    a = set(map(int, input().split(' ')))
    b = set(map(int, input().split(' ')))
    if len_a == len(a) and len_b == len(b):
        c = (a | b) - (a & b)
        print(len(c))
    else:
        print("Input Error")
except ValueError:
    print("Input Error")
'''

# 서로 다른 부분 문자열의 개수
try:
    str_ = input()
    len_s = len(str_)
    set_ = set()
    for l in range(1,len_s+1):
        start = 0
        while start + l <= len_s:
            end = start + l
            set_.add(str_[start:end])
            start += 1
    print(len(set_))
except ValueError:
    print("Input Error")
