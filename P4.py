from equation import *
class BiQuadraticEquation(QuadraticEquation):
    def solve(self):
        r=super().solve()
        if r==Equation.NO_SOLS:
            return  Equation.NO_SOLS
        if r==Equation.INF_SOLS:
            return Equation.INF_SOLS
        res=[]
        for t in r:
            if t>0:
                res.append(-1 * t ** 0.5)
                res.append(t ** 0.5)
            elif t==0:
                res.append(0.0)
if __name__ == "__main":
    lin_eq1=Equation(2, -1)
