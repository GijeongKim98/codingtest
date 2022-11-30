'''N = 5

list_ = [5, 17, 23, 14, 83]

r = 0

min_ = 5 # N

result = []

# 공약수 구하기
# 공약수 = 최대 공약수의 약수


    for num in list_:  # N
        if num % k != r:
            break
        count += 1
    if count == N:
        result.append(k)
    r += 1

print(result)

''''''
sudoku = [0, 3, 5, 4, 6, 9, 2, 7, 8,
            7, 8, 2, 1, 0, 5, 6, 0, 9,
            0, 6, 0, 2, 7, 8, 1, 3, 5,
            3, 2, 1, 0, 4, 6, 8, 9, 7,
            8, 0, 4, 9, 1, 3, 5, 0, 6,
            5, 9, 6, 8, 2, 0, 4, 1, 3,
            9, 1, 7, 6, 5, 2, 0, 8, 0,
            6, 0, 3, 7, 0, 1, 9, 5, 2,
            2, 5, 8, 3, 9, 4, 7, 6, 0]

result = []
for i, num in enumerate(sudoku):
    if num == 0:
        print(f'index = {i}')
        result.append(i)
print(result)
'''

'''
def scalar_product(a, b, __=2):
    rlt = []
    for i in range(2):
        list_ = []
        for j in range(__):
            sum_ = 0
            for k in range(2):
                sum_ += a[i][k] * b[k][j]
                sum_ = sum_ % 100000
            list_.append(sum_)
        rlt.append(list_)
    return rlt


print(scalar_product([[1,1],[1,0]],[[1],[0]],1))
'''
'''
import sys
N, M, K = tuple(map(int, sys.stdin.readline().split(' ')))
numbers = [int(sys.stdin.readline()) for _ in range(N)]
s_tree = [0] * (len(numbers) * 4)


def init(start, end, index):
    # 끝에 도달 했을 경우
    if start == end:
        s_tree[index] = numbers[start]
        return s_tree[index]
    # 그 외 경우 한 단계 더 밑으로 진행
    mid = (start + end) // 2
    s_tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
    return s_tree[index]


def sum_interval(start, end, index, left, right):
    # 범위안에 없을 때
    if start > right or end < left:
        return 0
    # 범위안에 완전 포함 될 때
    if left <= start and end <= right:
        return s_tree[index]
    # 범위에 부분 포함 될 때 부분을 나눠 진행한다.
    mid = (start + end) // 2
    return sum_interval(start, mid, index * 2, left, right) + sum_interval(mid + 1, end, index * 2 + 1, left, right)


def update(start, end, index, idx, value):
    # 범위 안에 없을때
    if start > idx or end < idx:
        return
    # 범위에 있을때
    s_tree[index] += value
    if start == end:  # 끝 노드면 마침
        return
    # 끝 노드가 아닐 경우 밑으로 계속 진행
    mid = (start + end) // 2
    update(start, mid, index * 2, idx, value)
    update(mid + 1, end, index * 2 + 1, idx, value)


print(f'초기화 전 : {s_tree}')
init(0, 4, 1)
print(f'초기화 후 : {s_tree}')
print(f'2~5까지의 구간 합 : {sum_interval(0, 4, 1, 1, 4)}')
print(f'3번째 값 6으로 변경')
update(0, 4, 1, 2, 6 - numbers[2])
print(f'2~5까지의 구간 합(변경후) : {sum_interval(0, 4, 1, 1, 4)}')
'''

a = 6
b = 3
print(f'a = {a}, b = {b}')
print(f'a/b = {a/b}\na//b = {a//b}')
