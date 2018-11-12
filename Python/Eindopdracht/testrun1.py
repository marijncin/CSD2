import random
timestampskick = []
beat = 14 #beat number counts down
x = 0 # X is ment to be a variable to subtract from the total number of 16th
while 0 < beat:
    rannumber = random.randint(1, 100)

    if rannumber <20: #implement a 80 percent change in an multiplication with 2 (8th note), 20% chance 16th note
        x = 1
    else:
        x = 4


    if rannumber <10:
        x = 4

    if beat < 8:
        if rannumber <20:
            x = 1
        else:
            x = 2

    if beat == 4:
        if rannumber <20:
            x = 1
        else:
            x = 2

    if beat == 2 or beat == 3:
        if rannumber <20:
            x = 1
        else:
            x = 2



    if beat == 1:
        x = 1


    beat = beat - x

    timestampskick.append(x)

print(timestampskick)
