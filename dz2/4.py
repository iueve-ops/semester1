def swap(string):
    temp = string.split(' ')
    for i in range(0, len(temp)-1, 2):
        temp[i], temp[i+1] = temp[i+1], temp[i]
    return temp
print(swap(input("Enter a string: ")))