import sys
sys.path.insert(0, r'C:\Users\长颈鹿蓝调\Desktop\学习\黑马_软件测试\代码\Python学习代码\2022.8.11_考试')
from test_04.tools import Animal

class Dog(Animal):
    def eat(self):
        super().eat()
        print('吃完骨头摇摇头...')

dog = Dog('大黄')
dog.eat()