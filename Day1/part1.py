dial = 50;
num = 0

with open('Day1/data.txt', 'r') as f:
    for line in f:
        direction = line[0]
        value = int(line[1:])
        
        if direction == "R":
            dial += value
        else:
            dial -= value

        if dial > 99:
            dial = dial % 100
        elif dial < 0:
            dial = dial % 100
        
        if dial == 0:
            num += 1


print(num)


