#инкапсуляция +1
# 1 публичный 2 защищенный _ 3 скрытый __


class Bank:
    name='Mbank'
    def __init__(self,name,key,balance=0):
        self.name = name
        self.__key = key
        self._balance = balance

    @property
    def get_key(self):
        return self.__key
    @get_key.setter
    def get_key(self,key):
        self.__key = key

    @get_key.deleter
    def get_key(self):
        del self.__key
    # def Get_keys(self):
    #     self.__keys()
    # def __keys(self):
    #     print(self.__key)
    #
    #
    # def Set_keys(self,key):
    #     self.__key = key


    def __str__(self):
        return f'{self.name} {self._balance}'


beka = Bank('beka','2525',1000)
# print(beka.get_key)
# beka.get_key=12434214
# print(beka.get_key)
beka.get_key='21354'
print(beka)
# print(beka.get_key)
# beka._balance=100_000_000
# print(beka)
#
#
print(dir(beka))
# mro()
# print(Bank.mro())