class node:  
    def __init__(self,ch):  
        self.ch = ch            
        self.fail = None        
        self.tail = 0           
        self.child = []        
        self.childvalue = []             
class acmation:           
    def __init__(self):                   
        self.root = node("")                     
        self.count = 0                            
    def insert(self,strkey):       
        self.count += 1                             
        p = self.root  
        for i in strkey:  
            if i not in p.childvalue:               
                child = node(i)  
                p.child.append(child)  
                p.childvalue.append(i)  
                p = child  
            else :                                 
                p = p.child[p.childvalue.index(i)]  
        p.tail = self.count                         
  
    def ac_automation(self):                                                  
        queuelist = [self.root]                     
        while len(queuelist):                      
            temp = queuelist[0]  
            queuelist.remove(temp)                  
            for i in temp.child:  
                if temp == self.root:               
                    i.fail = self.root  
                else:  
                    p = temp.fail                  
                    while p:                          
                        if i.ch in p.childvalue:    
                            i.fail = p.child[p.childvalue.index(i.ch)]  
                            break  
                        p = p.fail                 
                    if not p:                       
                        i.fail = self.root  
                queuelist.append(i)                 
 
    def runkmp(self,strmode):
        p = self.root  
        cnt = {}                                                         
        for i in strmode:          
            while i not in p.childvalue and p is not self.root:  
                p = p.fail  
            if i in p.childvalue: 
                p = p.child[p.childvalue.index(i)]  
            else :                                    
                p = self.root  
            temp = p  
            while temp is not self.root:              
                if temp.tail:
                    if temp.tail not in cnt:  
                        cnt.setdefault(temp.tail)  
                        cnt[temp.tail] = 1  
                    else:  
                        cnt[temp.tail] += 1  
                temp = temp.fail
        return cnt
n = int(raw_input())
key = []
for i in range(n):
    s = raw_input()
    key.append(s)
text = raw_input()
acp = acmation()
for i in key:
    acp.insert(i)                          
acp.ac_automation()
d = acp.runkmp(text)                    
textlist = []
for i in d.keys():
    text1 = text
    textlist.append(list(text1.replace(key[i-1],'*'*len(key[i-1]))))
output = ''
for i in range(len(text)):
    for j in range(len(textlist)):
        if textlist[j][i] == '*':
            output = output + '*'
            break
    if len(output)<(i+1):
        output = output+text[i]
print(output)