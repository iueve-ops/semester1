p = list(map(str, input()))
z1 = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8', 'E', 'J', 'S', 'Z', '3', 'L', '2', '5']
a = 0
l = 0
#for i in range(len(p)):
    for l in p:
        if p[l] in z1:
            a += 1
    if a == len(p):
        print("буквы да")




print(a)

