#1.C
#2.D
import time
start_time = time.time()
def on_mouse_down(pos):
    for b in balls:
        if b.collidepoint(pos):
            s.append(b.number)
            l = len(s)
            if l == 1:
                if s[0] == 1:
                    print('正确')
                    end_time = time.time()
                    print(end_time-start_time)
            else:
                print('错误')