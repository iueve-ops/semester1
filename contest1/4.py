n, m = map(int, input().split())


res = 0
while n % 2 == 1 and m % 2 == 1:
    res = 1 + 4*res
    n = n//2
    m = m//2

print(res)