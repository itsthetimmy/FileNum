import mutagen.id3._tags
import os


artist=0    #sort after artist
title=1     #sort after title
a_z=1       #sort from a to z
z_a=0       #sort from z to a

    
def askSort():
    print("Want to Sort after Artist? (y/n) ")
    answer = input()
    if(answer=="y"):
        artist  = 1
        title   = 0
    else:
        print("It will be sorted by title")
        artist  = 0
        title   = 1
    while 1:
        print("Do you want to sort from A to Z or from Z to A?\nPress (1) for A-Z\nPress (2) for Z-A")
        answer = input()
        if answer == "1":
            a_z = 1
            z_a = 0
            break;
        elif answer == "2":
            a_z = 0
            z_a = 1
            break;

def selectionsort():
    



print("Information: Move this Script to the Location where your Music Files are saved.")
askSort()
