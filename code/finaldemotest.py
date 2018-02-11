
########### Python 3.6 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json, cv2
import numpy as np
import cv2
import os
import keyboard
from time import sleep
import time
import pygame
import sys
import random
import keyboard
import threading
from threading import Thread
# from multiprocessing import Process

###############################################
#### Update or verify the following values. ###
###############################################

#_songs = ['mu/romantic.mp3','mu/joy.mp3', 'mu/relax.mp3', 'mu/rock.mp3']
_songs = ['mu/romantic.mp3','mu/romantic.mp3','mu/romantic.mp3','mu/relax.mp3','mu/relax.mp3','mu/relax.mp3','mu/rock.mp3','mu/rock.mp3','mu/rock.mp3']
_currently_playing_song = None
_songsindex = 0
ans = {}
ans['answer'] = 'happy'
##############################################################################################

def playsound(soundfile):
    """Play sound through default mixer channel in blocking manner.
       This will load the whole sound into memory before playback
    """

    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound(soundfile)
    clock = pygame.time.Clock()
    sound.play()
    while pygame.mixer.get_busy():
        print("Playing...")
        #clock.tick(1000)

def playmusic(soundfile):
    """Stream music with mixer.music module in blocking manner.
       This will stream the sound from disk while playing.
    """
    #: No need for global declaration to just read value
    #pygame.init()
    #pygame.mixer.init()
    #clock = pygame.time.Clock()
    pygame.mixer.music.load(soundfile)
    pygame.mixer.music.play()
    time.sleep(10)

    while pygame.mixer.music.get_busy():

        if ans['answer'] == 'sad':
            pygame.mixer.music.stop()
            print("Try new Genre as you dont like this song !")
            print("It will start in 2 sec")
            #time.sleep(2)
            play_next_genre()
        else:
            play_next_song()



def stopmusic():
    """stop currently playing music"""
    pygame.mixer.music.stop()

def getmixerargs():
    pygame.mixer.init()
    freq, size, chan = pygame.mixer.get_init()
    return freq, size, chan


def initMixer():
    BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
    FREQ, SIZE, CHAN = getmixerargs()
    pygame.init()
    pygame.mixer.init(FREQ, SIZE, CHAN, BUFFER)


def play_a_different_song():
    global _currently_playing_song, _songs
    next_song = random.choice(_songs)
    print(next_song)
    while next_song == _currently_playing_song:
        print(_currently_playing_song)
        next_song = random.choice(_songs)
        print(next_song)
    _currently_playing_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()

def play_next_song():
    global _songs
    global _songsindex
    if _songsindex == 8:
        _songsindex = 0
    else:
        _songsindex =_songsindex+1
    pygame.mixer.music.load(_songs[_songsindex])
    print("Now playing song number : {}".format(_songsindex))
    pygame.mixer.music.play()
    time.sleep(15)


def play_next_genre():
    global _songs
    global _songsindex
    _songsindex+=3;
    if _songsindex > 8:
        _songsindex = 0
    else:
        _songsindex+=1
    pygame.mixer.music.load(_songs[_songsindex])
    print("Now playing song number : {}".format(_songsindex))
    pygame.mixer.music.play()
    time.sleep(15)



################################################
# Replace the subscription_key string value with your valid subscription key.
subscription_key = 'a964c99ef5a944d99e2d50e1fea958d0'

# other keys for demo:



# Replace or verify the region.
#
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
uri_base = 'https://westcentralus.api.cognitive.microsoft.com'

