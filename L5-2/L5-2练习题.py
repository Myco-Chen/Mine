#1.
#def draw():
#   screen.clear()
#   hetaos = [hetao1,hetao2, hetao3]
#   for i in hetaos:
#       i.draw()
#def on_mouse_down():
#   hetaos = [hetao1, hetao2, hetao3]
#   for c in hetaos:
#       c.image = '小核桃'
#    pgzrun.go()

#2.D

#3.
import random
pic = ['禾木', '禾木', '桃子', '桃子', '乌拉乎', '乌拉乎']
pic2 = ['禾木 1', '禾木', '桃子 1', '桃子', '乌拉乎1', '乌拉乎']
random.shuffle(pic)
for i in range(6):
    if pic[i] == pic1[i]:
        print('相同！ ！')
    else:
        print('不相同')