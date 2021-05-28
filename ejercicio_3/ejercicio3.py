import random

t = random.randrange(1,1000) # test cases
print("-------------------------INPUTS-------------------------------")
print("test cases", t)
print("-------------------------OUTPUTS-------------------------------")
y = 0 # y position
k = 0 # jumps counter

def MinSaltos(y, t, k):
    for x in range(1,t+1):
        for k in range(1,121):
            #print("estoy en:", y, "y el no. salto es: ", k)
            y = y + k
            #print("al sumarle k estoy en:",y)
            if y == x:
                print("Destino=",x, "SALTOS DADOS: ", k)
                y=0
                x=0
                break
            elif y != x:
                yy2 = y -1
                if yy2 == x:
                    print("Destino=",x, "SALTOS DADOS: ", k+1)
                    y=0
                    x=0
                    break
            if k == 120:
                y2 = 0
                for k2 in range(1,121):
                    if k2 == 1:
                        #print("estoy en:", y2, "y el no. salto es: ", k2)
                        y2 = y2 - 1
                        #print("al restarle estoy en:", y2)
                    if k2 != 1:
                        #print("estoy en:", y2, "y el no. salto es: ", k2)
                        y2 = y2 + k2
                        #print("al sumarle k2 estoy en:",y2)
                        if y2 == x:
                            print("Destino=",x, "SALTOS DADOS: ", k2)
                            break
                        elif y2 != x:
                            y3 = y2 -1
                            if y3 == x:
                                print("Destino=",x, "SALTOS DADOS: ", k2+1)
                                break                

MinSaltos(y, t, k)