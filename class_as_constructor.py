# Class method as Constructore Alternative

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fun(cls,string):
      name,age=string.split(',')
      return cls(name,int(age))

k=Person("Hnaza",32);
print(k.name,k.age)
s=("Han,34")
p=Person.fun(s)
print(p.name,p.age)
