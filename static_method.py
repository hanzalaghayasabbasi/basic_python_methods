# Static method doesnot belong to clasas and instanece but we made static method when we donot 
# want to call or used  instance eof class an we donot want to used self in it


class math:
     def __init__(self,num):
      self.num=num
      
     def test(self):
       print(self.num)
      
     @staticmethod
     def add(a,b):
         return a+b

k=math(12)
k.test()
print(math.add(1,2))
# second method of calling
print(k.add(1,4))
# error
# print(add(1,2))