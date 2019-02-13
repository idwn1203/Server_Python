import sys
import subprocess

def ScreenMenu():
    print("1: atom")
    print("2: excel")
    print("3: exit")

while 1:
    ScreenMenu()
    print("---------\nChoose Menu :")
    KeyInput = input()
    Menu = int(KeyInput)
    if Menu == 1:
        print("hi")
        subprocess.call('ls')
        subprocess.run(['notepad','test.txt'])
    elif Menu == 2:
        subprocess.run('Atom')
        #num +=1
    elif Menu == 3:
         sys.exit()


