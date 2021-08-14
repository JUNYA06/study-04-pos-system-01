from typing import AsyncGenerator



# クラス
class Person:
    def __init__(self,name,natinality,age):
        self.name = name
        self.natinality = natinality
        self.age = age

    def __call__(self):
        print('ここはコール関数です')
    
    #メソッド
    def say_hello(self,name):
        print('こんにちは{}さん。私は{}です'.format(name,self.name))


class Saiyan(Person):
    def __init__(self,name,natinality,age,strength):
        super().__init__(name,natinality,age)
        self.strength = strength

# インスタンス化
imanishi = Person('今西','日本',25)
mike = Person('マイク','アメリカ',13)
imanishi.say_hello('佐藤')
mike.say_hello('佐藤')

# call関数は、インスタンス名+()で呼びだせる
imanishi()
goku = Saiyan('goku','宇宙',15,10000)
goku.say_hello('佐藤')
print(goku.strength)