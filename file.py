file = open('slang.txt', 'r')
count = 0
d={}
for line in file:
	line = line.strip()
	for i in range(len(line)):
		if line[i] == '=':
			d[line[:i]] = line[i+1:]
file.close()
print(d)