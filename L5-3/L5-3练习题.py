#1.A
#2.B
#3.
import pgzrun
import random
pacman = Actor('向右的吃豆人')
pacman.pos = [250, 250]
bean = Actor('豆子')
bean.x = random.randint(100, 400)
bean.y = random.randint(100, 400)
def draw():
    bean.draw()
    pacman.draw()
pgzrun.go()