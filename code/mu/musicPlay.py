from time import sleep
import pygame
import sys
import random
import keyboard


_songs = ['/MSCS/Projects/emosic/romantic.mp3','/MSCS/Projects/emosic/joy.mp3', '/MSCS/Projects/emosic/relax.mp3', '/MSCS/Projects/emosic/rock.mp3']
_currently_playing_song = None

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
        print "Playing..."
        clock.tick(1000)

def playmusic(soundfile):
    """Stream music with mixer.music module in blocking manner.
       This will stream the sound from disk while playing.
    """
    #pygame.init()
    #pygame.mixer.init()
    clock = pygame.time.Clock()
    pygame.mixer.music.load(soundfile)
    pygame.mixer.music.play()
    i=0
    while pygame.mixer.music.get_busy():
    	#print "Playing... "
        print "duration",pygame.mixer.music.get_pos()
  
       	#if not keyboard.is_pressed('n'):
        	# if(pygame.mixer.music.get_volume() < 1.0):
        	# 	i +=0.1
        	# 	pygame.mixer.music.set_volume(i)
        if pygame.mixer.music.get_pos()>5000:
        	print "check"
        	pygame.mixer.music.stop()
        	play_next_song()
        #play_a_different_song()
        	
        clock.tick(1000)
        

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
    print next_song
    while next_song == _currently_playing_song:
    	print _currently_playing_song
        next_song = random.choice(_songs)
        print next_song
    _currently_playing_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()

def play_next_song():
	global _songs
	_songs = _songs[1:] + [_songs[0]] # move current song to the back of the list 
	pygame.mixer.music.load(_songs[0])
	pygame.mixer.music.play()
 

    

try:
	initMixer()
	#filename = '/MSCS/Projects/emosic/romantic.mp3'
	filename = random.choice(_songs)
	print filename
	#flag = keyboard.is_pressed('n')
	#_currently_playing_song = None
	#play_next_song(_songs)
	playmusic(filename)
	#play_a_different_song()

except KeyboardInterrupt:	# to stop playing, press "ctrl-c"
    stopmusic()
    print "\nPlay Stopped by user"
# except Exception:
# 	print "unknown error"
	
print "Done"
#if __name__ == '__main__':
