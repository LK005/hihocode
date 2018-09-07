# n = int(input())
# strn = []
# for i in range(n):
#     s = input()
#     strn.append(s)
# c = len(strn)
# for j in range(c-1):
#     for t in range(j+1,c+1):
#     if strn[j][-1] == strn[t][0]:
#         ss = strn[j][:-1]+strn[j][-1]+strn[t][1:]
#         strn.append(ss)
#     if strn[t][-1] == strn[j][0]:
#         ss1 = strn[t][:-1]+strn[t][-1]+strn[j][1:]
#         strn.append(ss1)
# for strt in 

n = int(input())
strn = []
for i in range(n):
    s = input()
    strn.append(s)
goalstr = input()
strdf = {}
strdb = {}
strl = []
strnt = strn.copy()
strlist = [chr(i) for i in range(ord('a'),ord('z')+1)]
for s in strlist:
    for ss in strn:
        if ss[0] == s:
            if s not in strdf.keys():
                strdf[s] = list(ss)
            else:
                strdf[s].append(ss)
for s in strlist:
    for ss in strn:
        if ss[-1] == s:
            if s not in strdb.keys():
                strdb[s] = list(ss)
            else:
                strdb[s].append(ss)
print(strdf)
print(strdb)