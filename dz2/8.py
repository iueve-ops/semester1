s = list(map(int,input().split(' ')))

n = 0
for i in s:
    n += 1
m = n // 2 + 1

count = 0
for k in s:
    for g in s:
        if g > k:
            count += 1
            if count == m:
                print(g)
                break
