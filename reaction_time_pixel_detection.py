from mss import mss
from time import sleep
import pyautogui as pg

green_color = (75, 219, 106)

# Some random coordinate that turns green
pix = {'left': 1503, 'top': 474, 'width': 1, 'height': 1}

def main():
    print("Please open https://humanbenchmark.com/tests/reactiontime on your web browser.")
    print("Press enter to continue...", end='')
    input()

    with mss() as sct:
        rounds = 0
        max_rounds = 5
        while rounds < max_rounds:
            pg.moveTo(pix['left'], pix['top'])
            pg.leftClick()
            while True:
                current = sct.grab(pix).rgb
                current = (current[0], current[1], current[2])
                if current == green_color:
                    pg.moveTo(pix['left'], pix['top'])
                    pg.leftClick()
                    break
            sleep(0.5)
            rounds += 1
    print("Please press 'Save score' button on your web browser.")


if __name__ == '__main__':
    main()
