#1.D
#2.D
'''
3.一

s = []
def on_mouse_down(pos):
    for b in balls:
        if b.collidepoint(pos):
            s.append(b.number)
            print(s)
'''
'''
3.二

s = []
def on_mouse_down(pos):
    for b in balls:
        if b.collidepoint(pos):
            s.append(b.number)
            l = len(s)
            if l == 1:
                if s[0] == 1:
                    print('正确')
                else:
                    print('错误，请重新开始挑战')
'''