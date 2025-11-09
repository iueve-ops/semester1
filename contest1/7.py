def calc(a, op, b):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b

expr = input()
nums = []
ops = []
for i, ch in enumerate(expr):
    if i % 2 == 0:
        nums.append(int(ch))
    else:
        ops.append(ch)




n = len(nums)
min_val = [[0]*n for _ in range(n)]

max_val = [[0]*n for _ in range(n)]

for i in range(n):
    min_val[i][i] = max_val[i][i] = nums[i]

for s in range(1, n):
    for i in range(n - s):
        j = i + s
        min_res = 10000000000000000000
        max_res = -1000000000000000
        for k in range(i, j):
            a = calc(max_val[i][k], ops[k], max_val[k+1][j])
            b = calc(max_val[i][k], ops[k], min_val[k+1][j])
            c = calc(min_val[i][k], ops[k], max_val[k+1][j])
            d = calc(min_val[i][k], ops[k], min_val[k+1][j])
            min_res = min(min_res, a, b, c, d)
            max_res = max(max_res, a, b, c, d)
        min_val[i][j] = min_res
        max_val[i][j] = max_res

print(max_val[0][n-1])
