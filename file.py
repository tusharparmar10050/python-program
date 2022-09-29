data = data2 = ""

with open('fule1.txt') as fp:
	data = fp.read()

with open('fule2.txt') as fp:
	data2 = fp.read()

data += "\n"
data += data2

with open ('file3.txt', 'w') as fp:
	fp.write(data)
