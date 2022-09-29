val = input("enter the saprated numbers: ")


list = val.split(',')

# tuple = tuple(list)

print('list', list)
# print('tuple', tuple)
for i in range(len(list)):
	if list.count('15') == 2:
		print(list[i])
	else:
		print("helo",list[i])
