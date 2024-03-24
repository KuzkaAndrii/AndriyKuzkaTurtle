from MyWord import cut
from geomfigure import *
def make_d(l):
    if l[0]=="Triangle":
        name_o=Triangle(l[1:])
    elif l[0]=="Rectangle":
        name_o=Rectangle(l[1:])
    elif l[0]=="Trapeze":
        name_o=Trapeze(l[1:])
    elif l[0]=="Parallelogram":
        name_o=Parallelogram(l[1:])
    else:
        name_o=Circle(l[1:])
    return name_o
if __name__=="__main__":
    txtl= ('input01.txt', 'input02.txt', 'input03.txt')
    txty= ('ans01.txt', 'ans02.txt', 'ans03.txt')
    for it in range(3):
        f=open(txtl[it], 'rt')
        g=open(txty[it], 'at')
        lis=f.readlines()
        mS=0.00
        mP=0.00
        resP=None
        resS=None
        for i in lis:
            arg=cut(i)
            o=make_d(arg)
            print(o.P(), o.S(), file=g)
            if o.P()>mP:
                del resP
                resP=o
                mP=o.P()
            if o.S()>mS:
                del resS
                resS=o
                mS=o.S()
            del o
        print("P:", resP)
        print("S:", resS)
        del resP
        del resS
        f.close()
        g.close()