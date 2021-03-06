from ctypes import pythonapi
import subprocess, pyautogui, time, glob, os
from utils.rpa_utils import focus_screen

def add_word(word, option, scraped_info, t_sleep=1.75):
    """
    a RPA that adds a word to Anki
    """
    subprocess.Popen('C:\\Program Files\\Anki\\anki.exe') # opening the anki program
    time.sleep(t_sleep+5)
    focus_screen()
    time.sleep(t_sleep)
    pyautogui.hotkey('a') # opening the add window - in the front area

    n_example = len(glob.glob(f'./words/{word}/meaning_{option}/example[0-9].txt')) # numbers of examples

    time.sleep(t_sleep)
    pyautogui.write(word + '\n')
    
    try: # try to write the inflections
        with open(f'./words/{word}/inflections.txt') as file: # add inflection (if exist)
            pyautogui.write('Inflections: ' + file.readline() + '\n\n')
    except FileNotFoundError: # inflections not found, pass
        pass

    if scraped_info['searched word']['mp3'] != None: # adding the word pronunciation
        pyautogui.hotkey('f3') # attach picture/audio/video
        time.sleep(t_sleep)
        pyautogui.hotkey('alt', 'd') # path insert mode
        pyautogui.write(os.getcwd() + f'\\words\\{word}')
        time.sleep(t_sleep)
        pyautogui.press('enter')
        time.sleep(t_sleep)
        pyautogui.hotkey('alt', 'o')
        time.sleep(t_sleep)
        pyautogui.write(f'{word}.mp3')
        time.sleep(t_sleep)
        pyautogui.press('enter')
    
    for example_number in range(n_example):
        with open(f'./words/{word}/meaning_{option}/example{example_number}.txt', 'r') as file:
            pyautogui.write(('\n' if example_number!=0 else '') + f'Example {example_number+1}:' + next(file) + '\n') # write the example
            pyautogui.hotkey('f3') # attach picture/audio/video
            time.sleep(t_sleep)
            pyautogui.hotkey('alt', 'd') # path insert mode
            pyautogui.write(os.getcwd() + f'\\words\\{word}\\meaning_{option}')
            time.sleep(t_sleep)
            pyautogui.press('enter')
            time.sleep(t_sleep)
            pyautogui.hotkey('alt', 'o')
            time.sleep(t_sleep)
            pyautogui.write(f'example{example_number}.mp3')
            time.sleep(t_sleep)
            pyautogui.press('enter')
    
    time.sleep(t_sleep)
    pyautogui.press('tab') # switch to back

    with open(f'./words/{word}/meaning_{option}/meaning{option}.txt') as file:
        pyautogui.write(next(file)) # insert the meaning

    time.sleep(t_sleep)
    pyautogui.press('tab') # switch to back

    with open(f'./words/{word}/meaning_{option}/tag.txt') as file:
        pyautogui.write(next(file) + ' [CLAC]') # insert the vim
    
    time.sleep(t_sleep)
    pyautogui.press('tab') # switch to back
    time.sleep(t_sleep)
    pyautogui.press('enter')
    time.sleep(t_sleep)
    pyautogui.press('esc')

# add_word('bait', 2) # just testing