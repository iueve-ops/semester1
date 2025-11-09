n, k = map(int, input().split())

a = list(map(int, input().split()))
maximus = 0

for i in range(len(a)):
    j = i^k
    if j < len(a):
        #k это какашки
        maximus = max(a[i]+a[j], maximus)

print(maximus)