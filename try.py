from abc import ABC, abstractmethod

class ParentAbstarctClass(ABC):

    def a(self):
        pass

    def b(self):
        print('b')

    
class Child(ParentAbstarctClass):

    def c(self):
        print('c')

x=Child()
x.b()
