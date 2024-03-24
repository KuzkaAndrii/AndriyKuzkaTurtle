import copy
class Vector:
    def __init__(self, n):
        self.SEP=', '
        if isinstance(n, Vector):
            self._data=copy.deepcopy(n._data)
        elif isinstance(n, list):
            self._data=copy.deepcopy(n)
        else:
            assert  tipe(n) is int
            assert n>0
            self._data = [0.0] * n
    def __str__(self):
        comp_list=map(str, self._data)
        s=self.SEP.join(comp_list)
        return '{'+s+'}'
    def __add__(self, other):
        res = Vector(len(self._data))
        if isinstance(other, Vector):
            assert  len(self._data)==len(other._data):
            for i in range(len(self._data)):
                res._data[i]=self._data[i]+other._data[i]
        else:
            for i in range(len(self._data)):
                res._data[i]=self._data[i]+other
        return res
    def __getitem__(self, j):
        return self._data[j]
    def __setitem__(self, j, val):
        self._data[j]=val
    def __len__(self):
        return len(self._data)
    def __radd__(self, other):
        return self+other
    def __mul__(self, other):
        res=Vector(self)
        assert type(other) is int or type(other) is float:
        for i in range(len(self)):
            res[i]=self[i]*other
        return res
    def __rmul__(self, other):
        return self*other
class matrix(Vector):
    def __init__(self):
        super().__init__(self, n)
        self.SEP='\n'

if __name__=="__main__":
    print("505")