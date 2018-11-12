# IMPORTEER BELANGRIJKE BIBLIOTHEKEN
import simpleaudio as sa
import time
import random
"""
An example project in which a rhythmical sequence (one measure, 1 sample) is played.
  - Sixteenth note is the smallest used note duration.
  - One meassure, time signature: 3 / 4

Instead of using steps to iterate through a sequence, we are checking the time.
We will trigger events based on a timestamp.

------ HANDS-ON TIPS ------
- Run the code, read the code and answer the following question:
  - This script transforms a list of 'sixteenth notes timestamps' into a list of
    regular timestamps.
    In the playback loop, the time difference (currentTime minus startTime)
    is compared to the upcomming timestamp.
    Why is this a more accurate method then the methods used in the examples
    "04_randomNoteDuration.py" and "05_oneSampleSequenceSteps.py"?
    Notate your answer below this line (Dutch is allowed)!
    --> Omdat dat je een discrete tijdfactor geeft die ritmisch onderverdeeld is in
        tijdseenheden. Vertragingstijd (latency) van de code zelf speelt geen rol meer.

- Alter the code:
  Currently one sample is played. Add another sample to the script.
  When a sample needs to be played, choose one of the two samples
  randomly.
  (See the hint about the random package in script "02_timedPlayback".)

- Alter the code:
  Currently the sequence is only played once.
  Alter the code to play it multiple times.
  hint: The timestamps list is emptied using the pop() function.
  (multiple possible solutions)

"""

#setting the global variables
# INIT DE SAMPLE, load sample from computer
samples = [sa.WaveObject.from_wave_file("snare.wav"), sa.WaveObject.from_wave_file("kick.wav"), sa.WaveObject.from_wave_file("pop.wav"),]
notelengthvalues = []
timestamps = []

#-------------------------------------------------------
#PART 1: BPM CALCULATONS -------------------------------
#SET the standard BPM
bpm = 120
print("the standard bpm is now: " + str(bpm) )

#set bpm function (ASK TO CHANGE BPM)
# if yes: set new bpm, if no leave at standard bpm = 120
# Als gebruiker in de BPM een random ding invoert komt er nu een foutmelding
# googlen op TRy catch!


def setBpm():
    print("do you want to enter new bmp?  y or n")
    answer = input()
    answer = str(answer)
    #while the answer is not n or y repeat question
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
#-------------------------------------------------------

#-------------------------------------------------------
#PART 2: Calculating the time in seconds from 16th notes with the BPM
#DEFINE THE FUNCTION THAT CALCULATES TIMEDURATIONS FROM THE TIMESTAMPS
def durationsToTimestamps16th():
    quarterNoteDuration = 60 / bpm
    #Calculate the duration of a sixteenth note
    #Setting it global because we need it in later functions
    # the sixteenthnoteduration is the duration of a quarternote devided by for
    # we need the 16thnote because we are building a grid with 1616thnotes

    global sixteenthNoteDuration
    sixteenthNoteDuration = quarterNoteDuration / 4.0
    sixteenthNoteDuration = float(sixteenthNoteDuration)


    #ask the user how many notes to play..
    print("how many notes?")
    global aantalnoten
    aantalnoten = input("please enter how many notes?")
    aantalnoten = int(aantalnoten)

    #1 timestamp = 1 16thnote durarion --> the actual time depends on BPM
    #0.25*4 = 1 = 1 * 16thnote = 1 16thnote playtime in seconds
    #the actual playtime of the quarternote depends on the BMP.
    print("please enter note duration..")
    print("0.25 = 16th")
    print("0.5  = 8th")
    print("1    = 4th")
    print("2    = 2h")
    print("4    = 1")
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
#-------------------------------------------------------


# please enter the number of loops and store int
loops = input("enter number of loops: ")
loops = int(loops)
#FUNCTION THAT PLAYS THE SAMPLE WITH THE INDEX
def playAndloopSample():
    # i = 0   = get the first index of the timestamps list
    i = 0
    for loop in range(0, loops):

        #look at the first value in timestamps lst (0)
        timestamp = timestamps[i]
        # start the clock
        startTime = time.time()
        keepPlaying = True
            # while keepplaying is true: run the whileloop that plays the timestamps list
            # play the sequence
        while keepPlaying:
                # retrieve current time
            currentTime = time.time()
                  # check if the timestamp's time is passed
                  #check if currenttime is equal to the current item in the timestamps list
            if(currentTime - startTime >= timestamp):
                #play a random sample from the samples list
                samples[random.randint(0,1)].play()
                print(timestamp)
                # make the index run trough the timestamps list each itteration one position
                i = i+1

            if i > aantalnoten:
                    # if this point in the code is reached set keepPlaying to false and the sequence is compleet
                    #start new loop if loop int is not full yet
                    keepPlaying = False
                     #the i = 1 is used so the 0 in the durations lst get used only the first loop
                    i = 1
            # retrieve the next timestamp
            else:
            # if not.. take next item from the durations list
                timestamp = timestamps[i]
        else:
                    # wait for a very short moment
            time.sleep(0.001)
playAndloopSample()
