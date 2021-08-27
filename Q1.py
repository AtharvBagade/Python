fname=input("Enter a filename:")

file1 = open(fname, "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London"]
file1.writelines(L)
file1.close()


file1 = open(fname, "a")


file1.write("\n")
file1.write("Today")

file1.write("Tomorrow")


file1 = open(fname, "r")
print("Output of Readlines after appending")
print(file1.read())
print()
file1.close()
