import sys, time
import pyautogui, pygame.mixer, keyboard

pygame.mixer.init()
EXIT = sys.path[0] + '/exit.ogg'

def play_exit():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(EXIT)
    pygame.mixer.music.play()

def left_click():
    pyautogui.click()

def right_click():
    pyautogui.click(button='right')
    pass

def alt_click():
    keyboard.send('alt', do_release=False)
    left_click()

def ctrl_alt_click():
    keyboard.send('ctrl', do_release=False)
    alt_click()

def reset():
    keyboard.send('alt', do_press=False, do_release=True)
    keyboard.send('ctrl', do_press=False, do_release=True)

def main():
    if keyboard.is_pressed('-'):
        left_click()
    elif keyboard.is_pressed('='):
        right_click()
    elif keyboard.is_pressed('['):
        alt_click()
        reset()
    elif keyboard.is_pressed(']'):
        ctrl_alt_click()
        reset()
    elif keyboard.is_pressed('\\'):
        play_exit()
        time.sleep(1)
        sys.exit()
    time.sleep(0.001)

print('''
Hold down: 
'-' for left click      '=' for right;
'[' for alt-pings       ']' for ctrl-alt-pings;
'\\' for script exit.''')
while True:
    main()
