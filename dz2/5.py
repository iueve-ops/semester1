string = input("Enter a string: ").split(' ')
print([string[-1]] + string[0:-1])