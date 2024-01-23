'''
# 직사각형에서 탈출
try:
    x, y, w, h = tuple(map(int, input().split(' ')))

    if 1 <= x < w <= 1000 and 1 <= y < h <= 1000:
        list_ = [x,y,w-x,h-y]
        min_ = x
        for distance in list_[1:]:
            if min_ > distance:
                min_ = distance
        print(min_)

    else:
        print("Input Error")
except ValueError or IndexError:
    print("Input Error")

# 네 번째 점
try:
    point1 = tuple(map(int, input().split(' ')))
    point2 = tuple(map(int, input().split(' ')))
    point3 = tuple(map(int, input().split(' ')))

    if point1[0] == point2[0]:
        x = point3[0]
    elif point1[0] == point3[0]:
        x = point2[0]
    else:
        x = point1[0]
    if point1[1] == point2[1]:
        y = point3[1]
    elif point1[1] == point3[1]:
        y = point2[1]
    else:
        y = point1[1]
    print(f'{x} {y}')
except ValueError or IndexError:
    print("Input Error")


# 직각 삼각형

try:
    result = []
    while True:
        x, y, z = tuple(map(int, input().split(' ')))

        if x == 0 and y == 0 and z == 0:
            break

        if x > y:
            x, y = y, x
        if y > z:
            z, y = y, z

        if x ** 2 + y ** 2 == z ** 2:
            result.append(True)
        else:
            result.append(False)

    if result:
        for bool_ in result:
            print(('right' if bool_ else 'wrong'))
    else:
        print('Input Error')

except ValueError or IndexError:
    print("Input Error")

# 참외밭
try:
    K = int(input())
    a, b, c, d = 0, 0, 0, 0  # 각각 큰 사각형 가로 세로 작은 사각형 가로 세로
    list_ = []
    for i in range(6):
        tup_ = tuple(map(int, input().split(' ')))
        if tup_[0] < 3 and a < tup_[1]:
            a = tup_[1]
        elif 2 < tup_[0]  and b < tup_[1]:
            b = tup_[1]
        list_.append(tup_)

    for i in range(6):
        if a == list_[i][1] and b == list_[(i+1) % 6][1]:
            c, d = list_[(i+3) % 6][1], list_[(i+4) % 6][1]
        elif b == list_[i][1] and a == list_[(i+1) % 6][1]:
            d, c = list_[(i+3) % 6][1], list_[(i+4) % 6][1]

    print(K * (a*b - c*d))

except ValueError:
    print('Input Error')


# 택시 기하학
import math

try:
    R = int(input())
    t = float((R ** 2) * 2)
    e = (R ** 2) * math.pi
    print(f'{e:.6f}\n{t:.6f}')
except ValueError:
    print('Input Error')


# 터렛

import math
try:
    T = int(input())
    result = []
    for i in range(T):
        x1, y1, r1, x2, y2, r2 = tuple(map(int, input().split(' ')))
        # r2가 큰 걸로 만들기
        if r1 > r2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
            r1, r2 = r2, r1
        # 거리
        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        # print(distance)
        # 거리가 0 => 규현과 승현은 같은 위치
        if distance == 0:
            if r1 == r2:
                result.append(-1)
            else:
                result.append(0)
        # 규현과 승현사이 거리 보다 더 큰 범위에 류재명 존재
        elif distance < r2:
            d2 = r2 - distance
            # print(d2)
            if r1 < d2:
               result.append(0)
            elif r1 == d2:
                result.append(1)
            else:
                result.append(2)
        # 규현과 승현사이 거리 와 같은 범위에 류재명 존재
        elif distance == r2:
            result.append(2)
        else:
            if r1 + r2 > distance:
                result.append(2)
            elif r1 + r2 == distance:
                result.append(1)
            else:
                result.append(0)
    for count in result:
        print(count)
except ValueError:
    print("Input Error")


# 어린왕자
import math
try:
    T = int(input())
    result = []
    for test in range(T):
        start_x, start_y, end_x, end_y = tuple(map(int, input().split(' ')))
        n = int(input())
        count = 0

        for planet in range(n):
            tup_ = tuple(map(int, input().split(' ')))
            distance_s = math.sqrt((tup_[0] - start_x) ** 2 + (tup_[1] - start_y) ** 2)
            distance_e = math.sqrt((tup_[0] - end_x) ** 2 + (tup_[1] - end_y) ** 2)

            if distance_s < tup_[2] and distance_e < tup_[2]:
                continue
            if distance_s < tup_[2]:
                count += 1
            if distance_e < tup_[2]:
                count += 1
        #print(count)
        result.append(count)
    for count_ in result:
        print(count_)

except ValueError or IndexError:
    print("Input Error")

'''

# 하키

import math
try:
    w, h, x, y, p = tuple(map(int, input().split(' ')))
    r = h / 2
    count = 0
    for i in range(p):
        p_x, p_y = tuple(map(int, input().split(' ')))
        if y <= p_y <= y + h:
            if x <= p_x <= x+w:
                count += 1
            elif p_x < x:
                distance_1 = math.sqrt((p_x - x) ** 2 + (p_y - y - r) ** 2)
                if distance_1 <= r:
                    count += 1
            elif x + w < p_x:
                distance_2 = math.sqrt((p_x - x - w) ** 2 + (p_y - y - r) ** 2)
                if  distance_2 <= r:
                    count += 1
    print(count)
except ValueError or IndexError:
    print('Input Error')