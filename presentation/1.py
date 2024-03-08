import random
import matplotlib
import matplotlib.pyplot as plt

a = 1
e = 0.0

for i in range(20):
    p = random.random()
    if (a==1):
        if(p<1):
            a = 2
    elif (a==2):
        if(p<1.0/2 - 4*e):
            a = 2
        elif(p<3.0/4 - 3*e):
            a = 5
        elif(p< 7.0/8 - 2*e):
            a = 4
        elif(p<1-e):
            a=3
        else:
            a = 1
    elif (a==3):
        if(p<1.0/2-4*e):
            a = 3
        else:
            a = 2
    elif (a==4):
        if(p<1.0/2-4*e):
            a = 4
        else:
            a = 2
    elif (a==5):
        if(p<1-4*e):
            a = 5
        else:
            a = 2
    print(a, p)