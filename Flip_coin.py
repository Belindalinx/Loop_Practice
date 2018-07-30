#import random function
import random

#define variable
coin=random.randint(1,2)
times=0
head=0
tail=0

#flipcoin
while times<100:
    coin=random.randint(1,2)
    times+=1
    if coin==1:
        head+=1
        #print(head)
    else:
        tail+=1
        #print(tail)

print("head",head,"times")
print("tail",tail,"times")
print("coin flipped ",times,"times")