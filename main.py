import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    # Draw the rectangle f or birds
    for i in range(500, 560):
        for j in range(410, 563):
            if data[i, j] < 100:
                hit("down")
                # pyautogui.keyDown("down")
                return

    for i in range(500, 580):
        for j in range(510, 680):
            if data[i, j] < 100:
                hit("up")
                return
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time. sleep(3)

    hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

        # print(asarray(image))
'''
        # Draw the rectangle for cactus
        for i in range (470, 505):
            for j in range(550, 690):
                data[i, j] = 0

        # Draw the rectangle f or birds
        for i in range(474, 495):
            for j in range(410, 550):
                data[i, j] = 171

        image.show()
        break
'''

