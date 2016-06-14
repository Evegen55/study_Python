import math
def abc():
    i = 100
    b = 0;
    c = 0;
    d = 0;
    cubs = 0;
    while i < 1000:
        a = str(i)
        b = int(a[0])
        c = int(a[1])
        d = int(a[2])
        cubs = (math.pow(b, 3) + math.pow(c, 3)+ math.pow(d, 3))
        if (cubs == i):
            print(i,"\t")
        i = i + 1   
abc()        