import subprocess, pyautogui, time, os

def add_word(word, option):
    """
    a RPA that adds a word to Anki
    """
    subprocess.Popen(r'C:\Program Files\Anki\anki.exe') # opening the anki program
    time.sleep(2)
    pyautogui.press('a') # opening the add window

    os.chdir(os.getcwd() + f'\\words\\{word}\\meaning_{option}') # switching the folder to the corrrect one

add_word('bait', 2)