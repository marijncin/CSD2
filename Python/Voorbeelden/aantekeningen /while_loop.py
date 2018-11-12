#python aantekeningen While statement

username = input("your name is = ")
#eerst gaan we een variabel aanmaken met de waarde: False


#terwijl correctselection niet gelijk is aan true loopt de loop
#het fungeert dus als een controlepunt

print("hello" + username + "voer je hakeuze in")

correctSelection = False
while correctSelection != True:
    print("\nHi", username + ", welk geluid wil je horen?")
    print("geluid 1")
    print("geluid 2")
    print("geluid 3")

    #input opvragen
    selectie = input("sound number")
    selectieInt = int(selectie)

    if selectieInt is 1 or selectieInt is 2 or selectieInt is 3:
        print("oke")
        correctSelection = True
    else:
        print("ben je dibieltje? toets 1, 2 of 3 g")

print("lets go dan")
print("Op naar de volgende while loop")

print("we ar gonna count")
print("hello, where would you like to start counting from")
i = input()
i = int(i)
print("hello how far would you like to count.")
count = input()
count = int(count)


while i < count:
    print(i)
    i = i + 1

print("doei")
