x = 1_000_000_000_000 

for i in range(1, x):
    if i * i > x:
        print(i - 1)
        break 