import sys

dict = {}

s = input()

s = list(s.upper())

for c in s:
    if c not in dict:
        dict[c] = 1
    else:
        dict[c] += 1

res = sorted(dict.items(), key = lambda x : (-x[1]))

if len(res) < 2:
    print(res)
else:
    if res[0][1] == res[1][1]:
        print('?')
    else:
        print(res[0][0])