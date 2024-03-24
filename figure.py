import copy
import math
from turtle import *
class Figure:
    def __init__(self, pos, col="black"):
        assert isinstance(pos, list)
        assert isinstance(col, str)
        self._x=pos[0]
        self._y=pos[1]
        self._exist=False
        self._col=col
    def is_figure(self):
        if self._exist:
            print("Yes")
        else:
            print("No")
    def new_color(self, col):
        assert  isinstance(col, str)
        self._col=col
    def draw(self):
        up()
        self._exist=True
        goto(self._x, self._y)
        pencolor(self._col)
        down()
    def delfig(self):
        assert self._exist==True
        self._exist=False
        sc=self._col
        self._col="white"
        self.draw()
        self._col=sc
        self._exist=True
    def gotofig(self, newpos):
        assert isinstance(newpos, list)
        if self._exist==True:
            self.delfig()
            self._x = newpos[0]
            self._y = newpos[1]
            self.draw()
        else:
            self._x = newpos[0]
            self._y = newpos[1]
class Polygon(Figure):
    def __init__(self, pos, arg, d, col='black'):
        super().__init__(pos, col)
        assert isinstance(arg, list)
        assert isinstance(d, list)
        assert len(d)==len(arg)
        self._arg=copy.copy(arg)
        self._d=copy.copy(d)
    def draw(self):
        super().draw()
        for i in range(len(self._d)):
            fd(self._d[i])
            lt(180-self._arg[i])


class Circle(Figure):
    def __init__(self, pos, r, col="black"):
        super().__init__(pos, col)
        self._r=r/2
    def draw(self):
        self._y=(self._y-self._r)
        super().draw()
        circle(self._r)
        self._y=(self._y+self._r)
class Triangle(Polygon):
    def __init__(self, pos, d, col='black'):
        super().__init__(pos, [60, 60, 60], [d, d, d], col)
class Rectangle(Polygon):
    def __init__(self, pos, a, b, col='black'):
        super().__init__(pos, [90, 90, 90, 90], [a, b, a, b], col)
class Square(Rectangle):
    def __init__(self, pos, a, col='black'):
        super().__init__(pos, a, a, col)
class Trapeze(Polygon):
    def __init__(self, pos, a, b, h, col="black"):
        assert a-b!=0.0
        c=(((b-a)/2)**2+h**2)**0.5
        ar = math.degrees(math.asin((h / c)))
        if a>b:
            super().__init__(pos, [ar, 180 - ar, 180 - ar, ar], [a, c, b, c], col)
        else:
            super().__init__(pos, [180-ar, ar, ar, 180-ar], [a, c, b, c], col)
if __name__=="__main__":
    print('Hello, world!')