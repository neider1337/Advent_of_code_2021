

lines = []

with open("input.txt") as f:
    line = f.readline()

    while line:
        line = line.strip('\n').split(' ')
        left = [int(x) for x in line[0].split(',')] #x1,y1
        right = [int(x) for x in line[2].split(',')] #x2,y2
        lines.append([left, right])
        line = f.readline()
#x1y1, x2y2

grid = [[0]* 1000 for i in range(1000)]
for line in lines:
    # if x1 = x2
    if line[0][0] == line[1][0]:
        a = min(line[0][1], line[1][1])
        b = max(line[0][1], line[1][1])
        for index in range(a, b+1):
            grid[line[0][0]][index] += 1

    elif line[0][1] == line[1][1]:
        #if y1=y2
        a = min(line[0][0], line[1][0])
        b = max(line[0][0], line[1][0])
        for index in range(a, b+1):
            grid[index][line[0][1]] += 1



        
print(grid)
count = 0
for row in grid:
    for element in row:
        if element >1:
            count += 1

print('answer ', count)
