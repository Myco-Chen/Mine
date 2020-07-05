import random
import pgzrun

WIDTH = 1000
HEIGHT = 200

button = Actor('重置')
button.pos = [950, 30]

cards = []
flip = []
img = ['禾木', '禾木', '桃子', '桃子', '乌拉乎', '乌拉乎']

random.shuffle(img)
for i in range(6):
    card = Actor(img[i])
    card.person = img[i]
    card.pos = [100 + 150 * i, 100]
    cards.append(card)


def draw():
    screen.clear()
    screen.blit('背景', [0, 0])
    for card in cards:
        card.draw()
    button.draw()


def on_key_down(key):
    if key == keys.SPACE:
        for card in cards:
            card.image = '背面'


def on_mouse_down(pos):
    for card in cards:
        if card.collidepoint(pos):
            card.image = card.person
            flip.append(card.image)

            l = len(flip)
            if l == 2:
                if flip[0] == flip[1]:
                    print('正确')
                else:
                    print('错误，请点击重置按钮')
            if l == 4:
                if flip[2] == flip[3]:
                    print('正确')
                else:
                    print('错误，请点击重置按钮')

    if button.collidepoint(pos):
        random.shuffle(img)
        flip.clear()
        i = 0
        for card in cards:
            card.image = img[i]
            card.person = img[i]
            i += 1

pgzrun.go()