#STEP 1.. setting global variables, importing modules
import simpleaudio as sa
import time
import random
from midiutil.MidiFile import MIDIFile
from midiutil import MIDIFile


#loading samples in a list
samples = [sa.WaveObject.from_wave_file("kick.wav"), sa.WaveObject.from_wave_file("snare.wav"), sa.WaveObject.from_wave_file("HH.wav"),]
notelengthvalues = []
timestamps = []

#making BPM function
bpm = 120
print("the standard bpm is now: " + str(bpm) )
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


#STEP 2: here needs to be a code asking the user for a rythem

def Metricto16thconversion():
    global beat
    global metric
#asking the user for rythmic input
    print("Instructions: First enter the number of beats, then hit enter")
    print("after hitting enter, type in the Metric")
    print("example: '7', enter, '8' will give you 7/8th")
    print("good luck!")

    #USER INPUT METRIC
    beat = input("please enter beat: ")
    metric = input("Please enter metric: ")
    beat = int(beat)
    metric = int(metric)

    #the metric should always count up to the number of 16thnotes in the metric
    #for example: 7/8th should have 14 16th notes.
    if metric == 8:
        beat = beat * 2
    if metric == 4:
        beat = beat * 4
    if metric == 16:
        beat = beat * 1
    if metric == 2:
        beat = beat * 8

#calculating / scaling rythmic input to 16th
    print("beat = " + str(beat))
    print("metric =" + str(metric))
    print("beat now represents the total number of plays, beat = " + str(beat))

#making the timestamps list
    return beat #beat variable gets returned with the correct number of 16th's
Metricto16thconversion()
# Calculating a timestamp from the bpm

#this function calculates a 16th note timestamp depending on BPM
def bpmto16thnotes():
    quarterNoteDuration = 60 / bpm
    #Calculate the duration of a sixteenth note
    #Setting it global because we need it in later functions
    # the sixteenthnoteduration is the duration of a quarternote devided by for
    # we need the 16thnote because we are building a grid with 1616thnotes

    global sixteenthNoteDuration
    sixteenthNoteDuration = quarterNoteDuration / 4.0
    sixteenthNoteDuration = float(sixteenthNoteDuration)

bpmto16thnotes()
#STEP 3 -- GENERATING RYTHEM PATERNS FOR KICK, SNARE , HH

#The beat (number of 16th in selected rythem)
#gets copied 3 times, kick, snare, hh. This is to prevent out of range errors.
kick = beat
snare = beat
hihat = beat

#in the same manner, 3 lists are made, one for each drum patern.
kicknotes = []
snarenotes = []
hihatnotes = []

#the next 3 functions generate (semi) random rythem paterns for each instrument (kick,snare,hh)
#the main idea is that notedurations can vary but the total sum of 16th should be equal to beat.
def genkicklist():
    global kick
    #beat is now set to the number of 16th's in the total rythmic
    #from this point it will count down to 0

    x = 0 # X is ment to be a variable to subtract from the total number of 16th
    #the musical structure of the drumsloop can be changed by changing the percentages of chance for X

    #while kick (copy from beat) is bigger then 0, keep looping
    while 0 < kick:
        rannumber = random.randint(1, 100)

        if rannumber <20: #implement a 80 percent change in an multiplication with 2 (8th note), 20% chance 16th note
            x = 1
        else:
            x = 4



        if rannumber <10:
            x = 2

        if kick < 8:
            if rannumber <20:
                x = 1
            else:
                x = 2

        if kick == 4:
            if rannumber <20:
                x = 1
            else:
                x = 2

        #SAFETY NET: when kick becomes smaller then 4 only subtract 1 or 2 from the list
        if kick == 2 or kick == 3:
            if rannumber <20:
                x = 1
            else:
                x = 2

                    #when kick is 1 just subtract one.
        if kick == 1:
            x = 1

        #this is the subtraction of X from the beat list in kick, snare or HH
        kick = kick- x

        #value X (so 1,2, or 4) gets appended to the kicklist (or snare or HH)
        kicknotes.append(x)

    #PROBLEM:
    #the probebility of a notevalue X being smaller at the end is bigger.. this is solved
    #by shuffling the list around.
    random.shuffle(kicknotes)

    print(kicknotes)
