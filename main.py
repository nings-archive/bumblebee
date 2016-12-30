import sys, time, json
import pyautogui, pygame.mixer, keyboard

pygame.mixer.init()
EXIT = sys.path[0] + '/exit.ogg'
with open('config.json', 'r') as file:
    CONFIG = json.load(file)

def play_exit():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(EXIT)
    pygame.mixer.music.play()

def left_click():
    pyautogui.click()

def right_click():
    pyautogui.click(button='right')
    pass

def alt_ping():
    keyboard.send('alt', do_release=False)
    left_click()

def ctrl_alt_ping():
    keyboard.send('ctrl', do_release=False)
    alt_ping()

def reset():
    keyboard.send('alt', do_press=False, do_release=True)
    keyboard.send('ctrl', do_press=False, do_release=True)

def main():
    if keyboard.is_pressed(CONFIG['left_click']):
        left_click()
    elif keyboard.is_pressed(CONFIG['right_click']):
        right_click()
    elif keyboard.is_pressed(CONFIG['alt_ping']):
        alt_ping()
        reset()
    elif keyboard.is_pressed(CONFIG['ctrl_alt_ping']):
        ctrl_alt_ping()
        reset()
    elif keyboard.is_pressed(CONFIG['terminate']):
        play_exit()
        time.sleep(1)
        sys.exit()
    time.sleep(0.001)

print('''
Hold down: 
'{}' for left click      '{}' for right;
'{}' for alt-pings       '{}' for ctrl-alt-pings;
'{}' for script exit.'''.format(
    CONFIG['left_click'],
    CONFIG['right_click'],
    CONFIG['alt_ping'],
    CONFIG['ctrl_alt_ping'],
    CONFIG['terminate']
    ))
while True:
    main()
