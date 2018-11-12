
mijnArray = [1, 2, 3, 4, 5]
print(mijnArray[-1])

# indexnummer [-1] brengt je naar het laatste getal

print(mijnArray[0:2])
#laat je positie 0 tot 2 zien (dus 0 en 1)


print(mijnArray[0:2])


#recursief een array vullen:

print("how many times woule you like to hear the beat?")
beatnumber = input("aantal beats = ")
beatnumber = int(beatnumber)

Beatlijst = []

print("enter your fucking nuts")
while len(Beatlijst) < beatnumber:
    container = input()
    container = int(container)
    Beatlijst.append(container)
    container = container + 1

print(Beatlijst)
print("congratiolations here is your beat")

print("enter new beatnumber")
beatnumber2 = input("aantal beats = ")
beatnumber2 = int(beatnumber)

print("enter your fucking nuts again")
Beatlijst2 = []
for i in range(beatnumber2):
    container = input()
    container = int(container)
    Beatlijst2.append(container)
    container = container + 1

print(Beatlijst2)
