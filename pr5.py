class A:
    def pr(self):
        print("I am pr from A")
        print(self.f())
    def f(self):
        return -1
class B(A):
    def f(self):
        return 128
if __name__=="__main__":
    obj=A()
    obj.pr()
    del obj
    obj=B()
    obj.pr()
