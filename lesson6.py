
class A(object):
    def __init__(self,a):
        self.a=a

class B(A):
    def ls(self):
        print('это метод А')

print(A.mro())
print(B.mro())

class C:
    def __init__(self, name):
        self.name = name
    def ls(self):
        print('это метод С')

class D(B,C,A):...

print(D.mro())
d=D('A')
print(d.name)
d.ls()
# MRO -