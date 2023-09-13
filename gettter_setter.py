#getter 

'''

class k:
    def __init__(self,a):
        self.a=a
    @property
    def s(self):

     return 10*self.a

p=k(10);
p.a=9
d=p.s
print(d)

'''

#getter an setter

class k:
    def __init__(self,a):
        self.a=a
    @property
    def s(self):

     return 10*self.a
  
    @s.setter
    def s(self,val):
      self.a=val

p=k(10);
p.a=9
d=p.s
print(d)
p.s=3
d=p.s
print(d)



