import subprocess, pyautogui, time, glob, os

def add_word(word, option):
    """
    a RPA that adds a word to Anki
    """
    subprocess.Popen(r'C:\Program Files\Anki\anki.exe') # opening the anki program
    time.sleep(2)
    pyautogui.press('a') # opening the add window - in the front area

    n_example = len(glob.glob(f'./words/{word}/meaning_{option}/example[0-9].txt')) # numbers of examples

    time.sleep(2)
    for example_number in range(n_example):
        with open(f'./words/{word}/meaning_{option}/example{example_number}.txt', 'r') as file:
            pyautogui.write('Example:' + next(file)) # write the example
            pyautogui.press('f3') # attach picture/audio/video
            pyautogui.press('alt', 'd') # path insert mode
            pyautogui.write(os.getcwd() + 'something') # TODO
            if example_number == 0: # implies that the example was already given in the front area, move to back area
                time.sleep(2)
                pyautogui.press('tab')

add_word('bait', 2)