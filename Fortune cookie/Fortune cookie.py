import random

input("let me tell you your luck today")

fortune=random.randint(1,5)
if fortune==1:
    print("You are super lucky today")
elif fortune==2:
    print("You are lucky today")
elif fortune==3:
    print("You are soso today")
elif fortune==4:
    print("You are bad luck today")
else:
    print("You are super bad today")

input("press enter to end")