# ООП-обьект ориент прога

P=1,'',1.2,True,None,[],{},(),1
p=tuple
print(type(p))

def a():
    ...
a()

# класс
class Car:
    #переменная внутри класса - свойсво класса
    fars='True'

    # конструктор класса
    def __init__(self,model,year,color):
        self.model=model
        self.year=year
        self.color=color
    #   функция внутри класса - метод
    def Fars(self):
        print(self.fars)

# магический метод - функция класса
    def __str__(self):
        return (f' model: {self.model}\n'
                f' year: {self.year}\n'
                f' color: {self.color}\n')

    def __len__(self):
        return len(self.fars)*2




# обьект\эклемпляр класса
car=Car('Ford',200,'red')
car2=Car('bmw',2020,'black')
car3=Car('Ford',200,'red')
car.key='1235refg'
car2.model='mers'

car3.Fars()

print(car2)
print(car)

class User:
    def __init__(self,name,age,key):
        self.name=name
        self.age=age
        self.key=key
    def nawkey(self,a):
        self.key=a
        print(self,self.key)

User.nawkey(car,'2345ty')
print(car.key)
