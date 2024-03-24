class Triangle:
    def __init__(self, l):
        if isinstance(l, Triangle):
            self.a = l.a
            self.b = l.b
            self.c = l.c
            self.ex=l.ex
        else:
            self.a = int(l[0])
            self.b = int(l[1])
            self.c = int(l[2])
            if max(self.a,self.b,self.c)<self.a+self.b+self.c-max(self.a,self.b,self.c) and min(self.a,self.b,self.c)>0:
                self.ex=True
            else:
                self.ex=False

    def P(self):
        if self.ex==True:
            return self.a+self.b+self.c
        else:
            return -1
    def S(self):
        if self.ex==True:
            return (((self.a + self.b + self.c) * (self.a + self.b - self.c) * (self.a + self.c - self.b) * (
                        self.c + self.b - self.a)) ** 0.5) / 4
        else:
            return -1
class Rectangle:
    def __init__(self, l):
        if isinstance(l, Rectangle):
            self.a = l.a
            self.b = l.b
            self.ex=l.ex
        else:
            self.a = int(l[0])
            self.b = int(l[1])
            if self.a*self.b>0:
                self.ex=True
            else:
                self.ex=False
    def P(self):
        if self.ex==True:
            return (self.a+self.b)*2
        else:
            return -1
    def S(self):
        if self.ex==True:
            return self.a * self.b
        else:
            return -1
class Trapeze:
    def __init__(self, l):
        if isinstance(l, Trapeze):
            self.a = l.a
            self.b = l.b
            self.c = l.c
            self.d = l.d
            self.ex=l.ex
        else:
            self.a = int(l[0])
            self.b = int(l[1])
            self.c = int(l[2])
            self.d = int(l[3])
            if self.a+self.b+self.c+self.d-2*max(self.a,self.b,self.c,self.d)>0 and min(self.a,self.b,self.c,self.d)>0:
                q1=min(self.c, self.d, abs(self.a-self.b))
                q2=max(self.c, self.d, abs(self.a-self.b))
                p=self.c+self.d+abs(self.a-self.b)
                if q1>0 and p-2*q2>0:
                    self.ex = True
                else:
                    self.ex=False
            else:
                self.ex=False
    def P(self):
        if self.ex==True:
            return self.a + self.b + self.c + self.d
        else:
            return -1
    def S(self):
        if self.ex==True:
            p = abs(self.a-self.b)
            return ((self.a + self.b) * (((self.d + p + self.c) * (p + self.d - self.c) * (p + self.c - self.d) * (
                        self.c + self.d - p)) ** 0.5) / 4) / p
        else:
            return -1
class Parallelogram:
    def __init__(self, l):
        if isinstance(l, Parallelogram):
            self.a = l.a
            self.b = l.b
            self.h = l.h
            self.ex=l.ex
        else:
            self.a = int(l[0])
            self.b = int(l[1])
            self.h = int(l[2])
            if min(self.a,self.b,self.h)>0:
                self.ex=True
            else:
                self.ex=False
    def P(self):
        if self.ex==True:
            return (self.a + self.b) * 2
        else:
            return -1
    def S(self):
        if self.ex==True:
            return min(self.a, self.b) * self.h
        else:
            return -1
class Circle:
    def __init__(self, l):
        if isinstance(l, Circle):
            self.r = l.r
            self.ex=l.ex
        else:
            self.r = int(l[0])
            if self.r>0:
                self.ex=True
            else:
                self.ex=False
    def P(self):
        if self.ex==True:
            return self.r * 3.1415 * 2
        else:
            return -1
    def S(self):
        if self.ex==True:
            return self.r ** 2 * 3.1415
        else:
            return -1
if __name__=="__main__":
    print("Hello, world!")