# Request headers.
headers = {
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

# Request parameters.
params = {
    'returnFaceId': 'false',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'smile,emotion',
}


def find_emotions(path):
    # pathToFileInDisk = r'C:\Users\girls.jpg'
    global ans
    #ans['answer'] = 'happy'

    pathToFileInDisk = r'C:\Users\Karan Tyagi\Desktop\add to github\0 - hackbeanspot\code\{}'.format(path)
    with open( pathToFileInDisk, 'rb' ) as f:
        data = f.read()


    try:
        # Execute the REST API call and get the response.
        response = requests.request('POST', uri_base + '/face/v1.0/detect', json=None, data=data, headers=headers, params=params)
        # print ('Response:')
        parsed = json.loads(response.text)
        # print (json.dumps(parsed, sort_keys=True, indent=2))
        frame_num = 1;
        for face in parsed:
            #print(' Frame {} :\t'.format(frame_num),face['faceAttributes']['emotion'])
            #print(' Smile {} :\t'.format(fno),face['faceAttributes']['smile'])
            result =  (face['faceAttributes']['emotion']['sadness'] + face['faceAttributes']['emotion']['neutral'] + face['faceAttributes']['emotion']['fear'] +
            face['faceAttributes']['emotion']['disgust'] + face['faceAttributes']['emotion']['contempt'] +
            face['faceAttributes']['emotion']['anger'])

            if result > face['faceAttributes']['emotion']['happiness']:
                ans['answer'] = 'sad'
            else:
                ans['answer'] ='happy'

            # print(sum)
            #print('\t{}'.format(face['faceAttributes']['emotion']['happiness']).ljust(18)+'{}'.format(face['faceAttributes']['emotion']['surprise']).ljust(18)+'{}'.format(face['faceAttributes']['emotion']['neutral']).ljust(18)+'{}'.format(face['faceAttributes']['emotion']['sadness']).ljust(18)+'{}'.format(face['faceAttributes']['emotion']['disgust']).ljust(18)+'{}'.format(face['faceAttributes']['emotion']['anger']).ljust(18)+'{}'.format(face['faceAttributes']['emotion']['contempt']).ljust(18)+'{}'.format(face['faceAttributes']['emotion']['fear']).ljust(18)+"   "+ans['answer'])
            print('\t\t\t\t---------- '+ ans['answer'])
            frame_num+=1

    except Exception as e:
        print('Error:')
        print(e)


def playvideo():
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    img_counter = 1
    timer = 1
    #print('\n\tHappiness'.ljust(18)+'Surprise'.ljust(18)+'Neutral'.ljust(18)+'Sadness'.ljust(18)+'Disgust'.ljust(18)+'Anger'.ljust(18)+'Contempt'.ljust(18)+'Fear'.ljust(18))
    while rval:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        img_name = "img_frame{}.jpg".format(img_counter)

        # print("Created img_frame{}.jpg".format(img_counter))
        key = cv2.waitKey(50) # 1000/50 = 20 FPS
        if timer % 20 == 0:
            print('Time :  {}'.format(timer / 20), end='\r')

        # print(type(frame))

        # start processing the image emotions
        #if
        if timer / 20 == 10 :
            cv2.imwrite(img_name, frame)
            #find_emotions(img_name)
            #key = cv2.waitKey(50) # milliseconds
            timer=1

            if os.path.isfile(img_name):
                os.remove(img_name)
                # deleting the image after processing it
                #print("Deleted img_frame{}.jpg".format(i))
            else: ## Show an error ##
                print("Error: %s file not found" % myfile)

            continue

        timer+=1

        # take less frames
        # end processing this frame

        # deleting the image after processing it
        # print("Deleted img_frame{}.jpg".format(img_counter))

        # this can be put in a try catch box
        ## if file exists, delete it ##
        img_counter+=1
        if key == 27: # exit on ESC
            break

    cv2.destroyWindow("preview")
    vc.release()

    #print("\n\n\tAll images deleted. Memory freed. Enjoy Lappy. ;)")

def backgroundmusic():
    initMixer()
    global _songsindex
    _songsindex = 0   # random number can also be used
    filename = (_songs[_songsindex ])

    print(filename)
    playmusic(filename)

# playvideo()
# backgroundmusic()

def printit():
    # run your code
    print('Time :  ', end='\r')
    threading.Timer(1.0, printit).start()
    end = time.time()
    elapsed = int(end - start)
    print('Time :  {}'.format(elapsed), end='\r')


if __name__ == '__main__':
    #start = time.time()
    #printit()
    print('\n---- Freeze ur expressions near timer : 10 ------\n')
    p1 = Thread(target=backgroundmusic)
    p1.start()
    p2 = Thread(target=playvideo)
    p2.start()
    p1.join()
    p2.join()




####################################
