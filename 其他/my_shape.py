import turtle
t = turtle.Pen()
class draw:
    def mycircle(self,size,filled,color):
        t.color(color)
        if filled == True:
            t.begin_fill()
        t.circle(size)
        if filled == True:
            t.end_fill()
    
    def mysquare(self,size,filled,color):
        t.color(color)
        if filled == True:
            t.begin_fill()
        for i in range(4):
            t.forward(size)
            t.left(90)
        if filled == True:
            t.end_fill()

    def mystar(self,size,filled,color):
        t.color(color)
        if filled == True:
            t.begin_fill()
        for x in range(18):
            t.forward(size)
            if x % 2 == 0:
                t.left(175)
            else:
                t.left(225)
        if filled == True:
            t.end_fill()
    
    def reset(self):
        t.reset()

    def clear(self):
        t.clear()

class d(draw):
    pass