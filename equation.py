class Equation:
    INF_SOLS = (0, 0, 0, 0, 0)
    NO_SOLS = tuple()

    def __init__(self, b, c):
        self._b = b
        self._c = c

    def solve(self):
        if self._b == 0:
            if self._c == 0:
                return Equation.INF_SOLS
            else:
                return Equation.NO_SOLS
        else:
            x = -1 * self._c / self._b
            return tuple(x)
class QuadraticEquation(Equation):
    def __init__(self, a, b, c):
        self._a=a
        super().__init__(b, c)

    def solve(self):
        if self._a==0:
            return super().solve()
        else:
            D=self._b-4*self._a*self._c
            if D>0:
                x1=(-1*self._b-D**0.5)/(2*self._a)
                x2=(-1*self._b+D**0.5)/(2*self._a)
                return (x1, x2)
            elif D==0:
                return tuple(-1*self._b/(2*self._a))
            else:
                return super().NO_SOLS

if __name__ == "__main":
    print('Hello, world')