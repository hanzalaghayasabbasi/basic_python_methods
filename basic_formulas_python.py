import pandas


 
print('1*5"love" "king" \'dd\'\n ok not you',3,5,sep="~",end='\n5')
print("love")
print("love")


a=1
c=complex(5,7)
print(a)
k=None
print("The type of a is = ",type(c))
print("The type of a is = ",type(a))
print(a+c)

# list mutable

list=[8,2.3,[-4,5],["apple","banana"]],
print("\n",list)

# tuple immutable

tuple=(("parrot","sparrow"),("lion","tiger"))
print("\n",tuple)

#dictonary
dict={"name":"Hanzala","Roll":211099,
       "Sec":"BSCYS-B4",
       "CanVote":True}
print("\n",dict)

a=5
b=4
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)
print(a%b)


# Typecating
# The Conversion of one datatype into othrt data type is called Typecasting
# python support wide Variety of function or method like
# str(),ord(),hex(),oct(),tuple(),set(),list(),dict() etc are tyecasting in # # python if # it is convertable then it will convert for example not harry to int
a="1"
b="2"
print(a+b)
a=1
b=2
print(a+b)
a="1"
b="2"
print(int(a+b))
print("apply on single")
print(int(a)+int(b))


# User input

a,b=3,"5"
print(int(a)+int(b))

# if there is only input python will take it as a string for instance
k=input("Enter a number :")
c=input("Enter a number :")
print(k+c)

# NOW CHANGING TYPE OF INPUT TO INT5
k=int(input("Enter a number :"))
c=int(input("Enter a number :"))
print(k+c)

# NOW CHANGING TYPE OF INPUT TO Float
k=float(input("Enter a number :"))
c=float(input("Enter a number :"))
print(k+c)