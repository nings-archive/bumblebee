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
    pyautogui.keyDown('alt')
    left_click()
    pyautogui.keyUp('alt')

def ctrl_alt_click():
    pyautogui.keyDown('ctrl')
    alt_click()
    pyautogui.keyUp('ctrl')

def main():
    if keyboard.is_pressed('-'):
        left_click()
    elif keyboard.is_pressed('='):
        right_click()
    elif keyboard.is_pressed('['):
        alt_click()
    elif keyboard.is_pressed(']'):
        ctrl_alt_click()
    elif keyboard.is_pressed('\\'):
        play_exit()
        time.sleep(1)
        sys.exit()
    time.sleep(0.025)

print('''
Hold down: 
'-' for left click      '=' for right;
'[' for alt-pings       ']' for ctrl-alt-pings;
'\\' for script exit.''')
while True:
    main()
