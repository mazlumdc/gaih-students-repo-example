import random
m = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(3):
    l=3*(i-1)
    for j in range(3):
        n = True
        while n:
            a = random.randint(2,100)
            for k in range(2,a):
                if a%k==0:
                    asal = False
                    break
                else:
                    asal = True
            if asal:
                m[i][j]=a
                l=l+1
                n=False
    print(m[i])
