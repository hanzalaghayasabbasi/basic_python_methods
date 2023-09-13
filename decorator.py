def greet(fn):
    def ms():
        print("Your id is equal")
        fn()
        print(" I am good")
    return ms

#@greet
def s():
    print("100");

    
greet(s)()

#s()


'''
def greet(fn):
    def ms(*args,**kwargs):
        print("Your id is equal")
        fn(*args,**kwargs)
        print(" I am good")
    return ms

@greet
def s(a,b):
    print(a+b);

    
#greet(s)(3,2)

s(3,2)

'''
