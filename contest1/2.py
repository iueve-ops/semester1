a, b = map(int, input().split())
x = 0
while True:
    if (a+x) % b == 0 and (b+x) % a == 0:
        print(x)
        break
    else: x += 1