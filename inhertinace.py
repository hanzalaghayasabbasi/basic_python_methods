# Inhertiance
# Single inhertiance
# Multiple Inhertiance
# Multi Level Inhertiance
# Hybrid Inhertance

# Inhertance basic


class king:
    def __init__(self,k,s):
        self.k=k
        self.y=s
    def ot(self):
        print("My name is {0},And My Roll No is :{1}".format(self.k,self.y))

class Programmer(king):
    def s(self):
       print("My language is python");



t=king("Hanzala",21103)
t.ot()
v=king("Abdullah",211099)
v.ot()

v=Programmer("Shakkor",211097)
v.ot()
v.s()