genkicklist()

#same thing for snare
def gensnarelist():
    global snare
    #beat is now set to the number of 16th's in the total rythmic
    #from this point it will count down to 0
    x = 0 # X is ment to be a variable to subtract from the total number of 16th
    while 0 < snare:
        rannumber = random.randint(1, 100)

        if rannumber <20: #implement a 80 percent change in an multiplication with 2 (8th note), 20% chance 16th note
            x = 1
        else:
            x = 4



        if rannumber <10:
            x = 4

        if snare < 8:
            if rannumber <20:
                x = 1
            else:
                x = 2

        if snare == 4:
            if rannumber <20:
                x = 1
            else:
                x = 2

        if snare == 2 or snare == 3:
            if rannumber <20:
                x = 1
            else:
                x = 2



        if snare == 1:
            x = 1


        snare = snare - x

        snarenotes.append(x)

    random.shuffle(snarenotes)

    print(snarenotes)
gensnarelist()

#same thing for HH
#but with different values
def genhihatlist():
    global hihat
    #beat is now set to the number of 16th's in the total rythmic
    #from this point it will count down to 0
    x = 0 # X is ment to be a variable to subtract from the total number of 16th
    while 0 < hihat:
        rannumber = random.randint(1, 100)

        if rannumber <20: #implement a 80 percent change in an multiplication with 2 (8th note), 20% chance 16th note
            x = 1
        else:
            x = 4



        if rannumber <10:
            x = 4

        if hihat < 8:
            if rannumber <20:
                x = 1
            else:
                x = 2

        if hihat == 4:
            if rannumber <20:
                x = 1
            else:
                x = 2

        if hihat == 2 or hihat == 3:
            if rannumber <20:
                x = 1
            else:
                x = 2



        if hihat == 1:
            x = 1


        hihat = hihat - x

        hihatnotes.append(x)

    random.shuffle(hihatnotes)

    print(hihatnotes)
genhihatlist()

#STEP 4 -   CONVERTING THE RYTHEM PATERNS TO TIMESTAPMS (ABSOLUTE TIME VALUES)
# DESCRETE TIME CONVERSION TO CONTINUOUS TIME

timestampKick = []
timestampSnare = []
timestampHihat = []

#multiply kicknotes list with 16th duradion and insert 0
def convertkicktoTimestamps():

# I is the indexnumber in the kicknotes list
# convertion takes place where i is multiplied by 16thduration calculated from bpm
# timeadd takes on the value of the previous time value in the list
# timeadd gets added up by totaltime (totaltime = current index number multiplied by bpm time)
    timeAdd = 0
    for i in kicknotes:
        totaltime = i * sixteenthNoteDuration
        timestampKick.append(totaltime + timeAdd)
        timeAdd = timestampKick[-1]
# outputs a list of continuous timevlue's to be played
    #timestampKick.insert(0,0)
    print(timestampKick)
convertkicktoTimestamps()


# same thing for snare
def convertSnaretoTimestamps():

    timeAdd = 0
    for i in snarenotes:
        totaltime = i * sixteenthNoteDuration
        timestampSnare.append(totaltime + timeAdd)
        timeAdd = timestampSnare[-1]

    #timestampSnare.insert(0,0)
    print(timestampSnare)
convertSnaretoTimestamps()

# same thing for HH
def convertHihattoTimestamps():

    timeAdd = 0
    for i in hihatnotes:
        totaltime = i * sixteenthNoteDuration
        timestampHihat.append(totaltime + timeAdd)
        timeAdd = timestampHihat[-1]


    print(timestampHihat)
convertHihattoTimestamps()

print("code runs untill here")

# start the clock
print(timestampKick)
print(timestampSnare)
print(timestampHihat)


