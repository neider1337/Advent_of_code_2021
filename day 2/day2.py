import csv

x = 0
y = 0
s = ''
up = []
down = []
forward = []

with open('log1.csv') as csvfile:
    data = list(csv.reader(csvfile))

for z in range(len(data)):
    s=''.join(data[z])
    if "forward" in s:
        x = x + int(s[8])
    elif "up" in s:
        y = y - int(s[3])
    elif "down" in s:
        y = y + int(s[5])
print(x)
final = y*x

print(final)


