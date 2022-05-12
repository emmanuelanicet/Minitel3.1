#!/usr/bin/env python3

import os,time, sys
os.system('clear')
snk = ["ascii/file1.txt","ascii/file2.txt","ascii/file3.txt","ascii/file4.txt","ascii/file5.txt","ascii/file6.txt"]

def animator(filesname, delay = 0.4 , repeat = 10):
    frames = []
    for name in filesname: 
        with open(name,"r", encoding="utf8") as f : 
            frames.append(f.readlines())
    for i in range (repeat):
        for frame in frames: 
            sys.stdout.write("".join(frame))
            time.sleep(delay)
            os.system('clear')

def printanimation():
    while True: 
        animator(snk, delay = 0.2, repeat =100)

printanimation()