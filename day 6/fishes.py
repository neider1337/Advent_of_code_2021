with open("input.txt") as f:
    lanternfish_list = [int(x) for x in f.readline().strip().split(',')]

days = 0
list = lanternfish_list

while days < 256:
    fish = 0
    for i in list:
        if i != 0:
            lanternfish_list[fish] = list[fish] - 1
        elif i == 0:
            lanternfish_list[fish] = 6
            lanternfish_list.append(9)
        fish += 1
    days += 1
    list = lanternfish_list

print(len(list))
