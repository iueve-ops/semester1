word_dict = {}
text = ['aaa','aaa','abc']
for word in text:
    print(word_dict)
    if word in word_dict.keys():
        word_dict[word] += 1
    else:
        word_dict[word] = 1
print(word_dict)

nums = set([1,2,3,5])
nums2 = set([3,4,5,7])
print(nums | nums2)
#print(list(nums)[0])
a = ['a','b','c']
b = [1,2,3]
c = list(zip(a,b))
print(c)
print(list(enumerate(a)))
print(list(enumerate(a,start=10)))

#ARR = [i[0] for i in c]
DICT = {i: j for j,i in enumerate(a)}
print(DICT)

state_capital = {'Russia':'Moscow',
                 'France':'Paris', }
print(state_capital)
capital_state = {tuple(state_capital[key]) : key for key in state_capital}
print(capital_state)
