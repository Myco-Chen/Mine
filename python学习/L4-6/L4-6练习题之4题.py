import pgzrun
from pgzero.keyboard import keyboard


WITTH = 500
HEIGHT = 500

hetao = Actor('小核桃')
hetao.x, hetao.y = 100, 200

def draw():
    screen.clear()
    hetao.draw()

def update():
    if keyboard.space:
        hetao.y += 5
        if hetao.y >= 500:
            hetao.x, hetao.y = 100, 200

pgzrun.go()