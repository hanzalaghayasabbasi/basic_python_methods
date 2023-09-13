#Access Modfier
#Public:
#Protected
#Private
# There is no public private and protected but these are naming conventional in python

'''
class first:
    def __init__(self,k,r):
        self.k=k
        self.r=r

    def fun1(self):
       print("I am default {0},In the {1}".format(self.k,self.r))


class second(first):
       def fun2(self):
           print("Ok I am good")



k=first("Public","Program")
k.fun1()
# k.fun2() error
k=second("Public","Program")
k.fun1()
k.fun2()
'''
# Protected _
'''
class first:
    def __init__(self,k,r):
        self._k=k
        self._r=r

    def _fun1(self):
       print("I am default {0},In the {1}".format(self._k,self._r))


class second(first):
       def _fun2(self):
           print("Ok I am good")



k=first("Protected","Program")
k._fun1()
# k.fun2() error
k=second("protected","Program")
k._fun1()
k._fun2()
'''

#Private




class first:
    def __init__(self,k,r):
        self.__k=k
        self.__r=r

    def __fun1(self):
       print("I am default {0},In the {1}".format(self.__k,self.__r))


class second(first):
       def __fun2(self):
           print("Ok I am good")



k=first("Private","Program")
k._first__fun1()
# k.fun2() error
k=second("Private","Program")
k._first__fun1()
k._second__fun2()
