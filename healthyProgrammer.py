from pygame import mixer
import time
from datetime import datetime

def music_on_loop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log(msg):
    with open("mylog.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}")


if __name__ == '__main__':
    music_on_loop("water.mp3", "stop")
    init_water = time.time()
    init_eyes = time.time()
    init_ex = time.time()
    water = 5
    ex = 15
    eye = 25
    while True:
        if time.time() - init_water > water:
            print("Enter drank to stop")
            music_on_loop("water.mp3", input())
            init_water = time.time()
            log("Drank water at")
