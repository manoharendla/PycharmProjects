#!/usr/bin/python
import os
import sys
def handle():
    while True:
        try:
            x = int(input("Please enter a number: "))
            break
        except(ValueError,NameError):
            print "OOps entered a wrong number"
            break


def fileOpen():
    try:
        f= open("log.txt","r")
        f.writelines("Writing data")
    except IOError:
        if (f.mode == "r"):
            print "ERROR:File opened in read mode"
            print os.getpid()
    finally:
        print "Closing the file"
        f.close()

def fileOpenWithoutExcept():
    print os.getpid()
    f = open("log1.txt", "r")
    f.writelines("Writing data")

fileOpen()
#fileOpenWithoutExcept()
handle()


