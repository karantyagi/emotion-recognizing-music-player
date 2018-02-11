import keyboard #Using module keyboard
import threading
import time


def printit():
    # run your code
    print('Time :  ', end='\r')
    threading.Timer(1.0, printit).start()
    end = time.time()
    elapsed = int(end - start)
    print('Time :  {}'.format(elapsed), end='\r')

start = time.time()
printit()

'''while True:#making a loop
    try: #used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('a'): #if key 'a' is pressed
            print('You Pressed A Key!')
            break #finishing the loop
        else:

    except:
        break #if user pressed other than the given key the loop will break'''


import ctypes  # An included library with Python install.
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
#  Mbox('Analyzing your emotion', 'Do you like this song ?', 0)

'''import easygui as eg
# easygui.msgbox("This is a message!", title="simple gui")
eg.msgbox("Backup complete!", ok_button="Good job!")'''


'''
        '''
