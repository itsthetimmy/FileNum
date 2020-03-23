import eyed3
import os


artist=0    #sort after artist
title=1     #sort after title
RevOrder=False       #sort from a to z



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
        if answer == "1":   #sort Alphabetical Order
            RevOrder = False
            break;
        elif answer == "2": #sort reverse Alphabetical Order
            RevOrder = True
            break;

path = "/home/itsthetimmy/Musik"
count=0
print("Information befor running: Move this Script to the Location where your Music Files are saved.")
#askSort()
os.chdir(path)
filelist = os.listdir()
print(str(filelist) + "\nUNSortiert")
filelist.sort(reverse=RevOrder)

for x in filelist:
    count=count+1
    os.rename(x, str(count) + " - " + str(x))
count=0
filelist = os.listdir()
print(str(filelist) + "\nSortiert")
