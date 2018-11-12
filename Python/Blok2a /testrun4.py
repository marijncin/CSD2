# IMPORTEER BELANGRIJKE BIBLIOTHEKEN
import simpleaudio as sa
import time
import random

# INITIALISEER DE SAMPLE
samples = [sa.WaveObject.from_wave_file("snare.wav"), sa.WaveObject.from_wave_file("kick.wav"), sa.WaveObject.from_wave_file("pop.wav"),]


#SET DE BPM
bpm = 120
print("the standard bpm is now: " + str(bpm) )

#set bpm function (ASK TO CHANGE BPM)
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

#This function converts notevalues  to timestamp
notelengthvalues = []
timestamps = []
timestamps2 = []

#DEFINE THE FUNCTION THAT CALCULATES TIMEDURATIONS FROM THE TIMESTAMPS
def durationsToTimestamps16th():
    quarterNoteDuration = 60 / bpm
    # calculate the duration of a sixteenth note
    global sixteenthNoteDuration
    sixteenthNoteDuration = quarterNoteDuration / 4.0
    sixteenthNoteDuration = float(sixteenthNoteDuration)

    print("how many notes?")
    global aantalnoten
    aantalnoten = input("please enter how many notes?")
    aantalnoten = int(aantalnoten)


    print("please enter note duration..")
    print("0.25 = 16th")
    print("0.5  = 8th")
    print("1    = 4th")
    print("2    = 2h")
    print("4    = 1")

    # maak een lijst aan (notelengthvalues)
    # De container *4 slaat op het volgende:
    # 0.25*4  =1, 0.5* 4 = 2 1*4 = 4 etc..
    #timestamp = 1 element uit deze lijst bijv: 1, 2, 4
    #timstamp * note duration = het aantal 16e
    #1 timestamp is dus 1 16e
    #1 16e is (60/bpm)/4
    for i in range(int(aantalnoten)):
        if i == 0:
            notelengthvalues.append(0)

        container = input()
        container = float(container)
        notelengthvalues.append(container * 4)

    print(notelengthvalues)


    #the first time timeadd is 0 so the pprogram does not crash
    # the timeadd variable is ment to add the next notevalue in millseconds
    # to the totaltime.. this will then become the new totaltime (all the
    #notevalue's combined. This number is to be subtracted from equal time)

    timeAdd = 0
    for timestamp in notelengthvalues:
        totalTime = timestamp * sixteenthNoteDuration
        timestamps.append(totalTime + timeAdd)
        timeAdd = timestamps[-1]



# CALL THE FUNCTION WITH THE GIVEN INPUT
durationsToTimestamps16th()


loops = input("enter number of loops: ")
loops = int(loops)
#FUNCTION THAT PLAYS THE SAMPLE WITH THE POP 0



i = 0
for loop in range(0, loops):

    # retrieve first timestamp
    # pop(0) returns and removes the element at index 0
    timestamp = timestamps[i]


    # retrieve the startime: current time
    startTime = time.time()
    keepPlaying = True
        # play the sequence
    while keepPlaying:
            # retrieve current time
        currentTime = time.time()

              # check if the timestamp's time is passed

        if(currentTime - startTime >= timestamp):
            samples[random.randint(0,2)].play()
            i = i+1


                # if there are timestamps left in the timestamps list
        if i > aantalnoten:
                keepPlaying = False
                i = 1

                  # retrieve the next timestamp

        else:
                  # list is empty, stop loop
            timestamp = timestamps[i]



    else:
                # wait for a very short moment
        time.sleep(0.001)
