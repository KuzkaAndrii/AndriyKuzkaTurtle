from figure import *
class Car:
    def __init__(self, pos, siz=10):
        assert isinstance(pos, list)
        assert type(siz) is int or type(siz) is float
        self._hom=siz/10
        self._x=pos[0]
        self._y=pos[1]
        self._fw=Circle([self._x+5*self._hom, self._y-5*self._hom], 10*self._hom)
        self._sw=Circle([self._x+25*self._hom, self._y-5*self._hom], 10*self._hom)
        self._cab=Trapeze([self._x, self._y], 30*self._hom, 20*self._hom, 10*self._hom)
        self._wd=Rectangle([self._x+5*self._hom, self._y+5*self._hom], 20*self._hom, 5*self._hom)
    def _rego(self):
        self._fw = Circle([self._x + 5 * self._hom, self._y - 5 * self._hom], 10 * self._hom)
        self._sw = Circle([self._x + 25 * self._hom, self._y - 5 * self._hom], 10 * self._hom)
        self._cab = Trapeze([self._x, self._y], 30 * self._hom, 20 * self._hom, 10 * self._hom)
        self._wd = Rectangle([self._x + 5 * self._hom, self._y + 5 * self._hom], 20 * self._hom, 5 * self._hom)
    def go(self, step=10):
        self._fw.draw()
        self._sw.draw()
        self._cab.draw()
        self._wd.draw()
        for i in range(step):
            self._fw.gotofig([self._fw._x+5*self._hom, self._fw._y])
            self._sw.gotofig([self._sw._x+5*self._hom, self._sw._y])
            self._cab.gotofig([self._cab._x+5*self._hom, self._cab._y])
            self._wd.gotofig([self._wd._x+5*self._hom, self._wd._y])
            self._x=self._x+5*self._hom
            self._y=self._y+5*self._hom
if __name__=="__main__":
    shape("turtle")
    hideturtle()
    speed(20)
    siz=float(input())
    c=Car([0, 0], siz)
    c.go()
    exitonclick()
