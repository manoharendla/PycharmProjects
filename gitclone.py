__author__ = '619635'
import os
import subprocess

def checkDir(dir):
    if os.path.isdir(dir):
        print("dir exists")
    else:
        print("doesn't exist")

def execute(command):
    subprocess.call(command)

dir1="C:"+os.path.sep+"Users"+os.path.sep+"619635"
checkDir(dir1)
print(dir1)
dir2="C:"+os.path.sep+"Users"+os.path.sep+"619636"
checkDir(dir2)

execute(dir)
