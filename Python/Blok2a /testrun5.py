# IMPORTEER BELANGRIJKE BIBLIOTHEKEN
import simpleaudio as sa
import time
import random

# INITIALISEER DE SAMPLE
samples = [sa.WaveObject.from_wave_file("snare.wav")]

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
    aantalnoten = input("please enter how many notes?")
    print("please enter note duration..")
    print("0.25 = 16th")
    print("0.5  = 8th")
    print("1    = 4th")
    print("2    = 2h")
    print("4    = 1")

    # maak een lijst aan (notelengthvalues)
    # De container *4 slaat op het volgende:
    # 0.25*4  =1, 0.5* 4 = 2 1*4 = 4 etc..

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
    #notevalue's combined. This number is to be subtracted from the currenttime.)

# CALL THE FUNCTION WITH THE GIVEN INPUT
durationsToTimestamps16th()
timeAdd = 0

loops = input("please enter loops")
loops = int(loops)
#FUNCTION THAT PLAYS THE SAMPLE WITH THE POP 0

for loop in range(loops):
    startTime = time.time()
    def Playsample():
    # retrieve first timestamp
    # NOte: pop(0) returns and removes the element at index 0

        timestamp = timestamps.pop(0)



        # retrieve the startime: current time

        keepPlaying = True
        # play the sequence
        while keepPlaying:
          # retrieve current time
          currentTime = time.time()
          # check if the timestamp's time is passed
          if(currentTime - startTime >= timestamp):
            # play sample

            samples[0].play()

            # if there are timestamps left in the timestamps list
            if timestamps:
              # retrieve the next timestamp
              timestamp = timestamps.pop(0)



            else:
              # list is empty, stop loop
              keepPlaying = False
          else:
            # wait for a very short moment
            time.sleep(0.001)

    for timestamp in notelengthvalues:

        totalTime = timestamp * sixteenthNoteDuration
        timestamps.append(totalTime + timeAdd)
        timestamps2.append(totalTime + timeAdd)
        timeAdd = timestamps[-1]
    print(timestamps)
    Playsample()
