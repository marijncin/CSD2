
bpm = 120
print("the standard bpm is now: " + str(bpm) )

def setBpm():
    print("do you want to enter new bmp?  y or n")
    answer = input()
    answer = str(answer)
    while answer != "n" and answer != "y":
        print("Please enter y or n ")
        answer = input()
        answer = str(answer)
    if answer == "y":
        global bpm
        bpm = input("set bpm: ")
        bpm = int(bpm)
        print("bpm has been set to: " + str(bpm))
    if answer == "n":
        print("okay then, leave it at: " + str(bpm))
setBpm()

quarterNoteDuration = 60 / bpm
# calculate the duration of a sixteenth note
sixteenthNoteDuration = quarterNoteDuration / 4.0

def durationsToTimestamps16th():

    print("enter how many notes?")
    howmanynotes = input()
    howmanynotes = int(howmanynotes)

    print("please enter your notevalues")
    print("use: 0.25, for 16th")
    print("use: 0.5,  for 8th")
    print("use: 1,    for  4th")
    print("use: 2,     for  2th")
    print("use: 4,     for  1th")

    notelengthvalueslist = []
    for i in range(howmanynotes):
        container = input()
        container = float(container)
        while container != float(0.25) and container != float(0.5) and container != float(1) and container != float(1)  and container != float(2)  and container != float(4):
            print("enter correct float values")
            container = input()
            container = float(container)
        lenlist = len(notelengthvalueslist)
        notelengthvalueslist.append( (lenlist)



# 0 16e  1 16e   2 16e    3 16e    4  16     5   16e
#-  0      0.25    0.5     0.75     1         1.25

    print(notelengthvalueslist)

durationsToTimestamps16th()
