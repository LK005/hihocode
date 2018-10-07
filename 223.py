line1 = input().split()
n = int(line1[0])
xy = [int(x)for x in line1[1:]]
linent = []
for i in range(n):
    linent.append([int(y) for y in input().split()])
print(linent)
linen = sorted(linent)
print(linen)
x = xy[0];y = xy[1]
R = []
c = 1
if xy in linen:
    print(1)
else:
    if linen[0][0] <= x:
        x0 = linen[0][0]
        s = 0
        while True:
            R0t = []
            R0t = [r for r in linen[c-1:] if r[0]<=x0]
            R0 = sorted(R0t,key=lambda r:r[1])
            print(R0)
            if len(R0) != 0:
                c += len(R0)
                x0 = R0[-1][1]
                R.append(x0)
                if x0>=y:
                    print(len(R))
                    break
            else:
                print(-1)
                break
    else:
        print(-1)
'''
LK005
'''
