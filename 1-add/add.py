import fileinput

add = 0
for line in fileinput.input():
	add += float(line)

if add/int(add) == 1:
	print(int(add))
else:
	print(add)