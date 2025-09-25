string = list(map(int, input().split()))
max = 0
max_num = 0
for i in string:
    if string.count(i) > max:
        max = string.count(i)
        max_num = i
print(max_num)