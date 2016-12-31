# bumblebee by ning
# ningyuan.sg@gmail.com
import sys, time, json
import pyautogui, pygame.mixer, keyboard

# INITIALISATION
pygame.mixer.init()
EXIT = 'exit.ogg'
BUMBLEBEE = 'bumblebee.mp3'

try:
    with open('config.json', 'r') as file:
        CONFIG = json.load(file)
except FileNotFoundError:
    print('ERROR: config.json not found')
    time.sleep(5)
    sys.exit()

global is_playing, was_playing
is_playing = False
was_playing = False

# MUSIC FUNCTIONS
def load_bumblebee():
    try:
        pygame.mixer.music.load(BUMBLEBEE)
        pygame.mixer.music.set_volume(0.5)
    except pygame.error:
        print('ERROR: exit.ogg not found')
        time.sleep(5)
        sys.exit()

def load_exit():
    try:
        pygame.mixer.music.load(EXIT)
    except pygame.error:
        print('ERROR: exit.ogg not found')
        time.sleep(5)
        sys.exit()

def pause_bumblebee():
    pygame.mixer.music.pause()

def unpause_bumblebee():
    pygame.mixer.music.unpause()

# MOUSE/KEYBOARD FUNCTIONS
def play_exit():
    global is_playing
    is_playing = False
    pygame.mixer.music.stop()
    load_exit()
    pygame.mixer.music.play()

def left_click():
    global is_playing
    is_playing = True
    pyautogui.click()

def right_click():
    global is_playing
    is_playing = True
    pyautogui.click(button='right')
    pass

def alt_ping():
    global is_playing
    is_playing = True
    keyboard.send('alt', do_release=False)
    left_click()
    keyboard.send('alt', do_press=False, do_release=True)

def ctrl_alt_ping():
    global is_playing
    is_playing = True
    keyboard.send('ctrl', do_release=False)
    alt_ping()
    keyboard.send('alt', do_press=False, do_release=True)
    keyboard.send('ctrl', do_press=False, do_release=True)

def main():
    global is_playing, was_playing
    if keyboard.is_pressed(CONFIG['left_click']):
        left_click()
    elif keyboard.is_pressed(CONFIG['right_click']):
        right_click()
    elif keyboard.is_pressed(CONFIG['alt_ping']):
        alt_ping()
    elif keyboard.is_pressed(CONFIG['ctrl_alt_ping']):
        ctrl_alt_ping()
    elif keyboard.is_pressed(CONFIG['terminate']):
        play_exit()
        time.sleep(1)
        sys.exit()
    else:
        is_playing = False
    
    if (is_playing is not was_playing) and (is_playing is True):
        unpause_bumblebee()
        was_playing = is_playing
    elif (is_playing is not was_playing) and (is_playing is False):
        pause_bumblebee()
        was_playing = is_playing

    time.sleep(0.001)

if __name__ == '__main__':
    print('''
    bumblebee by ning. Hold down: 
    '{}' for left click      '{}' for right;
    '{}' for alt-pings       '{}' for ctrl-alt-pings;
    '{}' for script exit.
    '''.format(
        CONFIG['left_click'],
        CONFIG['right_click'],
        CONFIG['alt_ping'],
        CONFIG['ctrl_alt_ping'],
        CONFIG['terminate']
        ))

    load_bumblebee()
    pygame.mixer.music.play(-1)  # -1 -> repeats indefintiely
    pause_bumblebee()

    while True:
        main()
