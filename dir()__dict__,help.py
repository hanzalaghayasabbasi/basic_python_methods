# dir __dict__ help attribute
class Person:
  def __init__(self, name, age):
      self.name = name
      self.age = age
      self.version = 1

    
p = Person("John", 30)
print(p.__dict__)

print(help(Person))


x={1,2,3}

print(x)
#print(dir(x))
#print(x.__add__)
# error no method
#print(x.__addx__)

#print(x.__dict__)
print(help(x))
