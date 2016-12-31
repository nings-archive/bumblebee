# bumblebee by ning
# ningyuan.sg@gmail.com
import sys, time, json
import pyautogui, pygame.mixer, keyboard


# CONFIG INITIALISATION
pygame.mixer.init()
try:
    with open('config.json', 'r') as file:
        CONFIG = json.load(file)
except FileNotFoundError:
    print('ERROR: config.json not found')
    time.sleep(5)
    sys.exit()

# MUSIC INITIALISATION
global is_playing, was_playing
is_playing = False
was_playing = False
BUMBLEBEE = 'bumblebee.mp3'
EXIT = 'exit.ogg'
pygame.mixer.music.load(BUMBLEBEE)
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
pygame.mixer.music.pause()

class Key_Inputs:
    def ctrl(click):
        def press_ctrl(self):
            keyboard.send('ctrl', do_release=False)
            click(self)
            keyboard.send('ctrl', do_press=False, do_release=True)
        return press_ctrl

    def alt(click):
        def press_alt(self):
            keyboard.send('alt', do_release=False)
            click(self)
            keyboard.send('alt', do_press=False, do_release=True)
        return press_alt

    def left_click(self):
        pyautogui.click()

    def right_click(self):
        pyautogui.click(button='right')
    
    @alt
    def alt_ping(self):
        pyautogui.click()

    @ctrl
    @alt
    def ctrl_alt_ping(self):
        pyautogui.click()

def main():
    key_inputs = Key_Inputs()
    global is_playing, was_playing

    if keyboard.is_pressed(CONFIG['left_click']):
        key_inputs.left_click()
        is_playing = True
    elif keyboard.is_pressed(CONFIG['right_click']):
        key_inputs.right_click()
        is_playing = True
    elif keyboard.is_pressed(CONFIG['alt_ping']):
        key_inputs.alt_ping()
        is_playing = True
    elif keyboard.is_pressed(CONFIG['ctrl_alt_ping']):
        key_inputs.ctrl_alt_ping()
        is_playing = True
    elif keyboard.is_pressed(CONFIG['terminate']):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(EXIT)
        pygame.mixer.music.play()
        time.sleep(1)
        sys.exit()
    else:
        is_playing = False
    
    if (is_playing is not was_playing) and (is_playing is True):
        pygame.mixer.music.unpause()
        was_playing = is_playing
    elif (is_playing is not was_playing) and (is_playing is False):
        pygame.mixer.music.pause()
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

    while True:
        main()

