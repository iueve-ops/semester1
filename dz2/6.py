string = list(map(int, input().split()))
for i in string:
    if string.count(i) == 1:
        print(i)
