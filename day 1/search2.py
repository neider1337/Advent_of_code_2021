
with open("input.txt") as f:
    data =[x for x in f.read().split()]
z = 0
for i in range(0,len(data)-4):
    sum1 = 0
    sum2 = 0
    sum1 = int(data[i]) + int(data[i+1]) + int(data[i+2])
    sum2 = int(data[i+1]) + int(data[i+2]) + int(data[i+3])

    if sum1<sum2:
        z += 1

print('The right answer is: ', z)