#how many times must the sequence be played in a row?
loops = input("enter number of loops: ")
loops = int(loops)



#STEP 5 - PLAYING THE LISTS
def playAndloopSample():

    print("loops", loops)


    a = 0 #a is for the kick this is an INDEX counter
    b = 0 #b is for snare this is an INDEX counter
    c = 0 #c is for HH this is an INDEX counter

    for loop in range(0, loops):
        startTime = time.time()

        #making variables containing the first play for each instrument.
        kicktime = timestampKick[a]
        snaretime = timestampSnare[b]
        hihattime = timestampHihat[c]


        keepPlaying = True
        while keepPlaying == True:
            currentTime = time.time()
            print(kicktime)
            print(snaretime)
            print(hihattime)
                # retrieve current time

                  # check if the timestamp's time is passed
                  #check if currenttime is equal to the current item in the timestamps list
            if(currentTime - startTime >= kicktime):
                #play a random sample from the samples list


                # make the index run trough the timestamps list each itteration one position
                # a counts up.. when it gets bigger then the number of items in the timestampskick list stop playing.
                if a < len(timestampKick) -1:
                    samples[0].play()
                    print("kick played")
                    a = a + 1
                    #kicktime gets redefined as the next item for the next itteration in the while loop
                    kicktime = timestampKick[a]
                else:
                    print("a",a)



                #same thing for snare
            if(currentTime - startTime >= snaretime):
                #play a random sample from the samples list

                if b < len(timestampSnare) -1:
                    samples[1].play()
                    print("snare played")
                    b = b + 1
                    snaretime = timestampSnare[b]
                else:
                    print("b",b)


                # make the index run trough the timestamps list each itteration one position

                #same thing for HH
            if(currentTime - startTime >= hihattime):
                #play a random sample from the samples list

                if c < len(timestampHihat) -1:
                    samples[2].play()
                    print("hh played")
                    c = c + 1
                    hihattime = timestampHihat[c]
                else:
                    print("c",c)


                # make the index run trough the timestamps list each itteration one position



                #FINAL CHECK: when all lists are fininshed playing reset the index value's to 0 and go back in the
                # aantalloops loop
            if a == (len(timestampKick)-1) and b == (len(timestampSnare)-1) and c == (len(timestampHihat)-1):
                    # if this point in the code is reached set keepPlaying to false and the sequence is compleet
                print("rondje klaar")    #start new loop if loop int is not full yet
                keepPlaying = False

                a = 0
                b = 0
                c = 0
            else:
                #small delay for cpu workload smoothening
                time.sleep(0.001)



playAndloopSample()

#STEP 6 - MIDI
#make 3 midi lists
timestampKickMidi = []
timestampSnareMidi = []
timestampHihatkMidi = []

# I have no clue why i had to multiply this with 2, I copied it froms cisca.
#P is index number in the timetamps kicklist
# ALSO: how can these midi notes be correct when timestampskick has bpm dependend values???????????
# the rythem output is correct

for p in timestampKick:
    p = p * 2
    timestampSnareMidi.append(p)
for p in timestampKick:
    p = p * 2
    timestampSnareMidi.append(p)
for p in timestampKick:
    p = p * 2
    timestampSnareMidi.append(p)
print(timestampKick)
print(timestampKickMidi)

Drumsmidifile = MIDIFile(1)
   # One track, defaults to format 1 (tempo track is created
                      # automatically)

#add all the notevalues from the midi lists to the midi file.
for i in timestampKickMidi:
    Drumsmidifile.addNote(0, 0, 35, i, 0.1, 100)
for i in timestampKickMidi:
    Drumsmidifile.addNote(0, 0, 36, i, 0.1, 100)
for i in timestampKickMidi:
    Drumsmidifile.addNote(0, 0, 37, i, 0.1, 100)
print(timestampKickMidi)


#exports midi file (WHY IS IT CALLED OPEN???)
with open("Drums.mid", "wb") as output_file:
    Drumsmidifile.writeFile(output_file)
