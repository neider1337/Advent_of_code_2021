with open("input.txt") as f:
    lanternfish_list = [int(x) for x in f.readline().strip().split(',')]
    pond = {
        0:0,
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
        7:0,
        8:0
        }
days = 256
total = len(lanternfish_list)
print(total)

for fishes in lanternfish_list:
    pond[fishes] +=1
    # that function transmits fishes into dictionary pond and counts it
    print(pond)

for day in range(days):
    fish_holder = pond[0]
    pond[0] = pond[1]
    pond[1] = pond[2]
    pond[2] = pond[3]
    pond[3] = pond[4]
    pond[4] = pond[5]
    pond[5] = pond[6]
    pond[6] = pond[7]
    pond[7] = pond[8]
    pond[6] += fish_holder
    pond[8] = fish_holder

    total += fish_holder

print(total)
