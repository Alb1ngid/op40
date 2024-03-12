# Принципы ооп - 4 Наследование Полиморфизм инкапсуляция абстракция

# 1 наследование
# 2 полиморфизм






# суперкласс\родительским классом
class A:
    name='l'
    def __init__(self,name,radius):
        self.name = name
        self.radius = radius
    def XY(self,x,y):
        self.fine()
        print(x,y)

    def wrong(self):
        print('привет')



# дочерний класс\подкласс
class Rectangle(A):
    def __init__(self,name,radius,color):
        super().__init__(name,radius)
        A.__init__(self,name,radius)
        self.color = color

    name='прямоугольник'
    def wrong(self):
        print(f'привет {self.name}')

    def vizion(self):
        self.wrong()
        super().wrong()

    def fine(self):
        self.wrong()

        print(self.name)

class Figure(A):
    name='квадрат'

    def vizion(self):
        self.wrong()

    def fine(self):
        print(self.name)


a=A('name',radius='100')
a.wrong()

d=Rectangle('name','1','red')
d.vizion()
# DRY