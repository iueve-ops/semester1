
string = input()

stack = []

dic = {
    ')':'(',
    ']':'[',
    '}':'{'
}

c = 0

for i in string:
    if i == '(' or i == '[' or i == '{':
        stack.append(i)
        c=c+1
    else:
        if len(stack) != 0:
            if stack[-1] == dic[i]:
                stack.pop()
                c = c-1


if c == 0:
    print('Yes')
else:
    print('No')


