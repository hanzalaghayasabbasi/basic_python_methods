import time

# if you want to know you local time run it on ypoun computer
k=time.localtime()
s=time.strftime("%Y-%m-%d %H:%M:%S",k)
print(s)

# if you want to check  which code running more than yuse this


s=time.time()
for x in range(1,5,1):
   print(x)

print(time.time()-s)


sv=time.time()
x=1
while(x<5):
 x=x+1
 print(x)

print(time.time()-sv)




