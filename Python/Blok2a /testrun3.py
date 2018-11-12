import simpleaudio as sa
import time
import random
samples = [sa.WaveObject.from_wave_file("snare.wav")]

bpm = 120
print("the standard bpm is now: " + str(bpm) )

#set bpm function
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


    for i in range(int(aantalnoten)):
        if i == 0:
            notelengthvalues.append(0)

        container = input()
        container = float(container)
        notelengthvalues.append(container * 4)

    print(notelengthvalues)


    #the first time y is 0 so the pprogram does not crash
    global y
    y = 0

    for timestamp in notelengthvalues:
        x = timestamp * sixteenthNoteDuration
        timestamps.append(x + y)
        y = timestamps[-1]

durationsToTimestamps16th()

NumberLoops = input("Please enter the number of loops")
NumberLoops = int(NumberLoops)


def Playsample():
    # retrieve first timestamp
    # NOTE: pop(0) returns and removes the element at index 0
    timestamp = timestamps.pop(0)
    # retrieve the startime: current time
    startTime = time.time()
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
          timestamps.append(timestamps.pop(0))
          global y
          y = 0
        else:
          # list is empty, stop loop
          keepPlaying = False
      else:
        # wait for a very short moment
        time.sleep(0.001)


for x in range(NumberLoops):
    global y
    y = 0

        notelengthvalues.append(0)
    for timestamp in notelengthvalues:
        x = timestamp * sixteenthNoteDuration
        timestamps.append(x + y)
        y = timestamps[-1]

    Playsample()
