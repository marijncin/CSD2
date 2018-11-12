import simpleaudio as sa
import time
import random


#enter standard BPM
bpm = 120
print("the standard bpm is now: " + str(bpm) )
# set bpm
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
