class Vector:
  def __init__(self,i,j,k):
    self.i=i
    self.j=j
    self.k=k



  def __str__(self):
    return "{0}i + {1}j + {2}k".format(self.i, self.j, self.k)


  def __add__(self,x):
    return Vector(self.i+x.i,self.j+x.j,self.k+x.k)

one=Vector(1,3,4)
print(one)

two=Vector(2,1,4)
print(two)
sum=one+two
print(sum)