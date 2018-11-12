


import simpleaudio as sa
import time


print ("hello how many times would you like to hear the beat?")
numberPlays = input()
numberPlays = int(numberPlays)


print("At what BPM may I present you this groovy beat?")

bpm = input()
bpm = float(bpm)
bpm = (60 / bpm)

print("how many loops?")

aantalLoops = input()
aantalLoops = int(aantalLoops)

print ("Put your amazing notelengthvalues in here:")
print ("0.5,  =   2 notes")
print ("1,   =   1th note")
print ("2    =   2th note")
print ("4,   =   4th note")
print ("8,   =   8th note")
print ("16, =    16th note")
print (".......")



ritmelijst = []

for i in range(numberPlays):
    container = input()
    container = float(container)
    ritmelijst.append(container)

for loop in range(aantalLoops):
    firstbeat = 0
    numberplays = numberPlays * aantalLoops
    for loop in range(numberPlays):
        print(ritmelijst[firstbeat])
        wave_obj = sa.WaveObject.from_wave_file("snare.wav")
        play_obj = wave_obj.play()
        time.sleep(bpm / ritmelijst[firstbeat])
        firstbeat = firstbeat + 1
    aantalLoops = aantalLoops + 1


print ("make a new beat? yes or no")
answer = input()
if answer == "yes":
    print ("Hello how many times would you like to hear the beat?")
    numberPlays = input()
    numberPlays = int(numberPlays)


    print("At what BPM may I present you this groovy beat?")

    aantalLoops = input()
    aantalLoops = int(aantalLoops)

    print ("Put your amazing notelengthvalues in here:")
    print ("0.5,  =   2 notes")
    print ("1,   =   1th note")
    print ("2    =   2th note")
    print ("4,   =   4th note")
    print ("8,   =   8th note")
    print ("16, =  16th note")
    print (".......")



    ritmelijst = []

    for i in range(numberPlays):
        container = input()
        container = float(container)
        ritmelijst.append(container)
    print("how many loops?")

    #ga door een lijst heen met de benodigde aantal iteraties op basis van de numberPlays variabel
    #de tijdsvertraging tussen de iteraties wordt bepaald door de bps* de lengte van de noot


    aantalLoops = input()
    aantalLoops = int(aantalLoops)

    for loop in range(aantalLoops):
        firstbeat = 0
        numberplays = numberPlays * aantalLoops
        for loop in range(numberPlays):
            print(ritmelijst[firstbeat])
            wave_obj = sa.WaveObject.from_wave_file("snare.wav")
            play_obj = wave_obj.play()
            time.sleep(bpm / ritmelijst[firstbeat])
            firstbeat = firstbeat + 1
        aantalLoops = aantalLoops + 1

    print ("I don't know how to make it ask again by jumping to a previous line of code")

else:
    print ("bye")
