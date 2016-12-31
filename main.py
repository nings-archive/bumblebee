# bumblebee by ning
# ningyuan.sg@gmail.com
import sys, time, json
import pyautogui, pygame.mixer, keyboard

# INITIALISATION
try:
    with open('config.json', 'r') as file:
        CONFIG = json.load(file)
except FileNotFoundError:
    print('ERROR: config.json not found')
    time.sleep(5)
    sys.exit()

class Music:
    def __init__(self):
        pygame.mixer.init()
        self.EXIT = 'exit.ogg'
        self.BUMBLEBEE = 'bumblebee.mp3'
        pygame.mixer.music.load(self.BUMBLEBEE)
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)  # -1 repeats indefinitely
        pygame.mixer.music.pause()
        self.is_playing = False
        self.was_playing = False

    def pause(self):
        pygame.mixer.music.pause()

    def resume(self):
        pygame.mixer.music.unpause()

    def exit(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(self.EXIT)
        pygame.mixer.music.play()
        time.sleep(1)

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
    music = Music()
    key_inputs = Key_Inputs()

    if keyboard.is_pressed(CONFIG['left_click']):
        key_inputs.left_click()
        music.is_playing = True
    elif keyboard.is_pressed(CONFIG['right_click']):
        key_inputs.right_click()
        music.is_playing = True
    elif keyboard.is_pressed(CONFIG['alt_ping']):
        key_inputs.alt_ping()
        music.is_playing = True
    elif keyboard.is_pressed(CONFIG['ctrl_alt_ping']):
        key_inputs.ctrl_alt_ping()
        music.is_playing = True
    elif keyboard.is_pressed(CONFIG['terminate']):
        music.exit()
        sys.exit()
    else:
        music.is_playing = False  # FIX THIS
    
    if (music.is_playing is not music.was_playing) and (music.is_playing is True):
        music.resume()
        music.was_playing = music.is_playing
    elif (music.is_playing is not music.was_playing) and (music.is_playing is False):
        music.pause()
        music.was_playing = music.is_playing

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
