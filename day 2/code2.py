import csv

with open('cotam.csv') as csvfile:
    data = list(csv.reader(csvfile))
    print(data)

x = 0
y = float(0)
d = float(0)
yy = float(0)
aim = float(0)
s = ''

for z in range(len(data)):
    s = ''.join(data[z])
    if "forward" in s:
        x = x + int(s[8])
        yy = yy + (aim * float(s[8]))
    elif "up" in s:
        y = float(s[3])
        aim = aim - y
    elif "down" in s:
        d = float(s[5])
        aim = aim + d


print(yy)
print(x)
print(yy*x)

