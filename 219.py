'''
author@LK,sep 10
'''
def judgen3(node1,node2,node3):
    n3 = False
    if node3[0] == node1[0] and node3[1]==node2[1]:
        n3 = True
    return n3
def judgen4(node1,node2,node4):
    n4 = False
    if node4[0] == node2[0] and node4[1] == node1[1]:
        n4 = True
    return n4
# node = [[0,0],[0,1],[0,4],[1,0],[1,1],[1,4],[4,0],[4,1],[4,4]]
node = []
n = int(input())
for i in range(n):
    nd = []
    s = input().strip().split()
    nd.append(int(s[0]))
    nd.append(int(s[1]))
    node.append(nd)
Slist = []
Rlists = []
for i in range(n-1):
    for j in range(i+1,n):
        node0 = node.copy()
        node1 = node[i]
        node2 = node[j]
        node0.remove(node1)
        node0.remove(node2)
        for nd3 in node0:
            if judgen3(node1,node2,nd3):
                node0.remove(nd3)
                for nd4 in node0:
                    if judgen4(node1,node2,nd4):
                        Rlist = []
                        S = abs((node1[1]-node2[1])*(node1[0]-node2[0]))
                        Slist.append(S)
                        Rlist.append(node1)
                        Rlist.append(node2)
                        Rlist.append(nd3)
                        Rlist.append(nd4)
                        Rlists.append(Rlist)
if Slist is not None:
    print(min(Slist))
else:
    print(-1)




