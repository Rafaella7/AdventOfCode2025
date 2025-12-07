dial = 50;
num = 0

with open('Day1/data.txt', 'r') as f:
    for line in f:
        direction = line[0]
        value = int(line[1:])
        
        if direction == "R":
            for i in range(value):
                dial += 1
                if dial % 100 == 0:
                     dial = 0
                     num += 1
        else:
            for i in range(value):
                dial -= 1
                if dial % 100 == 0:
                     dial = 0
                     num += 1

print(num)
