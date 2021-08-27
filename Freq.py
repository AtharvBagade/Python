fname=input("Enter a filename")

file = open(fname, "r")

data = file.read()

word=input("Enter a word")

occurrences = data.count(word)
print('Number of occurrences of the word :', occurrences)               