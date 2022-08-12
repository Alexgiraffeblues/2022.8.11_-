class Animal:
    type = '狗'
    def __init__(self, name):
        self.name = name
        self.__age = 0
    
    def eat(self):
        print('狗吃骨头', end = ',')