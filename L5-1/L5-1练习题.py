#1.A
#2.A
#3.↓
import pgzrun
card = Actor('桃子')
card.image = '背面'
card.person = '桃子'
card.pos = [100, 100]
def draw():
    card.draw()
def on_mouse_down(pos):
    if card.collidepoint(pos):
        card.image = card.person
pgzrun.go()