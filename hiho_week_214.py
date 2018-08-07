import re
fileNum = int(raw_input())
fileNameStr = []
fileNameNum = []
fileNameSort = []
for i in xrange(fileNum):
	fileName = raw_input()
	fileNameSort.append(fileName)
fileNameSort.sort()
for name in fileNameSort:
	fileNameNum.extend(re.findall(r'\d+',name))
	fileNameStr.extend(re.findall(r'\D+',name))
fileNameSet = list(set(fileNameStr))
fileNameSet.sort()
for file in fileNameSet:
	i = fileNameStr.index(file)
	j = fileNameStr.count(file)
	if j == 1:
		print file+fileNameNum[i]
	else:
		fileTest = []
		for fs in fileNameNum[i:i+j]:
			fileTest.append(int(fs))
		fileTest.sort()
		for h in fileTest:
			print file+str(h)
