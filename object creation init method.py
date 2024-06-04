class Person:
    def __init__(card,name):
        card.name=name
        
    def say_hi(card):
        print('Hello,my name is',card.name)
        
p=Person(' Nandu  ')
p.say_hi()