
with open("input.txt") as f:
    data =[x for x in f.read().split()]

print(len(data))

gamma = ""
epsilon = ""


for b in range(0, len(data[0])):
    one = 0
    zero = 0

    for c in range(0,len(data)):
        if data[c][b] == '0':
            zero +=1
        else:
            one+=1
    if zero>one:
        gamma += '0'
        epsilon+= '1'
    else:
        gamma+='1'
        epsilon+='0'


a = int(gamma,2)
b = int(epsilon,2)
c = a * b
print('solution is : ', c)

