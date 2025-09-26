with open('input_9.txt', 'r') as file:
    line = file.readline()
    line = line.split(" ")
    count = 0
    for word in line:
        if word[-1] in "?!.":
            count += 1
print((count))
