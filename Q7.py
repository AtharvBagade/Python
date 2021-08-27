fname = input("Enter file name: ")

file = open(fname, "r")

count = 0
while True:
	

	char = file.read(1)
	
	if char.isspace():
		count += 1
	if not char:
		break

print(count)

      
