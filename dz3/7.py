import string

with open('lorem.txt', 'r') as file:
    text = file.read()

for i in string.punctuation:
    text = text.replace(i, ' ')

text = text.lower()

text = text.split()

dic = {}

for g in text:
    if g in dic:
        dic[g] = dic[g] + 1

    else:
        dic[g] = 1

c = 10

for key, values in dic.items():
    k = max(dic, key = dic.get)
    print(k, dic[k] )
    dic[k] = 0
    c -= 1
    if c == 0:
        break