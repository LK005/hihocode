# _*_ code:utf-8 _*_
class trienode:
    def __init__(self):
        self.__map = {}
        self.__end = False
    def set(self,str,off):
        if len(str)==off:
            self.__end = True
            return
        c = str[off]
        if c not in self.__map:
            self.__map[c] = trienode()
        p = self.__map[c]
        p.set(str,off+1)
    def test(self,str,off):
        if len(str)==off:
            if self.__end:
                return 0
            else:
                return -1
        c = str[off]
        if c not in self.__map:
            if self.__end:
                return 0
            else:
                return -1
        t1=-1
        if self.__end:
            t1=0
        t2 = self.__map[c].test(str,off+1)
        if t2!=-1:
            return t2+1
        return t1

n = int(raw_input())
root = trienode()
for i in range(0,n):
    str = raw_input().strip()
    root.set(str,0)
str = raw_input()
l1 = len(str)
rsl = []
t1 = 0
for i in range(0,l1):
    c = str[i]
    q=root.test(str[i:],0)
    
    if q+i>t1:
        t1=q+i
    if i<t1:
        c = '*'
    rsl.append(c)
print ''.join(rsl)






