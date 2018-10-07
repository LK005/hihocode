n = int(raw_input())
key = []
for i in xrange(n):
    s = raw_input()
    key.append(s)
text = raw_input()                   
textlist = []
for ss in key:
    text1 = text
    if ss in text:
        textlist.append(list(text1.replace(ss,'*'*len(ss))))
output = ''
for i in xrange(len(text)):
    for j in xrange(len(textlist)):
        if textlist[j][i] == '*':
            output = output + '*'
            break
    if len(output)<(i+1):
        output = output+text[i]
print output