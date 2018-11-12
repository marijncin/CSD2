import simpleaudio as sa
import time
import random

timestampKick = [1,2,3,4,5]
timestampSnare = [3,4,5,6,7,8,9,0]
timestampHihat = [3,4,5,6,7,0]
loops = 4


startTime = time.time()
def playAndloopSample():

    print("loops", loops)

    # i = 0   = get the first index of the timestamps list
    a = 0
    b = 0
    c = 0

    for loop in range(0, loops):
        currentTime = time.time()



        keepPlaying = True
        while keepPlaying == True:
            kicktime = timestampKick[a]
            snaretime = timestampSnare[b]
            hihattime = timestampHihat[c]
            print(kicktime)
            print(snaretime)
            print(hihattime)
                # retrieve current time

                  # check if the timestamp's time is passed
                  #check if currenttime is equal to the current item in the timestamps list
            if(currentTime - startTime >= kicktime):
                #play a random sample from the samples list
                samples[0].play()
                print("kick played")

                # make the index run trough the timestamps list each itteration one position
                a = a + 1

            if(currentTime - startTime >= snaretime):
                #play a random sample from the samples list
                samples[1].play()
                print("snare played")
                b = b + 1
                # make the index run trough the timestamps list each itteration one position


            if(currentTime - startTime >= hihattime):
                #play a random sample from the samples list
                samples[2].play()
                print("hh played")

                c = c + 1
                # make the index run trough the timestamps list each itteration one position




            if a == (len(timestampKick)) or b == (len(timestampSnare)) or c == (len(timestampHihat)):
                    # if this point in the code is reached set keepPlaying to false and the sequence is compleet
                print("rondje klaar")    #start new loop if loop int is not full yet
                keepPlaying = False

                a = 1
                b = 1
                c = 1
            else:
                print("aaaa")


        time.sleep(0.001)

playAndloopSample()
