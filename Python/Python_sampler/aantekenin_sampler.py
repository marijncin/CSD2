
# list met waarden
# forloop
#
import time
#maak een lijst en tel hoeveel elementen er in de lijst zitten
values [0.5, 0.25, 0.5, 2, 1]
numValues = len(values)

#print values to control with a time delay

# de forloop is nu slim genoeg om te weten hoeveel elementen er in de lijst values staat

#print letsgo numvalues number of times
for I in values:
    print(I)


#VOORBEELD
for x in range(3 + 10):
    print(i)


#of:
for x in range(10, 14):
    print(i)

#of:
for x in range(numValues):
    print(i)


#of: nu wordt er ook een index meegegeven aan de lijst met nummers
for index, value in enumerate(values):
    print(index)
    print (values)


#of: dit voorbeeld doet: de beginwaarde tot de beginwaarde + numvalues
startValue = 10
for x in range(startValue, startValue + numValues):
    print(i)


#------------------------------------



#------------------------------------
# forloop in en forloop
print("enter first forloop")
for value in values:
    #start forloop1
    print(value)
    print("klaar met eerste forloop")

    #entering second forloop1
    print("enter second forloop")
    for val2 in values:
        print(val2)
    print("finished second forloop")
